# Cohort-retention-analysis
## Introduction

This project is a Cohort retention analysis,  that emphasizes the focus on tracking and analyzing customer retention over time within specific cohorts.

## Cohort Analysis using Pandas, Seaborn and Plotly

This code is designed to perform a Cohort Analysis on a dataset using Pandas, Seaborn and Plotly libraries. The Cohort Analysis allows us to analyze the behavior of groups of users who share common characteristics over time. In this code, we analyze the behavior of users who have made submissions in different months.

## Prerequisites

The code requires the following Python libraries to be installed:

    Pandas
    Seaborn
    Matplotlib
    Plotly

## Data Input

The data used for this analysis is in an Excel format and it is loaded using the Pandas read_excel function. The dataset contains the following columns:

    created_at: date of submission
    owner_id: user ID

## Cohort Analysis Steps

The Cohort Analysis is performed in the following steps:

    1- Convert the submission date to the first day of the month using a custom function get_month.
    2- Group the users by owner_id and SubMonth.
    3- Calculate the month in which each user made their first submission and create a new column called    CohortMonth.
    4- Calculate the difference in months between the first submission and subsequent submissions for each user and create a new column called CohortIndex.
    5- Group the users by CohortMonth and CohortIndex to identify the users who made submissions in the same month with the same interval.
    6- Take only the first month of each user to calculate a pivot table so that we can calculate later the recurring users.
   7- Calculate the number of users that came in each month to keep them as a base, and calculate later the percentage of recurring users.
    8- Reshape the data in the interval of 1-0 so that we can show the percentage of recurring users.
    9- Plot the results in a heatmap using Seaborn.

## Output

The output of this code is a heatmap that shows the retention rate of users who have made submissions in different months. The heatmap shows the percentage of users who continued to make submissions in subsequent months, based on the month in which they made their first submission.

## Improvements

The code has been optimized for better efficiency and readability. The improvements include:

    Using vectorized operations in place of loops and custom functions.
    Removing unnecessary code and variables.
    Renaming variables to improve readability.
    Adding comments to improve readability and understanding of the code.
    Saving the heatmap as a JPEG file for easier sharing and distribution.
