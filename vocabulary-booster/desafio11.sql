SELECT C.ContactName AS "Nome",
C.Country AS "País",
(SELECT COUNT(C3.Country) - 1
FROM w3schools.customers AS C3
WHERE C3.Country = C.Country
GROUP BY C3.Country) AS "Número de compatriotas"
FROM w3schools.customers AS C
WHERE (SELECT COUNT(C3.Country)
FROM w3schools.customers AS C3
WHERE C3.Country = C.Country
GROUP BY C3.Country) >= 2
ORDER BY C.ContactName;
