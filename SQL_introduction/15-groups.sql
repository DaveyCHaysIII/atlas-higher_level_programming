-- this script displays all rows with the same score in second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
