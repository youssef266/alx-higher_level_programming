-- script for listing records with a score >= 10 and order by descending
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;
