Student Study Habits and Academic Performance Dataset
Overview

This project presents a self-collected educational dataset created to support learning in Machine Learning, Data Analysis, and Data Preprocessing.

The dataset investigates how students’ daily study habits, sleep behavior, social media usage, and class attendance influence their academic exam performance.

Data was gathered through a manual survey questionnaire distributed to real students.
To reflect real-world data science conditions, the dataset intentionally contains:

Missing values

Small typing inconsistencies

Possible outliers

Slight class imbalance

This makes it highly suitable for practical Machine Learning training rather than perfectly clean theoretical data.

Dataset Summary

Total Samples: 60 students

Input Features (X): 6 variables

Target Label (y): Exam Score

Data Types: Mixed (Numerical + Categorical)

Collection Method: Manual survey → Spreadsheet entry

Purpose: Educational Machine Learning practice

Features Description
Feature	Type	Description
Age	Numeric	Student age in years
Gender	Categorical	Male or Female
Study_Hours_Per_Day	Numeric	Average daily study duration
Sleep_Hours	Numeric	Average nightly sleep time
Social_Media_Hours	Numeric	Daily time spent on social media
Attendance_Percentage	Numeric	Percentage of attended classes
Exam_Score (Label)	Numeric	Latest exam result out of 100
Data Quality Notes

Because the dataset originates from real student responses, it includes realistic imperfections:

Missing entries in sleep or social media fields

Typographical mistakes in attendance or score formatting

Potential outliers (e.g., extremely high study hours)

Slight gender distribution imbalance

These characteristics make the dataset valuable for practicing:

Data cleaning

Handling missing values

Outlier detection

Feature engineering

Data validation

Possible Machine Learning Tasks
1. Regression

Predict the numerical exam score using:

Linear Regression

Decision Tree Regressor

Random Forest Regressor

2. Classification

Transform exam scores into categories such as:

Fail

Pass

Good

Excellent

Then apply:

Logistic Regression

K-Nearest Neighbors (KNN)

Decision Tree Classifier

3. Clustering

Discover hidden student behavior patterns using:

K-Means Clustering

Project Learning Objectives

This dataset is designed to help learners practice:

Real-world data collection techniques

Clear data documentation

Managing imperfect and inconsistent data

Preparing datasets for Machine Learning modeling

Understanding the full ML workflow from raw data to prediction

Recommended Workflow (Next Steps)

Data cleaning and preprocessing

Handling missing values and outliers

Encoding categorical variables

Feature scaling and normalization

Train–test data splitting

Model training and comparison

Performance evaluation using metrics such as:

MAE / MSE (Regression)

Accuracy / F1-Score (Classification)

Ethical & Educational Use

This dataset does not contain sensitive personal identifiers.

It is intended only for learning, research practice, and academic assignments.

Results derived from this dataset should not be used for real academic decision-making.

Author Information

Student Name: Fill in your name
Course: Data Foundations for Machine Learning
Institution: Fill in your school or university
Academic Year: 2026

License

This dataset is released for educational and non-commercial use only.
You are free to use, modify, and share it for learning purposes with proper attribution.