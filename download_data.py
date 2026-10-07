import pandas as pd
from pathlib import Path

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

COLUMNS = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education_num",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital_gain",
    "capital_loss",
    "hours_per_week",
    "native_country",
    "income",
]

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

output_path = data_dir / "adult.csv"

df = pd.read_csv(
    URL,
    names=COLUMNS,
    skipinitialspace=True,
    na_values="?"
)

df.to_csv(output_path, index=False)

print(f"Dataset saved to: {output_path}")
print(f"Shape: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())