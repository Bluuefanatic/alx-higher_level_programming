-- List genres and the number of shows linked to each
SELECT genres.genre as genre, COUNT(tv_show_genres.show_id) as number_of_shows
FROM genres
LEFT JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.genre
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
