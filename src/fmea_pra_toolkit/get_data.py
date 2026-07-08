import pandas as pd 
from importlib.resources import files

def get_data(source : str) -> pd.DataFrame:
    csv_path = files("fmea_pra_toolkit.data")/f"{source}.csv"
    return pd.read_csv(csv_path)
