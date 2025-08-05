-- Drop existing tables to start fresh
DROP TABLE IF EXISTS order_history;
DROP TABLE IF EXISTS pricing_rules;
DROP TABLE IF EXISTS products;

-- products: Stores core product information and stock levels.
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    sku VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    stock_level INTEGER NOT NULL DEFAULT 0,
    restock_threshold INTEGER NOT NULL DEFAULT 50
);

-- pricing_rules: Defines pricing and business logic for each product.
CREATE TABLE pricing_rules (
    id SERIAL PRIMARY KEY,
    product_id INTEGER UNIQUE REFERENCES products(id) ON DELETE CASCADE,
    base_price NUMERIC(10, 2) NOT NULL,
    -- Tiered discounting
    discount_threshold_quantity INTEGER,
    discount_percentage NUMERIC(5, 2),
    -- Delivery ETA
    delivery_eta_days INTEGER NOT NULL DEFAULT 3
);

-- order_history: Logs all inquiries and generated quotes.
CREATE TABLE order_history (
    id SERIAL PRIMARY KEY,
    customer_inquiry TEXT NOT NULL,
    generated_quote_json JSONB,
    status VARCHAR(20) DEFAULT 'quoted', -- e.g., 'quoted', 'ordered', 'fulfilled'
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Add indexes for faster lookups
CREATE INDEX idx_products_name ON products USING GIN (to_tsvector('english', name));
CREATE INDEX idx_products_description ON products USING GIN (to_tsvector('english', description));
