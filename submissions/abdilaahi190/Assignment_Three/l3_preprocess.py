import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# --- 1. Load & Inspect ---
print("--- Step 1: Loading Data ---")
df = pd.read_csv('../../../dataset/car_l3_dataset.csv')

print("First 10 rows:")
print(df.head(10))

print("\nData Info:")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nLocation counts:")
print(df['Location'].value_counts())

# --- 2. Clean Price ---
print("\n--- Step 2: Cleaning Price ---")
# Remove $ and commas so we can turn Price into a number
df['Price'] = df['Price'].replace(r'[\$,]', '', regex=True).astype(float)
print(f"Price is now a: {df['Price'].dtype}")

# --- 3. Fix Location Errors ---
print("\n--- Step 3: Fixing Location Typos ---")
# Fix 'Subrb' typo and turn '??' into actual missing values
df['Location'] = df['Location'].replace({'Subrb': 'Suburb', '??': np.nan})
print("Cleaned Location counts:")
print(df['Location'].value_counts(dropna=False))

# --- 4. Fill Missing Values (Imputation) ---
print("\n--- Step 4: Filling Missing Values ---")
# Fill Odometer with the middle value (median)
df['Odometer_km'] = df['Odometer_km'].fillna(df['Odometer_km'].median())

# Fill Doors, Accidents, and Location with the most common value (mode)
df['Doors'] = df['Doors'].fillna(df['Doors'].mode()[0])
df['Accidents'] = df['Accidents'].fillna(df['Accidents'].mode()[0])
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])

print("Missing values after filling:")
print(df.isnull().sum())

# --- 5. Remove Duplicates ---
print("\n--- Step 5: Removing Duplicates ---")
print(f"Rows before: {len(df)}")
df = df.drop_duplicates()
print(f"Rows after: {len(df)}")

# --- 6. Handle Outliers (IQR Capping) ---
print("\n--- Step 6: Handling Outliers ---")
# For Price
Q1_p = df['Price'].quantile(0.25)
Q3_p = df['Price'].quantile(0.75)
IQR_p = Q3_p - Q1_p
lower_p = Q1_p - 1.5 * IQR_p
upper_p = Q3_p + 1.5 * IQR_p
df['Price'] = df['Price'].clip(lower_p, upper_p)

# For Odometer
Q1_o = df['Odometer_km'].quantile(0.25)
Q3_o = df['Odometer_km'].quantile(0.75)
IQR_o = Q3_o - Q1_o
lower_o = Q1_o - 1.5 * IQR_o
upper_o = Q3_o + 1.5 * IQR_o
df['Odometer_km'] = df['Odometer_km'].clip(lower_o, upper_o)
print("Outliers have been capped.")

# --- 7. One-Hot Encoding ---
print("\n--- Step 7: Encoding Location ---")
# Turn Location into 0s and 1s
df = pd.get_dummies(df, columns=['Location'], prefix='Loc', dtype=int)
print("New columns:", df.columns.tolist())

# --- 8. Feature Engineering ---
print("\n--- Step 8: Creating New Features ---")
# Feature 1: Car Age
df['CarAge'] = 2026 - df['Year']

# Feature 2: Is the car new? (less than 5 years old)
df['IsNew'] = (df['CarAge'] < 5).astype(int)

# Feature 3: Driven high or low?
avg_km = df['Odometer_km'].mean()
df['HighUsage'] = (df['Odometer_km'] > avg_km).astype(int)

# Special target: Log of Price
df['LogPrice'] = np.log1p(df['Price'])
print("Features created: CarAge, IsNew, HighUsage, LogPrice")

# --- 9. Feature Scaling ---
print("\n--- Step 9: Scaling Features ---")
# We scale only the continuous numbers, not the targets or 0/1 columns
cols_to_scale = ['Odometer_km', 'Doors', 'Accidents', 'Year', 'CarAge']
scaler = StandardScaler()
df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
print("Scaling finished.")

# --- 10. Final Checks & Save ---
print("\n--- Step 10: Final Check & Saving ---")
print(df.describe())
df.to_csv('car_l3_clean_ready.csv', index=False)
print("All done! Saved to car_l3_clean_ready.csv")
