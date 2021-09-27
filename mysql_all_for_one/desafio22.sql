UPDATE northwind.order_details
SET discount = 15
WHERE id IN (SELECT * FROM(SELECT id FROM northwind.order_details
WHERE discount <> 15)menor);
