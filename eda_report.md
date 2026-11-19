# Artificial Intellegience and Algorithmic Bias: EDA 

**Author:** Ekram Milash
**Course:** CSE163
**Date:** November 2026

**My Github:** https://github.com/ekrammi/cse163-compas-ai 

## Summary of Findings and Research Questions

In this project, i look through the COMPAS file to investigate differences in AI risk assessments in different groups of people across different age groups.

My research questions are:

1.Do different types of machine learning models have different types of errors across racial groups?

2. How does AI risk score differently across different groups?

3.Does someone’s age affect the accuracy of AI risk prediction?

Mainly this project uses teh COMPAS risk assessment, which is able then to estimate recidivism.

## 3. Datasets

This projects uses multiple datasets but the most important one is the COMPASS recidivism dataset 
- Contains over 7000 rows and around 53 columns

variable included are:
- 'age'
- 'race'
- 'sex'
- 'decile_score'
- two_year_recid'

It also includes other variables but this are the most important ones we are looking at.

## 4. Method
The dataset uses pandas, matplotlub, Seaborn to analyze the data. the Analysis assess missing values, examines numerical values and summarizes it, main difference in recidivism and more.

Moreover, the analuses uses visulaizations to identify common patterns in order to assess different risk scores and understand the potential recidivsim across race, and age groups.

## 5. EDA Results

Age
- Mean: 34.82
- standard deviation: 11.89
- minimum: 18
- Q1: 25
- Median: 31
- Q3: 42
- Maximum: 96

Two Year Recidivism
- Mean: 0.45
- standard deviation: 0.50
- minimum: 0
- Q1: 0
- Median: 0
- Q3: 1
- Maximum: 1

Decile Score
- Mean: 4.51
- standard deviation: 2.86
- minimum: 1
- Q1: 2
- Median: 4
- Q3: 7
- Maximum: 10

Racial Groups included:
- African Americans: 3696
- Hispanics: 637
- White: 2454
- Asians: 32
- Native Americans: 18
- others: 377

Age sections has around 1529 under 25, 1576 over 45 and 4109 between 25 - 45
Risk section has 3897 Low, 1914 medium and 1403 High.

## Data Visulizations: Risk Score  by race
![COMPAS risk scores by race](visualizations/risk_scores_by_race.png)

## Data Visulizations: Recidivism across race
![Two-year recidivism rates by race](visualizations/recidivism_by_race.png)

## Data Visulizations: Recidivism by age
![Two-year recidivism rates by age](visualizations/recidivism_by_age.png)
