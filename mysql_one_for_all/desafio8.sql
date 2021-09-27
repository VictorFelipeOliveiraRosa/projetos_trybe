DELIMITER $$
CREATE TRIGGER trigger_usuario_delete
BEFORE DELETE ON SpotifyClone.usuarios
FOR EACH ROW
BEGIN
DELETE hr, ls 
FROM SpotifyClone.historico_reproducoes AS hr
INNER JOIN SpotifyClone.lista_seguidores AS ls
ON hr.usuario_id = ls.usuario_id
WHERE hr.usuario_id = OLD.id;
END $$
DELIMITER ;
