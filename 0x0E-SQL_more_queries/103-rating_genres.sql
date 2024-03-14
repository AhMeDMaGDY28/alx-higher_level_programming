-- Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name, SUM(rating) AS rating_sum
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
