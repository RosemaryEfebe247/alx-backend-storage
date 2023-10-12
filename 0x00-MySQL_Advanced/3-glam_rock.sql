-- List bands with Glam rock as their main style, ranked by longevity
SELECT band_name,
       (YEAR('2022') - YEAR(split)) AS lifespan
FROM metal_bands
WHERE split IS NOT NULL
   AND style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
