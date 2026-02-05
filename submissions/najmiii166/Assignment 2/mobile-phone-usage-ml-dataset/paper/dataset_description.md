# Mobile Phone Usage and Battery Drain Dataset

## 1. Title and Collection Method

This dataset focuses on mobile phone usage patterns and their relationship to daily battery drain. The data was created using a simulated survey-based approach to reflect realistic smartphone usage behavior among students and young adults.

The values were manually generated based on common daily habits such as screen time, number of applications used, internet connection type, and observed battery consumption. The dataset was intentionally designed to resemble real-world data, including variability and minor imperfections, in order to support practical Machine Learning exercises.

---

## 2. Description of Features and Label

### Input Features (X):
- **Age**: Age of the phone user.
- **Phone_Type**: Type of smartphone (Android or iPhone).
- **Daily_Screen_Time_Hours**: Average daily screen usage in hours.
- **Apps_Used_Per_Day**: Number of different apps used per day.
- **Internet_Type**: Primary internet connection (WiFi or Mobile Data).
- **Battery_Drop_Per_Day (%)**: Estimated percentage of battery consumed per day.

### Output Label (y):
- **Needs_Charging_More_Than_Once**: Indicates whether the phone needs to be charged more than once per day (Yes/No).

---

## 3. Dataset Structure

- Number of rows: 50
- Number of columns: 7 (6 features and 1 label)

### Sample Data (5 rows):

| Age | Phone_Type | Screen_Time_Hours | Apps_Used | Internet_Type | Battery_Drop (%) | Needs_Charging |
|----|----|----|----|----|----|----|
| 22 | Android | 6.5 | 12 | Mobile Data | 75 | Yes |
| 28 | iPhone | 4.2 | 8 | WiFi | 55 | No |
| 19 | Android | 7.8 | 15 | Mobile Data | 82 | Yes |
| 35 | iPhone | 3.5 | 6 | WiFi | 48 | No |
| 24 | Android | 5.9 | 10 | WiFi | 68 | Yes |

---

## 4. Data Quality Issues

Several data quality challenges are present:
- Categorical variables that require encoding.
- Estimated values rather than exact measurements.
- Possible class imbalance in the target label.
- Different feature scales requiring normalization or standardization.

These issues are intentional and suitable for preprocessing exercises.

---

## 5. Machine Learning Use Cases

The dataset can be used for:
- **Classification**: Predicting whether a user needs to charge the phone more than once per day.
- **Regression**: Estimating daily battery drain or screen time.
- **Clustering**: Grouping users based on usage behavior patterns.

---

## 6. Conclusion

This dataset provides a realistic foundation for practicing data preprocessing and Machine Learning modeling. Although manually created, it follows real-world logic and fulfills all assignment requirements.
