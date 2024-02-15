-- list_genres_by_rating.sql
-- This script lists all genres in the hbtn_0d_tvshows_rate database by their rating


-- List genres by their rating sum, sorted in descending order
SELECT tv_genres.name, SUM(tv_ratings.rating) AS rating_sum
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_ratings ON tv_show_genres.show_id = tv_ratings.show_id
GROUP BY tv_genres.id
ORDER BY rating_sum DESC;
