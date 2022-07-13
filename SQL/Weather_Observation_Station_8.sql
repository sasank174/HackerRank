-- Query the list of CITY names from STATION which have vowels as both their first and last characters. Your result cannot contain duplicates.

-- Input Format

-- The STATION table is described as follows:

SELECT city
FROM station
WHERE (
   LOWER(city) LIKE 'a%' 
   OR LOWER(city) LIKE 'e%' 
   OR LOWER(city) LIKE 'i%' 
   OR LOWER(city) LIKE 'o%' 
   OR LOWER(city) LIKE 'u%'
)
AND (
   LOWER(city) LIKE '%a' 
   OR LOWER(city) like '%e' 
   OR LOWER(city) LIKE '%i' 
   OR LOWER(city) LIKE '%o' 
   OR LOWER(city) LIKE '%u'
);