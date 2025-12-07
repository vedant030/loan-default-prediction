import pandas as pd
import pickle
from sklearn.metrics import classification_report

def evaluate():
    df = pd.read_csv("data/processed/features.csv")

    X = df.drop("default", axis=1)
    y = df["default"]

    with open("data/model/model.pkl", "rb") as f:
        model = pickle.load(f)

    preds = model.predict(X)
    print("[EVALUATION]\n", classification_report(y, preds))

if __name__ == "__main__":
    evaluate()
