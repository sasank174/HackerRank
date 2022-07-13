-- Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than . Round your answer to  decimal places.

-- Input Format

-- The STATION table is described as follows:

-- Station.jpg

-- where LAT_N is the northern latitude and LONG_W is the western longitude.

select round(LONG_W,4) AS test1 from 
(select LONG_W AS LONG_W from STATION where lat_n>38.7780 order by lat_n limit 1) as test2

select round(LONG_W,4) from STATION where lat_n=(select min(lat_n) from station where lat_n>38.7780);

select round(LONG_W,4) from STATION where lat_n>38.7780 order by lat_n limit 1