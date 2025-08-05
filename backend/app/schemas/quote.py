from pydantic import BaseModel
from typing import Optional

class ProductInquiry(BaseModel):
    query: str
    customer_id: Optional[str] = "guest"

class QuoteDetails(BaseModel):
    sku: str
    product_name: str
    quantity: int
    in_stock: bool
    unit_price: float
    subtotal: float
    discount_applied_percent: float
    discount_amount: float
    total_price: float
    delivery_eta_days: int

class QuoteResponse(BaseModel):
    natural_language_summary: str
    invoice_json: Optional[QuoteDetails] = None
