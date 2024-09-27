# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Generate mock sensor data (or replace with actual sensor data)
# Sensor data includes parameters like pH, Turbidity, Conductivity, Temperature, etc.
data = {
    'pH': np.random.uniform(6.5, 8.5, 1000),  # pH levels of water
    'Turbidity': np.random.uniform(1, 5, 1000),  # Turbidity in NTU
    'Conductivity': np.random.uniform(50, 500, 1000),  # Conductivity in µS/cm
    'Temperature': np.random.uniform(5, 30, 1000),  # Temperature in Celsius
    'Water_Quality': np.random.choice([0, 1], 1000)  # 0 = Poor, 1 = Good water quality
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Define features (input parameters) and target (water quality)
X = df[['pH', 'Turbidity', 'Conductivity', 'Temperature']]
y = df['Water_Quality']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the RandomForestClassifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Example: Predict water quality for new sensor data
new_data = np.array([[7.0, 3.0, 200, 15]])  # New sensor readings: [pH, Turbidity, Conductivity, Temperature]
prediction = model.predict(new_data)
print("Predicted Water Quality (0 = Poor, 1 = Good):", prediction[0])

# (Optional) Visualize feature importance
importances = model.feature_importances_
features = X.columns
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 5))
plt.title("Feature Importance for Water Quality Prediction")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), [features[i] for i in indices])
plt.tight_layout()
plt.show()

