import pandas as pd 
from importlib.resources import files

def get_data(source : str) -> pd.DataFrame:
    csv_path = files("fmea_pra_toolkit.data")/f"{source}.csv"
    return pd.read_csv(csv_path)

def get_all_data() -> dict[str, pd.DataFrame]:
    data = {}
    for file in files("fmea_pra_toolkit.data"):
        if file.endswith(".csv"):
            source = file.stem
            df = get_data(source)
            data[source] = df
    return data