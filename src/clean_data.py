import pandas as pd

# Load dataset
file_path = "../data/burr_ct_dataset.xlsx"

df = pd.read_excel(file_path)

print("Dataset loaded successfully!\n")

# Show first rows
print(df.head())

print("\nOriginal Shape:", df.shape)

# Remove columns that start with 'Unnamed'
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Drop rows with many missing values
df = df.dropna(how='all')

# Reset index
df = df.reset_index(drop=True)

print("\nCleaned Shape:", df.shape)

# Save cleaned dataset
df.to_csv("../data/cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved as cleaned_dataset.csv")