WITH
  stats AS (
    SELECT
      year,
      AVG(mean_temp) mu,
      STDDEV (mean_temp) sigma
    FROM
      `bigquery-public-data.samples.gsod`
    WHERE
      mean_temp IS NOT NULL
    GROUP BY
      year
  )
SELECT
  g.year,
  g.station_number,
  g.mean_temp,
  (g.mean_temp - s.mu) / s.sigma z_score
FROM
  `bigquery-public-data.samples.gsod` g
  JOIN stats s USING (year)
WHERE
  ABS((g.mean_temp - s.mu) / s.sigma) > 3
ORDER BY
  z_score DESC
LIMIT
  10;