-- Consider  and  to be two points on a 2D plane.

--  happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
--  happens to equal the minimum value in Western Longitude (LONG_W in STATION).
--  happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
--  happens to equal the maximum value in Western Longitude (LONG_W in STATION).
-- Query the Manhattan Distance between points  and  and round it to a scale of  decimal places.

-- Input Format

-- The STATION table is described as follows:


select round(abs(max(lat_n) - min(lat_n)) + abs(max(long_w) - min(long_w)),4) from STATION

