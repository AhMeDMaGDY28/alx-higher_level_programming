-- Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- First, select all shows linked to the genre Comedy
SELECT tv_shows.title 
FROM tv_shows 
WHERE tv_shows.title NOT IN (
    SELECT tv_shows.title 
    FROM tv_show_genres 
    JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id 
    JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id 
    WHERE tv_genres.name = 'Comedy'
) 
ORDER BY tv_shows.title;
