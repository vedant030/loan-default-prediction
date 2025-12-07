import streamlit as st
import pandas as pd
import pickle

st.title("Loan Default Prediction Dashboard")

with open("data/model/model.pkl", "rb") as f:
    model = pickle.load(f)

df = pd.read_csv("data/processed/features.csv")

st.subheader("Sample Data")
st.dataframe(df.head())

selected = st.selectbox("Select borrower index", df.index)

borrower = df.iloc[selected:selected+1].drop("default", axis=1)
prob = model.predict_proba(borrower)[0][1]

st.metric("Default Probability", f"{prob:.2f}")
