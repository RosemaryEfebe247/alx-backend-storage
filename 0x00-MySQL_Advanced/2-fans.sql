-- Rank country origins of bands by the number of fans
SELECT origin, SUM(nb_fans) AS total_fans
FROM meta_bands
GROUP BY origin
ORDER BY total_fans DESC;
