CREATE VIEW SpotifyClone.top_2_hits_do_momento AS
SELECT m.nome_musica AS "cancao",
COUNT(hr.musica_id) AS `reproducoes`
FROM SpotifyClone.musicas AS m
INNER JOIN SpotifyClone.historico_reproducoes AS hr
ON m.id = hr.musica_id
GROUP BY hr.musica_id
ORDER BY `reproducoes` DESC, m.nome_musica
LIMIT 2;
