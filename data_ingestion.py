import pandas as pd

def load_raw_data(path="data/raw/loan_data.csv"):
    df = pd.read_csv(path)
    print(f"[INGESTION] Loaded {df.shape[0]} rows.")
    return df

if __name__ == "__main__":
    df = load_raw_data()
    df.to_csv("data/processed/ingested.csv", index=False)
