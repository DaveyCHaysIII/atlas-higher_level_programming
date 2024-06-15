--write a script that lists all cities in database
SELECT id, name, states.name 
FROM cities
LEFT JOIN states ON cities.state_id = state_id
ORDER BY cities.id ASC;
