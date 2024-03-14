-- Write a script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id 
WHERE tv_show_genres.genre_id is NULL 
ORDER BY tv_shows.title, tv_show_genres.genre_id;