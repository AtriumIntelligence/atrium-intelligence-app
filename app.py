import streamlit as st

st.set_page_config(
    page_title="Atrium Intelligence",
    layout="wide"
)

# --- Header with logo and brand ---
col1, col2 = st.columns([1, 3])

with col1:
    st.image("assets/AtriumIntelligenceLogo.png", use_container_width=True)

with col2:
    st.title("Atrium Intelligence")
    st.subheader("Data, AI, and Analytics for Real-World Decisions")

st.markdown("---")

# --- About Section ---
st.header("About Atrium Intelligence")

st.markdown("""
Atrium Intelligence is a data and AI consultancy focused on turning messy, real-world data 
into clear, actionable insight.

I help organizations:
- Build interactive, data-driven websites and dashboards  
- Apply AI to automate workflows and enhance decision-making  
- Run analytics and advanced machine learning to solve real business problems  

Everything I build is designed to be **practical, transparent, and immediately useful**.
""")

st.markdown("---")

# --- What I Do ---
st.header("What I Do")

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.subheader("Streamlit-Powered Websites")
    st.markdown("""
    I build custom, interactive sites using Streamlit that act as:
    - Live dashboards  
    - Internal tools  
    - Public-facing data products  
    """)

with col_b:
    st.subheader("AI & Automation")
    st.markdown("""
    I help companies apply AI to:
    - Automate workflows  
    - Summarize and interpret data  
    - Build intelligent assistants  
    """)

with col_c:
    st.subheader("Analytics & Machine Learning")
    st.markdown("""
    From descriptive analytics to advanced ML, I:
    - Explore and clean data  
    - Build predictive models  
    - Deliver clear, decision-ready outputs  
    """)

st.markdown("---")

# --- Projects Teaser ---
st.header("Check It Out")

st.markdown("""
Explore live projects built on real data to see exactly how Atrium Intelligence works in practice.

For example:
- **Connecticut Labor Market Dashboard** – interactive exploration of employment trends using public labor statistics.

Use the navigation sidebar to explore **Services** and **Projects** pages.
""")
