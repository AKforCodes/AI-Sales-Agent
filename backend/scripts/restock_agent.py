import os
import sys
from dotenv import load_dotenv

# Add the parent directory to the Python path to allow importing from 'app'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database.queries import _run_query

load_dotenv()

def check_low_stock():
    """Checks for products below their restock threshold."""
    query = "SELECT sku, name, stock_level, restock_threshold FROM products WHERE stock_level < restock_threshold;"
    return _run_query(query)

def generate_restock_alert(products: list):
    """Generates a plain text alert for products that need restocking."""
    if not products:
        return None

    alert = "--- URGENT: LOW INVENTORY ALERT ---\n"
    alert += f"Generated on: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    alert += "The following products are running low on stock and require reordering:\n\n"
    for p in products:
        alert += f"- SKU: {p['sku']}\n"
        alert += f"  Name: {p['name']}\n"
        alert += f"  Current Stock: {p['stock_level']} (Threshold is {p['restock_threshold']})\n\n"

    alert += "Please create purchase orders immediately.\n"
    alert += "--- END OF ALERT ---"
    return alert

if __name__ == "__main__":
    print("Running daily inventory check...")
    low_stock_products = check_low_stock()
    if low_stock_products:
        alert_message = generate_restock_alert(low_stock_products)
        print(alert_message)
        # In a real system, you would email this alert:
        # send_email('procurement@distributor.com', 'URGENT: Low Inventory Alert', alert_message)
    else:
        print("All product stock levels are healthy.")
