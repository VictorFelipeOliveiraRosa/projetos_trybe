CREATE VIEW SpotifyClone.estatisticas_musicais AS
SELECT
COUNT(c.id) AS "cancoes",
(SELECT COUNT(art.id) FROM SpotifyClone.artistas AS art) AS "artistas",
(SELECT COUNT(alb.id) FROM SpotifyClone.albuns AS alb) AS "albuns"
FROM SpotifyClone.musicas AS c;
