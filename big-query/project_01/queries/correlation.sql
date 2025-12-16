SELECT
    CORR(mean_temp, total_precipitation) temp_precip_corr
FROM
    `bigquery-public-data.samples.gsod`
WHERE
    mean_temp IS NOT NULL
    AND total_precipitation IS NOT NULL;