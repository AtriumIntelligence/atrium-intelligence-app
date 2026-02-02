import streamlit as st

def show_sidebar_nav():
    st.sidebar.markdown("<h2 style='color:#005f73;'>Atrium Navigation</h2>", unsafe_allow_html=True)

    st.sidebar.markdown("""
    <ul style='list-style-type:none; padding-left:0; font-size:16px;'>
        <li><a href='/' style='text-decoration:none;'>🏠 Homepage</a></li>
        <li><a href='/services/Streamlit_Sites' style='text-decoration:none;'>📊 Streamlit-Powered Websites</a></li>
        <li><a href='/services/AI_Automation' style='text-decoration:none;'>🤖 AI & Automation</a></li>
        <li><a href='/services/Analytics_ML' style='text-decoration:none;'>📈 Analytics & Machine Learning</a></li>
        <li><a href='/2_Projects' style='text-decoration:none;'>🧪 Projects</a></li>
        <li><a href='/3_About' style='text-decoration:none;'>👤 About</a></li>
        <li><a href='/4_Contact' style='text-decoration:none;'>📬 Contact</a></li>
    </ul>
    """, unsafe_allow_html=True)