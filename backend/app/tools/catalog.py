# backend/app/tools/catalog.py

from langchain.agents import tool
from app.database.queries import find_products_by_keyword, get_product_by_sku
import json
from decimal import Decimal # <--- ADD THIS LINE

@tool
def search_product_catalog(query: str) -> str:
    """
    Use this tool to search the product catalog for items matching a customer's query.
    It returns a JSON string of product details including SKU, name, description, stock level,
    and pricing rules. If no products are found, it returns an empty list.
    """
    print(f"TOOL: Searching for product: '{query}'")
    results = find_products_by_keyword(query)

    # Convert numeric types to float for JSON serialization
    for item in results:
        for key, value in item.items():
            # This check now includes the Decimal type
            if isinstance(value, (Decimal, int, float)) and key not in ['id', 'stock_level', 'discount_threshold_quantity', 'delivery_eta_days']:
                item[key] = float(value)
    return json.dumps(results)

# The generate_quote function is already correct because it casts to float. No changes needed here.
@tool
def generate_quote(sku: str, quantity: int) -> str:
    """
    Use this tool to generate a final quote for a specific product SKU and quantity.
    It calculates the total price, applies any volume discounts, checks stock availability,
    and returns a final JSON object representing the quote.
    """
    print(f"TOOL: Generating quote for SKU {sku}, quantity {quantity}")
    product_data = get_product_by_sku(sku)
    if not product_data:
        return json.dumps({"error": "Product not found for SKU.", "sku": sku})

    p = product_data
    in_stock = p['stock_level'] >= quantity
    base_price = float(p['base_price'])

    subtotal = base_price * quantity
    discount_percent = 0.0
    if p['discount_threshold_quantity'] and quantity >= p['discount_threshold_quantity']:
        discount_percent = float(p['discount_percentage'])

    discount_amount = subtotal * (discount_percent / 100.0)
    total_price = subtotal - discount_amount

    quote = {
        "sku": p['sku'],
        "product_name": p['name'],
        "quantity": quantity,
        "in_stock": in_stock,
        "unit_price": base_price,
        "subtotal": round(subtotal, 2),
        "discount_applied_percent": discount_percent,
        "discount_amount": round(discount_amount, 2),
        "total_price": round(total_price, 2),
        "delivery_eta_days": p['delivery_eta_days'],
    }
    return json.dumps(quote)
