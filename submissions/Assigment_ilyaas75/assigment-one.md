# Practical Assignment: Data Foundations for Machine Learning

## Title

**Analysis of Factors Influencing Annual Salaries in the Technology Sector**

---

## 1. Dataset Description & Collection Method

This study analyzes professional salary trends in the technology sector by examining how job-related factors influence annual income. The dataset was **manually collected** by logging information from **54 active job postings** published on professional job platforms such as **LinkedIn** and **Indeed**, as well as selected local company career pages.

Each job posting was reviewed individually, and relevant attributes such as experience requirements, education level, work arrangement, and listed salary were recorded in a spreadsheet. When salaries were presented as ranges, the midpoint value was used. Hourly wages were converted into annual salaries using a standard full-time assumption (40 hours/week, 52 weeks/year).

This dataset was created specifically for this assignment and was not sourced from any pre-existing public datasets.

---

## 2. Description of Features (X) and Label (y)

To support effective machine learning analysis, the following variables were collected:

### Input Features (X)

| Feature Name             | Type        | Description                                                          |
| ------------------------ | ----------- | -------------------------------------------------------------------- |
| Years of Experience      | Numerical   | Total years of relevant professional experience required for the job |
| Education Level          | Categorical | Highest degree required (High School, Bachelor’s, Master’s, PhD)     |
| Remote Status            | Categorical | Work arrangement: Remote, Hybrid, or On-site                         |
| Company Size             | Categorical | Organization size: Small (<50), Medium (50–500), Large (500+)        |
| Programming Skills Count | Numerical   | Number of technical keywords mentioned (e.g., Python, Java, SQL)     |

### Output Variable (Label y)

* **Annual Salary (USD)** – Target variable representing total yearly compensation. If a range was provided, the midpoint value was recorded.

This structure makes the dataset well-suited for **supervised learning**, particularly regression.

---

## 3. Dataset Structure

* **Total Rows (Samples):** 54
* **Total Columns:** 6 (5 features + 1 label)

### Sample Data Table (5 Rows)

| Experience (Years) | Education  | Remote  | Company Size | Tech Count | Salary (USD) |
| -----------------: | ---------- | ------- | ------------ | ---------- | ------------ |
|                  3 | Bachelor’s | Remote  | Medium       | 4          | 85,000       |
|                  0 | Bachelor’s | On-site | Large        | 2          | 55,000       |
|                  7 | Master’s   | Hybrid  | Small        | 5          | 110,000      |
|                  5 | ?          | Remote  | Medium       | 3          | 95,000       |
|                 10 | PhD        | Remote  | Large        | 6          | 165,000      |

---

## 4. Data Quality Issues (Real-World Messiness)

Because the dataset was collected from real job postings, several common data quality issues were identified:

* **Missing Values:** Approximately 15% of job listings did not explicitly state the required education level.
* **Formatting Inconsistencies:** Some salaries were listed as hourly wages (e.g., "$50/hour") and required conversion to annual figures.
* **Salary Ranges:** Most postings provided salary ranges (e.g., "$80,000 – $100,000"). Using the midpoint introduces approximation noise.
* **Textual Inconsistencies:** Minor typos and variations such as "Bachlor" vs. "Bachelor’s" were observed in manual entries.
* **Subjectivity in Skill Count:** The number of programming skills depends on how explicitly employers list technologies.

These imperfections reflect realistic industry data and provide valuable material for data preprocessing in later lessons.

---

## 5. Machine Learning Use Case

### Primary Use Case: Regression

* **Goal:** Predict the exact annual salary of a job posting based on experience, education, company size, and technical requirements.

### Alternative Use Case: Classification

* Salaries can be converted into categories such as:

  * **High Pay:** Greater than $100,000
  * **Standard Pay:** $100,000 or less

This enables a binary classification task useful for job market analysis.

### Additional Analysis

* Feature importance analysis to determine which factors most strongly influence salary.
* Trend analysis of remote vs. on-site compensation.

---

## 6. Conclusion

This assignment provided practical experience in collecting and documenting a real-world dataset suitable for machine learning. By manually gathering salary information from live job postings, the dataset captures realistic challenges such as missing values, inconsistent formats, and approximation errors. In future lessons, this dataset will be cleaned, encoded, and scaled to build predictive machine learning models, bridging the gap between theory and real-world data practice.
