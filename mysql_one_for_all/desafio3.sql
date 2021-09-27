CREATE VIEW SpotifyClone.historico_reproducao_usuarios AS
SELECT u.nome_usuario AS "usuario",
m.nome_musica AS "nome"
FROM SpotifyClone.usuarios AS u
INNER JOIN SpotifyClone.historico_reproducoes as hr
ON u.id = hr.usuario_id
INNER JOIN SpotifyClone.musicas as m
ON hr.musica_id = m.id
ORDER BY u.nome_usuario, m.nome_musica;
