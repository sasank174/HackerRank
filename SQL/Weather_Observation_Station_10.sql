-- Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.

-- Input Format

-- The STATION table is described as follows:

/*
Enter your query here.
*/
SELECT DISTINCT city
FROM station
WHERE (
   LOWER(city) not LIKE '%a' 
   AND LOWER(city) not LIKE '%e' 
   AND LOWER(city) not LIKE '%i' 
   AND LOWER(city) not LIKE '%o' 
   AND LOWER(city) not LIKE '%u'
);