DELIMITER $$
CREATE FUNCTION SpotifyClone.quantidade_musicas_no_historico(identificador INT)
RETURNS INT READS SQL DATA
BEGIN
DECLARE total INT;
SELECT COUNT(hr.musica_id)
FROM SpotifyClone.historico_reproducoes AS hr
INNER JOIN SpotifyClone.usuarios AS u
ON hr.usuario_id = u.id
WHERE u.id = identificador
INTO total;
RETURN total;
END $$
DELIMITER ;
