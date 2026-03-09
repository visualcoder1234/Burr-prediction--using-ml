import pandas as pd

def preprocess_data():

    print("\nStep 2: Preprocessing dataset")

    df = pd.read_csv("data/cleaned_dataset.csv")

    print("Dataset loaded for preprocessing")

    return df