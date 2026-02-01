import streamlit as st

st.set_page_config(
    page_title="Atrium Intelligence",
    layout="wide"
)

# --- Dome header image ---
st.image("assets/atrium_dome.png", use_container_width=True)

# --- Contact block ---
st.markdown("""
<div style="text-align:center; padding:20px;">
    <h1 style="font-size:48px; margin-bottom:0;">ATRIUM INTELLIGENCE</h1>
    <h3 style="margin-top:5px;">Jamison Welch – Founder</h3>
    <p style="font-size:16px;">📞 860-836-7624 &nbsp;&nbsp; ✉ atriumintelligence@outlook.com</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

# --- About section ---
st.markdown("<h2 style='color:#005f73;'>About Atrium Intelligence</h2>", unsafe_allow_html=True)

st.markdown("""
Atrium Intelligence is a data and AI consultancy focused on turning messy, real-world data 
into clear, actionable insight.

I help organizations:
- Build interactive, data-driven websites and dashboards  
- Apply AI to automate workflows and enhance decision-making  
- Run analytics and advanced machine learning to solve real business problems  

Everything I build is designed to be **practical, transparent, and immediately useful**.
""")

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

# --- What I Do section ---
st.markdown("<h2 style='color:#005f73;'>What I Do</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/streamlit_sites.png", use_container_width=True)
    st.markdown("""
    <div style='background-color:#fefae0; padding:15px; border-radius:8px;'>
        <h4 style='color:#bc6c25;'>Streamlit-Powered Websites</h4>
        <p>I build interactive, data-driven sites that act as:</p>
        <ul>
            <li>Live dashboards</li>
            <li>Internal tools</li>
            <li>Public-facing data products</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("assets/ai_automation.png", use_container_width=True)
    st.markdown("""
    <div style='background-color:#e0f7fa; padding:15px; border-radius:8px;'>
        <h4 style='color:#0077b6;'>AI & Automation</h4>
        <p>I help companies apply AI to:</p>
        <ul>
            <li>Automate workflows</li>
            <li>Summarize and interpret data</li>
            <li>Build intelligent assistants</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.image("assets/analytics_ml.png", use_container_width=True)
    st.markdown("""
    <div style='background-color:#ede7f6; padding:15px; border-radius:8px;'>
        <h4 style='color:#5e548e;'>Analytics & Machine Learning</h4>
        <p>From descriptive analytics to advanced ML, I:</p>
        <ul>
            <li>Explore and clean data</li>
            <li>Build predictive models</li>
            <li>Deliver decision-ready outputs</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

# --- Projects teaser ---
st.markdown("<h2 style='color:#005f73;'>Check It Out</h2>", unsafe_allow_html=True)

st.markdown("""
Explore live projects built on real data to see exactly how Atrium Intelligence works in practice.

For example:
- **Connecticut Labor Market Dashboard** – interactive exploration of employment trends using public labor statistics.

Use the navigation sidebar to explore **Services** and **Projects** pages.
""")