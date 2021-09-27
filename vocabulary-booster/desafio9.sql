SELECT CONCAT(E.FirstName, ' ', E.LastName) AS "Nome completo",
COUNT(OD.EmployeeID) AS "Total de pedidos"
FROM w3schools.employees AS E
INNER JOIN w3schools.orders AS OD
ON E.EmployeeID = OD.EmployeeID
GROUP BY OD.EmployeeID
ORDER BY COUNT(OD.EmployeeID);
