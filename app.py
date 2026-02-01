import streamlit as st
import pandas as pd
import os

st.title("Atrium Intelligence – Connecticut Labor Dashboard")

csv_path = "data/CT_Labor_Stats_December2025.csv"

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    st.write("Preview of the dataset:")
    st.dataframe(df.head())
else:
    st.error(f"CSV file not found at: {csv_path}")
