-- list_shows_by_rating.sql
-- This script lists all shows from hbtn_0d_tvshows_rate by their rating


-- List shows by their rating sum, sorted in descending order
SELECT tv_shows.title, SUM(tv_ratings.rating) AS rating_sum
FROM tv_shows
JOIN tv_ratings ON tv_shows.id = tv_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating_sum DESC;
