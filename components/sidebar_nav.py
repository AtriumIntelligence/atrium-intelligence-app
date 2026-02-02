import streamlit as st

def show_sidebar_nav():
    st.sidebar.markdown("## Atrium Navigation")

    st.sidebar.page_link("app.py", label="🏠 Homepage")

    st.sidebar.markdown("### Services")
    st.sidebar.page_link("pages/services/Streamlit_Sites.py", label="📊 Streamlit-Powered Websites")
    st.sidebar.page_link("pages/services/AI_Automation.py", label="🤖 AI & Automation")
    st.sidebar.page_link("pages/services/Analytics_ML.py", label="📈 Analytics & Machine Learning")

    st.sidebar.markdown("### Other")
    st.sidebar.page_link("pages/2_Projects.py", label="🧪 Projects")
    st.sidebar.page_link("pages/3_About.py", label="👤 About")
    st.sidebar.page_link("pages/4_Contact.py", label="📬 Contact")