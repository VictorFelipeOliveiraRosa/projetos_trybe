UPDATE northwind.order_details
SET discount = 30
WHERE id IN (
SELECT * FROM(
SELECT id FROM northwind.order_details
WHERE unit_price < 10.0000)price);
