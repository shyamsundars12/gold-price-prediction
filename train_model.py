import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("Gold vs USDINR.csv")
print("Original Data:", df.shape)

# Drop rows with missing or invalid values
df = df[['USD_INR', 'Goldrate']].dropna()
df['USD_INR'] = pd.to_numeric(df['USD_INR'], errors='coerce')
df['Goldrate'] = pd.to_numeric(df['Goldrate'], errors='coerce')
df = df.dropna()
print("Cleaned Data:", df.shape)
print(df.head())

# If dataset is empty after cleaning, stop
if df.empty:
    raise ValueError("No valid data found after cleaning. Please check your CSV content.")

# Features and target
X = df[['USD_INR']]
y = df['Goldrate']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.1, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model and scaler
pickle.dump(model, open("regressor.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))

print("✅ Model and scaler saved successfully!")
