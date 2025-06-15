import pandas as pd

# Correct CSV file (actual data!)
csv_file = r"C:\Users\SANIYA SULTHANA\Final_sleep_apnea_project\uploads\data.csv"

# Load
df = pd.read_csv(csv_file)

# Drop 'date' column
if 'date' in df.columns:
    df = df.drop('date', axis=1)

# Save cleaned file
df.to_csv("uploads/sleep_data_cleaned.csv", index=False)
print("✅ Cleaned CSV saved as sleep_data_cleaned.csv")
