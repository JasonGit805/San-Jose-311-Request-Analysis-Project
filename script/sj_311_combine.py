import pandas as pd
import glob
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

files = glob.glob(
    os.path.join(BASE_DIR, "data", "311", "*.csv")
)

df = pd.concat(
    [pd.read_csv(file) for file in files],
    ignore_index=True
)

csv_path = os.path.join(BASE_DIR, "data", "sj_311_data.csv")

df.to_csv(
    csv_path,
    index=False
)

print(f"Total records: {len(df):,}")