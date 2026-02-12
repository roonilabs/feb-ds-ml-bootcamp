Analysis of Factors Influencing Annual Salaries in the Technology Sector
Practical Assignment – Data Foundations for Machine Learning
Overview

This project presents a manually collected dataset designed to analyze how job-related characteristics influence annual salaries in the technology sector.

Data was gathered from 54 real job postings published on professional platforms such as:

LinkedIn

Indeed

Local company career pages

Each listing was reviewed individually, and important attributes—such as experience requirements, education level, remote status, company size, technical skill demand, and salary—were recorded in a structured spreadsheet.

To standardize the dataset:

Salary ranges were converted to a midpoint annual value.

Hourly wages were transformed into annual salaries assuming 40 hours/week and 52 weeks/year.

This dataset was created specifically for academic learning and not taken from any public dataset repository.

Dataset Summary

Total Samples: 54 job postings

Input Features (X): 5 variables

Target Label (y): Annual Salary (USD)

Data Types: Mixed (Numerical + Categorical)

Collection Method: Manual review and spreadsheet entry

Purpose: Educational Machine Learning analysis

Feature Description
Feature	Type	Description
Years of Experience	Numerical	Required professional experience in years
Education Level	Categorical	Highest required degree (High School, Bachelor’s, Master’s, PhD)
Remote Status	Categorical	Work arrangement: Remote, Hybrid, On-site
Company Size	Categorical	Small (<50), Medium (50–500), Large (500+)
Programming Skills Count	Numerical	Number of technical skills listed in the job post
Annual Salary (Label)	Numerical	Total yearly compensation in USD
Data Quality Considerations

Because the dataset originates from real-world job advertisements, it contains realistic imperfections:

Missing values in education requirements (~15% of postings)

Inconsistent salary formats (hourly vs. yearly)

Salary ranges requiring midpoint estimation

Manual entry typos and wording variations

Subjective counting of technical skills

These characteristics make the dataset valuable for practicing:

Data cleaning

Missing value handling

Feature engineering

Data preprocessing for Machine Learning

Machine Learning Applications
1. Regression (Primary Task)

Goal: Predict the exact annual salary using:

Years of experience

Education level

Remote status

Company size

Technical skill demand

Possible algorithms:

Linear Regression

Decision Tree Regressor

Random Forest Regressor

2. Classification (Alternative Task)

Convert salaries into categories:

High Pay: Salary > $100,000

Standard Pay: Salary ≤ $100,000

This enables:

Logistic Regression

K-Nearest Neighbors (KNN)

Decision Tree Classifier

3. Additional Analysis

Feature importance to identify strongest salary predictors

Remote vs. on-site salary comparison

Exploratory data visualization for industry insights

Learning Objectives

This project helps learners practice:

Real-world data collection

Proper dataset documentation

Handling messy and inconsistent data

Preparing data for Machine Learning modeling

Understanding the complete ML workflow

Next Steps

Planned future work includes:

Data cleaning and preprocessing

Handling missing values and outliers

Encoding categorical variables

Feature scaling and normalization

Train–test split

Model training and evaluation using:

MAE / MSE for regression

Accuracy / F1-Score for classification

Author

Student Name: Your Name Here
Course: Data Foundations for Machine Learning
Institution: Your School or University
Academic Year: 2026

License

This dataset is provided for educational and non-commercial use only.
It may be freely used, modified, and shared for learning and academic purposes with proper attribution.