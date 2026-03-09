print("==========================================")
print("     BURR HEIGHT PREDICTION SYSTEM")
print("==========================================")

from src.clean_data import clean_dataset
from src.preprocess import preprocess_data


clean_dataset()


preprocess_data()
    
