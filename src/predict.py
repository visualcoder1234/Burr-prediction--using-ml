import joblib
import numpy as np
from tabulate import tabulate
import pandas as pd

print("\n==========================================")
print("   BURR HEIGHT PREDICTION SYSTEM (ML)")
print("==========================================\n")


print("Loading trained model...")
model = joblib.load("../model/burr_prediction_model.pkl")
print("Model loaded successfully!\n")



ss = float(input("Enter Spindle Speed (SS): "))
fr = float(input("Enter Feed Rate (FR): "))
dd = float(input("Enter Drill Diameter (DD): "))

print("\nDrill Type Options:")
print("0 = Core")
print("1 = Step")
print("2 = Twist")

d = int(input("Enter Drill Type (0/1/2): "))


input_data = pd.DataFrame(
    [[ss, fr, dd, d]],
    columns=["SS", "FR", "DD", "D"]
)

prediction = model.predict(input_data)

al = prediction[0][0]
sic = prediction[0][1]
neat = prediction[0][2]

print("\n==========================================")
print("           PREDICTION RESULTS")
print("==========================================\n")

table = [
    ["Material", "Predicted Burr Height"],
    ["Aluminium", round(al,4)],
    ["SiC", round(sic,4)],
    ["Neat", round(neat,4)]
]

print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))



choice = input("\nDo you want to calculate percentage error? (y/n): ")

if choice.lower() == "y":

    al_actual = float(input("Enter actual Aluminium value: "))
    sic_actual = float(input("Enter actual SiC value: "))
    neat_actual = float(input("Enter actual Neat value: "))

    al_error = ((al_actual - al) / al_actual) * 100
    sic_error = ((sic_actual - sic) / sic_actual) * 100
    neat_error = ((neat_actual - neat) / neat_actual) * 100

    print("\n==========================================")
    print("           ERROR ANALYSIS")
    print("==========================================\n")

    error_table = [
        ["Material", "Actual", "Predicted", "Error (%)"],
        ["Aluminium", al_actual, round(al,4), round(al_error,2)],
        ["SiC", sic_actual, round(sic,4), round(sic_error,2)],
        ["Neat", neat_actual, round(neat,4), round(neat_error,2)]
    ]

    print(tabulate(error_table, headers="firstrow", tablefmt="fancy_grid"))

print("\nPrediction complete.")