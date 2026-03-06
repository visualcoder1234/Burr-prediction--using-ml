import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import joblib

print("Loading cleaned dataset...")

# Load dataset
df = pd.read_csv("../data/cleaned_dataset.csv")

# Remove extra spaces
df.columns = df.columns.str.strip()

# Keep only required columns
df = df[['SS','FR','DD','D','AL','SiC','Neat']]

# Remove rows with missing values
df = df.dropna()

print("Dataset after cleaning:", df.shape)

# Convert drill type to numbers
df['D'] = df['D'].astype('category').cat.codes

# Features
X = df[['SS','FR','DD','D']]

# Targets
y = df[['AL','SiC','Neat']]

print("Splitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training model...")

model = MultiOutputRegressor(
    RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )
)

model.fit(X_train, y_train)

print("Model trained successfully!")

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Metrics:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)

# Save model
joblib.dump(model, "../model/burr_prediction_model.pkl")

print("\nModel saved successfully!")