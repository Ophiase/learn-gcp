SELECT
  year,
  country,
  AVG(temp) AS avg_temp
FROM `bigquery-public-data.gsod.gsod2023`
WHERE temp IS NOT NULL
GROUP BY year, country
ORDER BY year, avg_temp DESC
