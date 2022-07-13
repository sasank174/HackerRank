-- Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than . Truncate your answer to  decimal places.

-- Input Format

-- The STATION table is described as follows:

-- Station.jpg

-- where LAT_N is the northern latitude and LONG_W is the western longitude.

select round(max(LAT_N),4) FROM STATION where lat_n<137.2345

select round(LAT_N,4) FROM STATION where lat_n<137.2345 order by lat_n desc limit 1
