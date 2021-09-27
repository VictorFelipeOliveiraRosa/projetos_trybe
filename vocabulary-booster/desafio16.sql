DELIMITER $$
CREATE FUNCTION buscar_quantidade_de_empregos_por_funcionario(email VARCHAR(50))
RETURNS INT READS SQL DATA
BEGIN
DEClARE total_empregos_funcionario INT;
SELECT COUNT(JH.EMPLOYEE_ID) 
FROM hr.job_history AS JH
INNER JOIN hr.employees AS E
ON JH.EMPLOYEE_ID = E.EMPLOYEE_ID
WHERE E.EMAIL LIKE CONCAT('%', email, '%')
INTO total_empregos_funcionario;
RETURN total_empregos_funcionario;
END $$
DELIMITER ;
