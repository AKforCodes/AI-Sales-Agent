-- Sample data for the products table
-- This data is more diverse, including electronics, office supplies, and kitchenware.
INSERT INTO products (sku, name, description, stock_level, restock_threshold) VALUES
('LT-MAC-PRO-16', '16-inch Pro Laptop', 'A high-end laptop with a powerful processor, 16GB RAM, and 1TB SSD.', 30, 10),
('MO-DELL-U27', '27-inch 4K Monitor', 'A professional Ultra HD monitor with excellent color accuracy.', 50, 20),
('KB-LOGI-MX', 'MX Advanced Wireless Keyboard', 'A comfortable, backlit keyboard for professionals.', 150, 40),
('DT-HPM-PRO', 'Pro Desktop PC', 'A reliable desktop computer for business use, includes keyboard and mouse.', 25, 10),
('CP-PPR-A4-500', 'A4 Copy Paper Ream', 'A 500-sheet ream of standard 80gsm A4 printer paper.', 800, 200),
('PN-PILOT-G2-BLK', 'Gel Ink Rollerball Pens (12-pack, Black)', 'A pack of 12 smooth-writing black gel ink pens.', 450, 100),
('NB-MOLE-LG-PLN', 'Large Hardcover Notebook (Plain)', 'A classic large notebook with 240 plain, acid-free pages.', 250, 50),
('CM-NESP-VRT', 'Espresso & Coffee Machine', 'A single-serve machine for brewing coffee or espresso.', 75, 25),
('BL-VITAMIX-5200', 'High-Performance Blender', 'A powerful blender for smoothies, soups, and more. 64-ounce container.', 40, 15),
('HD-SENN-HD650', 'Open-Back Audiophile Headphones', 'Reference-class headphones for critical listening.', 60, 20);

-- Sample data for the pricing_rules table
-- Corresponds to the new, diverse product set.
INSERT INTO pricing_rules (product_id, base_price, discount_threshold_quantity, discount_percentage, delivery_eta_days) VALUES
((SELECT id from products where sku='LT-MAC-PRO-16'), 2399.00, NULL, NULL, 5),
((SELECT id from products where sku='MO-DELL-U27'), 749.99, 5, 5.0, 3),
((SELECT id from products where sku='KB-LOGI-MX'), 99.99, 10, 7.5, 2),
((SELECT id from products where sku='DT-HPM-PRO'), 1199.50, 3, 10.0, 4),
((SELECT id from products where sku='CP-PPR-A4-500'), 5.50, 50, 15.0, 1),
((SELECT id from products where sku='PN-PILOT-G2-BLK'), 14.99, 20, 10.0, 1),
((SELECT id from products where sku='NB-MOLE-LG-PLN'), 19.95, NULL, NULL, 2),
((SELECT id from products where sku='CM-NESP-VRT'), 159.00, NULL, NULL, 3),
((SELECT id from products where sku='BL-VITAMIX-5200'), 449.95, 2, 5.0, 3),
((SELECT id from products where sku='HD-SENN-HD650'), 399.95, NULL, NULL, 4);
