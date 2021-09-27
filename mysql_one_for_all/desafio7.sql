CREATE VIEW SpotifyClone.perfil_artistas AS
SELECT art.nome_artista AS `artista`,
alb.nome_album AS `album`,
COUNT(ls.usuario_id) AS `seguidores`
FROM SpotifyClone.artistas AS art
INNER JOIN SpotifyClone.albuns AS alb
ON art.id = alb.artista_id
INNER JOIN SpotifyClone.lista_seguidores AS ls
ON art.id = ls.artista_id
GROUP BY alb.id
ORDER BY `seguidores` DESC, art.nome_artista, alb.nome_album;
