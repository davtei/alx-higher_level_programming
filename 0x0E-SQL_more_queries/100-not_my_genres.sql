-- A script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record displays: tv_genres.name
-- Results are be sorted in ascending order by the genre name
-- Uses only one SELECT statement
SELECT name
    FROM tv_genres
        WHERE name NOT IN
            (SELECT name
                FROM tv_genres
                    LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
                    LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
                    WHERE tv_shows.title = 'Dexter')
    GROUP BY name
    ORDER BY name ASC;