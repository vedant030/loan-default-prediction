import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model():
    df = pd.read_csv("data/processed/features.csv")

    X = df.drop("default", axis=1)
    y = df["default"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    with open("data/model/model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("[TRAINING] Model trained and saved.")

if __name__ == "__main__":
    train_model()
