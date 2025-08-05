from typing import List, Dict, Any
from app.database.connection import get_db_connection
from psycopg2.extras import DictCursor
import json

def _run_query(query: str, params: tuple = ()) -> List[Dict[str, Any]]:
    """Execute query and return results"""
    conn = get_db_connection()
    try:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query, params)
            if cur.description:
                results = [dict(row) for row in cur.fetchall()]
            else:
                results = []
            conn.commit()
            return results
    finally:
        conn.close()

def find_products_by_keyword(keyword: str) -> List[Dict[str, Any]]:
    """Find products using full-text search"""
    query = """
        SELECT p.id, p.sku, p.name, p.description, p.stock_level,
               pr.base_price, pr.discount_threshold_quantity, pr.discount_percentage, pr.delivery_eta_days
        FROM products p
        LEFT JOIN pricing_rules pr ON p.id = pr.product_id
        WHERE to_tsvector('english', p.name || ' ' || p.description) @@ plainto_tsquery('english', %s);
    """
    return _run_query(query, (keyword,))

def get_product_by_sku(sku: str) -> Dict[str, Any] | None:
    """Find product by SKU"""
    query = """
        SELECT p.id, p.sku, p.name, p.description, p.stock_level,
               pr.base_price, pr.discount_threshold_quantity, pr.discount_percentage, pr.delivery_eta_days
        FROM products p
        LEFT JOIN pricing_rules pr ON p.id = pr.product_id
        WHERE p.sku = %s;
    """
    results = _run_query(query, (sku,))
    return results[0] if results else None

def log_quote_in_db(inquiry: str, quote: Dict[str, Any]):
    """Log quote to order history"""
    quote_json = json.dumps(quote)
    query = "INSERT INTO order_history (customer_inquiry, generated_quote_json) VALUES (%s, %s);"
    _run_query(query, (inquiry, quote_json))
