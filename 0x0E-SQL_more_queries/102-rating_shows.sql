-- A script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record displays: tv_shows.title - rating sum
-- Results are sorted in descending order by the rating
-- Uses only one SELECT statement
SELECT title, SUM(rate) AS rating
    FROM tv_shows
        INNER JOIN tv_show_ratings AS r
        ON tv_shows.id = r.show_id
    GROUP BY title
    ORDER BY rating DESC;