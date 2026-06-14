import streamlit as st
from utils.db import conn, cursor

st.title("🚚 Courier Agent Portal")

student_name = st.text_input("Student Name")
tracking_id = st.text_input("Tracking ID")
company = st.text_input("Courier Company")

if st.button("Register Package"):

    cursor.execute("""
    INSERT INTO packages
    (student_name, tracking_id, courier_company, status)
    VALUES(?,?,?,?)
    """,
    (
        student_name,
        tracking_id,
        company,
        "Received at Campus Center"
    ))

    conn.commit()

    st.success("Package Registered Successfully")
    import qrcode

qr = qrcode.make(tracking_id)

qr.save(f"qrcodes/{tracking_id}.png")
ALTER TABLE packages
ADD COLUMN qr_path TEXT;
cursor.execute("""
INSERT INTO packages
(student_name,tracking_id,courier_company,status,qr_path)
VALUES(?,?,?,?,?)
""",
(student_name,
 tracking_id,
 company,
 "Received",
 f"qrcodes/{tracking_id}.png"))
 import smtplib

def send_email(email, tracking_id):

    message = f"""
    Your package has arrived.

    Tracking ID:
    {tracking_id}

    Collect it from Campus Courier Center.
    """

    server = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    server.starttls()

    server.login(
        "yourmail@gmail.com",
        "app_password"
    )

    server.sendmail(
        "yourmail@gmail.com",
        email,
        message
    )

    server.quit()
    send_email(student_email, tracking_id)