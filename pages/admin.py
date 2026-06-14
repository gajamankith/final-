import streamlit as st
import pandas as pd
from utils.db import conn

st.title("👨‍💼 Admin Dashboard")

query = """
SELECT *
FROM packages
"""

df = pd.read_sql(query, conn)

st.metric(
    "Total Packages",
    len(df)
)

st.dataframe(df)