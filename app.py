import streamlit as st
import pandas as pd
import altair as alt
import os

st.set_page_config(page_title="Atrium Intelligence – CT Labor Dashboard", layout="wide")

st.title("Atrium Intelligence – Connecticut Labor Dashboard")

csv_path = "data/CT_Labor_Stats_December2025.csv"

# -----------------------------
# Load dataset safely
# -----------------------------
if not os.path.exists(csv_path):
    st.error(f"CSV file not found at: {csv_path}")
    st.stop()

df = pd.read_csv(csv_path)

# -----------------------------
# Reshape data (wide → long)
# -----------------------------
month_cols = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

df_long = df.melt(
    id_vars=['YEAR','INDUSTRY TITLE '],
    value_vars=month_cols,
    var_name='MONTH',
    value_name='EMPLOYMENT'
)

month_map = {
    'JAN':1,'FEB':2,'MAR':3,'APR':4,'MAY':5,'JUN':6,
    'JUL':7,'AUG':8,'SEP':9,'OCT':10,'NOV':11,'DEC':12
}

df_long['MONTH_NUM'] = df_long['MONTH'].map(month_map)
df_long['DATE'] = pd.to_datetime(df_long['YEAR'].astype(str) + '-' + df_long['MONTH_NUM'].astype(str) + '-01')

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("Filters")

industry_list = sorted(df_long['INDUSTRY TITLE '].unique())
industry = st.sidebar.selectbox("Select Industry", industry_list)

min_year = int(df_long['YEAR'].min())
max_year = int(df_long['YEAR'].max())

year_range = st.sidebar.slider(
    "Select Year Range",
    min_year, max_year,
    (min_year, max_year)
)

# -----------------------------
# Filtered dataset
# -----------------------------
filtered = df_long[
    (df_long['INDUSTRY TITLE '] == industry) &
    (df_long['YEAR'] >= year_range[0]) &
    (df_long['YEAR'] <= year_range[1])
].sort_values("DATE")

# -----------------------------
# Main chart
# -----------------------------
st.subheader(f"Employment Trend: {industry}")

chart = (
    alt.Chart(filtered)
    .mark_line(point=True)
    .encode(
        x=alt.X("DATE:T", title="Date"),
        y=alt.Y("EMPLOYMENT:Q", title="Employment Level"),
        tooltip=["YEAR","MONTH","EMPLOYMENT"]
    )
    .properties(height=400)
)

st.altair_chart(chart, use_container_width=True)

# -----------------------------
# Data preview
# -----------------------------
with st.expander("Show raw data"):
    st.dataframe(filtered)
