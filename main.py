import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load Dataset
train = pd.read_csv("train.csv")

print("First Five Rows")
print(train.head())

print("\nDataset Shape")
print(train.shape)

print("\nMissing Values")
print(train.isnull().sum())

print("\nStatistics")
print(train.describe())

# Fill Missing Values
train["Item_Weight"] = train["Item_Weight"].fillna(train["Item_Weight"].mean())
train["Outlet_Size"] = train["Outlet_Size"].fillna(train["Outlet_Size"].mode()[0])

# Visualization 1
plt.figure(figsize=(8,5))
sns.histplot(train["Item_Outlet_Sales"], bins=30)
plt.title("Distribution of Outlet Sales")
plt.show()

# Visualization 2
plt.figure(figsize=(10,5))
sns.boxplot(x="Outlet_Type", y="Item_Outlet_Sales", data=train)
plt.xticks(rotation=20)
plt.title("Sales by Outlet Type")
plt.show()

# Prepare Data
X = train.drop("Item_Outlet_Sales", axis=1)
y = train["Item_Outlet_Sales"]

categorical = X.select_dtypes(include=["object"]).columns
numeric = X.select_dtypes(exclude=["object"]).columns

numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="mean"))
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numeric),
    ("cat", categorical_transformer, categorical)
])

model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ))
])

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

print("\nSample Predictions")
print(prediction[:10])

# Evaluation
mae = mean_absolute_error(y_test, prediction)
r2 = r2_score(y_test, prediction)

print("\nMean Absolute Error :", mae)
print("R2 Score :", r2)

# Feature Importance (Top 10)
feature_names = model.named_steps["preprocessor"].get_feature_names_out()
importances = model.named_steps["regressor"].feature_importances_

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importances
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 10 Important Features")
print(importance_df.head(10))