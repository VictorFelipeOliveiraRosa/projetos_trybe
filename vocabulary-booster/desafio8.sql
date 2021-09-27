SELECT C.ContactName AS "Nome de contato",
SH.ShipperName AS "Empresa que fez o envio",
OD.OrderDate AS "Data do pedido"
FROM w3schools.customers AS C
INNER JOIN w3schools.orders AS OD
ON C.CustomerID = OD.CustomerID
INNER JOIN w3schools.shippers AS SH
ON OD.ShipperID = SH.ShipperID
WHERE SH.ShipperName = "Speedy Express"
OR SH.ShipperName = "United Package"
ORDER BY C.ContactName, SH.ShipperName, OD.OrderDate;
