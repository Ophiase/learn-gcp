SELECT
  year,
  COUNTIF (fog) fog_days,
  COUNTIF (rain) rain_days,
  COUNTIF (snow) snow_days,
  COUNTIF (thunder) thunder_days
FROM
  `bigquery-public-data.samples.gsod`
  -- WHERE year >= 2000 
  -- could reduce cost if partioned (not the case here)
GROUP BY
  year
ORDER BY
  year;