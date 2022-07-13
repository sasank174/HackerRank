-- Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than . Round your answer to  decimal places.

-- Input Format

-- The STATION table is described as follows:

-- Station.jpg

-- where LAT_N is the northern latitude and LONG_W is the western longitude.


select round(LONG_W,4) FROM STATION where lat_n<137.2345 order by lat_n desc limit 1

select round(LONG_W,4) FROM STATION where lat_n = (select max(lat_n) from STATION where lat_n<137.2345)