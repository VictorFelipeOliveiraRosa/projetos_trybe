DELIMITER $$
CREATE FUNCTION exibir_quantidade_pessoas_contratadas_por_mes_e_ano(hire_month INT, hire_year INT)
RETURNS INT READS SQL DATA
BEGIN
DECLARE total_employees INT;
SET @month_n = IF(hire_month < 10, lpad(hire_month, 2, 0), hire_month);
SELECT COUNT(HIRE_DATE) FROM hr.employees
WHERE HIRE_DATE LIKE CONCAT(hire_year, '-', @month_n, '%')
INTO total_employees;
RETURN total_employees;
END $$
DELIMITER ;
