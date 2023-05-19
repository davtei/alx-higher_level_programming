-- A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- display NULL in the genre column if a show doesn’t have a genre
-- Each record displays: tv_shows.title - tv_genres.name
-- Results are sorted in ascending order by the show title and genre name
-- Uses only one SELECT statement
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;