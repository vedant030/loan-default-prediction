import pandas as pd

def clean_data():
    df = pd.read_csv("data/processed/ingested.csv")

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing values
    df.fillna(df.median(numeric_only=True), inplace=True)

    print("[CLEANING] Data cleaned.")
    df.to_csv("data/processed/cleaned.csv", index=False)

if __name__ == "__main__":
    clean_data()
