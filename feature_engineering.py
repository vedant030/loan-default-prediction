import pandas as pd

def create_features():
    df = pd.read_csv("data/processed/cleaned.csv")

    df["debt_to_income_ratio"] = df["loan_amount"] / (df["annual_income"] + 1)
    df["credit_utilization"] = df["current_balance"] / (df["credit_limit"] + 1)

    print("[FEATURE ENGINEERING] Features created.")
    df.to_csv("data/processed/features.csv", index=False)

if __name__ == "__main__":
    create_features()
