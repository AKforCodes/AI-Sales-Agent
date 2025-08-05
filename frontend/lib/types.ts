export interface QuoteDetails {
  sku: string;
  product_name: string;
  quantity: number;
  in_stock: boolean;
  unit_price: number;
  subtotal: number;
  discount_applied_percent: number;
  discount_amount: number;
  total_price: number;
  delivery_eta_days: number;
}

export interface QuoteResponse {
  natural_language_summary: string;
  invoice_json: QuoteDetails | null;
}
