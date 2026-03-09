import pandas as pd

def clean_dataset():

    print("\nStep 1: Cleaning dataset")

    df = pd.read_excel("data/burr_ct_dataset.xlsx")

    print("Original Shape:", df.shape)

    # remove unwanted columns
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    # remove fully empty rows
    df = df.dropna(how="all")

    print("Cleaned Shape:", df.shape)

    df.to_csv("data/cleaned_dataset.csv", index=False)

    print("Cleaned dataset saved")

    return df

