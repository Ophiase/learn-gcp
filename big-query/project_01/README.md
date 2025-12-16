# Project 01 - Public GCP Datasets

This project demonstrates how to access and query public datasets hosted on Google Cloud Platform's BigQuery service.

## Costs

BigQuery charges per data scanned.
On-demand price: $\$5/TB$ scanned.

e.g. [`extreme_weather_frequency_by_year.sql`](queries/extreme_weather_frequency_by_year.sql)
- scans 1.28 GB of data
- 1.28 GB = 0.00128 TB
- Cost = $0.00128 TB \times \$5/TB = \$0.0064$

## Public Datasets Used

- [bigquery-public-data](https://docs.cloud.google.com/bigquery/public-data)

###  GSOD

- referenced under: `noaa_gsod`
    - a lighter version with a different schema is available under: `samples.gsod`
- schemas
    - [`schema/noaa_gsod.gsod2023.json`](schema/noaa_gsod.gsod2023.json)
    - [`schema/samples.gsod.json`](schema/samples.gsod.json)
- Global Surface Summary of the Day Weather Data
- National Oceanic and Atmospheric Administration (NOAA)
- Data:
    - 1929 $\to$ present
    - over 9000 stations worldwide

### Github Nested

- ✅ `github_nested`
        - GitHub Archive Data
        - Contains data on GitHub events, repositories, users, and more.

