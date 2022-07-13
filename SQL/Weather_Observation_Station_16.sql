-- Query the smallest Northern Latitude (LAT_N) from STATION that is greater than . Round your answer to  decimal places.

-- Input Format

-- The STATION table is described as follows:

-- Station.jpg

-- where LAT_N is the northern latitude and LONG_W is the western longitude.


select round(lat_n,4) FROM STATION where lat_n>38.7780 order by lat_n asc limit 1

select round(min(lat_n),4) from STATION where lat_n>38.7780