-- Write a script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title, tv_genres.name AS genre, SUM(tv_show_ratings.rate) AS rating 
FROM tv_show_ratings 
JOIN tv_shows ON tv_shows.id = tv_show_ratings.show_id 
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_shows.title 
ORDER BY rating DESC;
