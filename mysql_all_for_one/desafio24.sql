UPDATE northwind.order_details
SET discount = 45
WHERE id IN (
SELECT * FROM(
SELECT id FROM northwind.order_details
WHERE unit_price > 10.0000 AND id BETWEEN 30 AND 40)disc);
