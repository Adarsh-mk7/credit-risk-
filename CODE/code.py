# Credit Risk Assessment and Decision Support System with Python and Power BI

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load the dataset
df = pd.read_csv("data.csv")

# -------------------------------
# Step 1: Data Understanding
# -------------------------------
print("First 5 rows of dataset:\n", df.head())
print("\nMissing Values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)
print("\nShape of Data:", df.shape)

# -------------------------------
# Step 2: Data Preprocessing
# -------------------------------
# Fill missing values (if any)
df.fillna(method='ffill', inplace=True)

# Encode categorical variables
label_encoders = {}
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# -------------------------------
# Step 3: Feature Selection
# -------------------------------

# Correlation Matrix
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# Define Features and Target
target = 'Risk_Flag' if 'Risk_Flag' in df.columns else df.columns[-1]
X = df.drop(target, axis=1)
y = df[target]

# -------------------------------
# Step 4: Model Building
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -------------------------------
# Step 5: Evaluation
# -------------------------------

y_pred = model.predict(X_test)

print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# -------------------------------
# Step 6: Export for Power BI
# -------------------------------

results_df = X_test.copy()
results_df["Actual_Risk"] = y_test.values
results_df["Predicted_Risk"] = y_pred
results_df.to_csv("credit_risk_results.csv", index=False)
print("\n✅ Exported 'credit_risk_results.csv' for Power BI dashboard.")
 # type: ignore