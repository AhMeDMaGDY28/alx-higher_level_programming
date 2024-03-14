-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 11-genre_id_all_shows.sql)
-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv_show_genres.genre_id AS genre,
       COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;

