import streamlit as st
import pandas as pd
from utils.db import conn

st.title("🎓 Student Portal")

student = st.text_input("Enter Your Name")

if st.button("Search Package"):

    query = f"""
    SELECT *
    FROM packages
    WHERE student_name='{student}'
    """

    df = pd.read_sql(query, conn)

    if len(df) > 0:
        st.dataframe(df)
    else:
        st.warning("No Packages Found")