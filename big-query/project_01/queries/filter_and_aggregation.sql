WITH
  base AS (
    SELECT
      year,
      month,
      day,
      station_number,
      wban_number,
      mean_temp,
      max_temperature,
      min_temperature,
      total_precipitation,
      snow_depth,
      fog,
      rain,
      snow,
      thunder
    FROM
      `bigquery-public-data.samples.gsod`
    WHERE
      mean_temp IS NOT NULL
  ),
  daily_metrics AS (
    SELECT
      year,
      month,
      station_number,
      AVG(mean_temp) avg_daily_temp,
      MAX(max_temperature) max_daily_temp,
      MIN(min_temperature) min_daily_temp,
      SUM(total_precipitation) total_precip,
      COUNTIF (rain) rainy_days,
      COUNTIF (snow) snowy_days,
      COUNTIF (thunder) thunder_days
    FROM
      base
    GROUP BY
      year,
      month,
      station_number
  ),
  ranked_stations AS (
    SELECT
      *,
      RANK() OVER (
        PARTITION BY
          year,
          month
        ORDER BY
          avg_daily_temp DESC
      ) temp_rank
    FROM
      daily_metrics
  )
SELECT
  year,
  month,
  station_number,
  avg_daily_temp,
  max_daily_temp,
  min_daily_temp,
  total_precip,
  rainy_days,
  snowy_days,
  thunder_days
FROM
  ranked_stations
WHERE
  temp_rank <= 5
ORDER BY
  year,
  month,
  avg_daily_temp DESC;