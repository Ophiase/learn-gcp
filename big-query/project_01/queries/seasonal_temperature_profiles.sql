SELECT
  month,
  AVG(mean_temp) avg_temp,
  APPROX_QUANTILES(mean_temp, 4)[OFFSET(1)] q25,
  APPROX_QUANTILES(mean_temp, 4)[OFFSET(2)] median,
  APPROX_QUANTILES(mean_temp, 4)[OFFSET(3)] q75
FROM `bigquery-public-data.samples.gsod`
WHERE mean_temp IS NOT NULL
GROUP BY month
ORDER BY month;
