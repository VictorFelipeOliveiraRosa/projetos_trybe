CREATE VIEW SpotifyClone.cancoes_premium AS
SELECT m.nome_musica AS `nome`,
COUNT(hr.musica_id) AS `reproducoes`
FROM SpotifyClone.musicas AS m
INNER JOIN SpotifyClone.historico_reproducoes AS hr
ON m.id = hr.musica_id
INNER JOIN SpotifyClone.usuarios AS u
ON hr.usuario_id = u.id
INNER JOIN SpotifyClone.planos AS p
ON u.plano_id = p.id
WHERE p.nome_plano IN("familiar", "universitario")
GROUP BY m.nome_musica
ORDER BY m.nome_musica;
