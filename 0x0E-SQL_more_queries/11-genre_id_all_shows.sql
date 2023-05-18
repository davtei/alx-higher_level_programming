-- A script that lists all shows contained in the database hbtn_0d_tvshows.
-- Each record displays: tv_shows.title - tv_show_genres.genre_id, in ascending order of tv_shows.title and tv_show_genres.genre_id
-- Displays NULL if a show does not have a genre
-- Uses only one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows
        LEFT JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
    ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;