CREATE VIEW SpotifyClone.top_3_artistas AS
SELECT art.nome_artista AS "artista",
COUNT(ls.artista_id) AS `seguidores`
FROM SpotifyClone.artistas AS art
INNER JOIN SpotifyClone.lista_seguidores AS ls
ON art.id = ls.artista_id
GROUP BY ls.artista_id
ORDER BY `seguidores` DESC, art.nome_artista
LIMIT 3;
