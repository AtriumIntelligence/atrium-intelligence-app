import requests
import streamlit as st

def send_to_webhook(first, last, phone, email, comment):
    url = st.secrets["webhook"]["url"]

    payload = {
        "first_name": first,
        "last_name": last,
        "phone": phone,
        "email": email,
        "comment": comment
    }

    try:
        requests.post(url, json=payload, timeout=5)
        return True
    except Exception:
        return False