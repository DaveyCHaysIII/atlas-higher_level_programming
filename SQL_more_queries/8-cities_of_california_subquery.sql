-- write a script that lists all the cities in california in a database
SELECT 'id', 'name' FROM 'cities' WHERE state_id = (
    SELECT 'id' FROM 'states' WHERE 'name' = 'California' 
) ORDER BY 'id';
