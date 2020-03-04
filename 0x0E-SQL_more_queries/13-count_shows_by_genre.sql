-- A script that lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each
SELECT tv_genres.name as genres, COUNT(tv_genres.name) as number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genres
ORDER BY number_of_shows DESC;
