print("==========================================")
print("     BURR HEIGHT PREDICTION SYSTEM")
print("==========================================")

from src.clean_data import clean_dataset
from src.preprocess import preprocess_data

# step 1
clean_dataset()

# step 2
preprocess_data()
    