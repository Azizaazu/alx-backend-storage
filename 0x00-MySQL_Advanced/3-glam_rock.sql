-- List bands with Glam rock as their main style, ranked by longevity
SELECT band_name,
       (IFNULL(SPLIT_PART(lifespan, '-', 2), 2022) - SPLIT_PART(lifespan, '-', 1)) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
