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
        import random

otp = random.randint(100000,999999)
st.session_state["otp"] = otp
user_otp = st.text_input("Enter OTP")

if st.button("Verify"):

    if user_otp == str(st.session_state["otp"]):
        st.success("Verified")

    else:
        st.error("Wrong OTP")