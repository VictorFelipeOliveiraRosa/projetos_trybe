DELIMITER $$
CREATE PROCEDURE SpotifyClone.albuns_do_artista(IN get_artista VARCHAR(20))
BEGIN
SELECT art.nome_artista AS `artista`,
alb.nome_album AS `album`
FROM SpotifyClone.artistas AS art
INNER JOIN SpotifyClone.albuns AS alb
ON art.id = alb.artista_id
WHERE art.nome_artista = get_artista
ORDER BY alb.nome_album;
END $$
DELIMITER ;
