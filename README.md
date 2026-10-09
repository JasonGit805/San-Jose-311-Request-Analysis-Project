## Purpose
This project explores 10 years of 311 request data for the city of San Jose. The goal was to identify patterns in request volume, common request types, and the geographic distribution of requests using SQL and Power BI.

## Tools & Technologies
Python - Consolidated 10 different CSV files into one dataset
PostgreSQL - Cleaned, transformed, and formatted the data for analysis
Power BI - Created visualizations to identify trends in request volume, request types, and locations.

## Data Source
https://data.sanjoseca.gov/dataset/311-service-request-data

## Data Processing
Consolidated 10 separate data files into one CSV using Python.
Imported the data into PostgreSQL.
Removed rows with mostly null values.
Separated date and time into individual columns to support further analysis.

## Analysis
Request Volume by Day: Identifies which days have the highest number of requests.
Most Common Request Types: Highlights the types of service requests reported most frequently.
Geographic Distribution: Uses a heat map to visualize where requests are concentrated across San Jose.

## Dashboard
<img width="1163" height="652" alt="image" src="https://github.com/user-attachments/assets/60c4dfea-720d-416a-ba93-555ddc28f666" />

## Key Findings
Finding: I found that the most common day of the week for 311 service requests was Monday, followed by Tuesday.
Recommendation: Consider allocating additional staffing or request-processing resources more toward the beginning of the week.

Finding: The most common service request type was junk pickup.
Recommendation: Shift staffing decisions to focus more on workers with commercial driver’s licenses or experience operating vehicles suited for large-item and bulk-junk removal.

Finding: Request locations were concentrated in downtown San Jose, with a relatively sparse cluster around some hotels and corporate buildings.
Recommendation: Consider whether service needs and resource allocation differ between residential and commercial areas, taking into account factors such as population density and request frequency.

## Project Structure
/data --- The 10 years of data, the combined data file, and the Power BI file are all included here. Note that the Power BI file will be the only one present on GitHub due to my .gitignore file excluding CSVs
from being uploaded.

/scripts --- Python script used to consolidate CSV files

## Future Improvements
In the future, I will compare this data with other datasets to identify additional patterns. For example, does the type of weather affect the number of 311 requests we get on a given day?
