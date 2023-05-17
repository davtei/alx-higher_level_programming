-- A script that imports a table dump into hbtn_0c_0 database
-- Displays the max temperature of each state (ordered by State name).
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;