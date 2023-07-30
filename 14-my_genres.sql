-- This script uses the database to list all genres of the show Dexter
SELECT g.name
FROM tv_genres AS g
INNER JOIN tv_shows_genres AS s
ON g.id = s.genre_id
INNER JOIN tv_shows as t
ON t.id = s.show_id
WHERE t.title = "Dexter"
ORDER BY g.name ASC;
