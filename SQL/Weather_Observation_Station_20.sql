-- A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to  decimal places.

-- Input Format

-- The STATION table is described as follows:

-- Station.jpg

-- where LAT_N is the northern latitude and LONG_W is the western longitude.

select round(S.LAT_N,4) from station AS S where 
(select count(Lat_N) from station where Lat_N < S.LAT_N ) = 
(select count(Lat_N) from station where Lat_N > S.LAT_N);