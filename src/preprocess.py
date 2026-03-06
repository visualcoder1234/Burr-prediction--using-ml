import pandas as pd

print("Dataset loaded for preprocessing")

df = pd.read_csv("../data/cleaned_dataset.csv")

# Remove spaces in column names
df.columns = df.columns.str.strip()

print(df.columns)

# Convert drill type to numbers
df['D'] = df['D'].astype('category').cat.codes

# Features
X = df[['SS','FR','DD','D']]

# Targets (all materials)
y = df[['AL','SiC','Neat']]

print("Features:")
print(X.head())

print("Targets:")
print(y.head())

print("Preprocessing complete")
