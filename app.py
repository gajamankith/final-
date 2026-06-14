import streamlit as st

st.set_page_config(
    page_title="Campus Courier Management",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Campus Courier Management System")

st.markdown("""
### Problem Solved
Students miss deliveries because they are attending classes.

This system allows:
- Courier agents to drop packages at campus center.
- Students to collect packages later.
- Administration to manage deliveries efficiently.
""")

role = st.selectbox(
    "Select User Type",
    ["Student", "Courier Agent", "Admin"]
)

if role == "Student":
    st.switch_page("pages/student.py")

elif role == "Courier Agent":
    st.switch_page("pages/delivery.py")

elif role == "Admin":
    st.switch_page("pages/admin.py")