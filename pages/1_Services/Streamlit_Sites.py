import streamlit as st
from utils.webhook import send_to_webhook
from utils.storage import save_submission

from components.sidebar_nav import show_sidebar_nav
show_sidebar_nav()

st.set_page_config(page_title="Streamlit-Powered Websites", layout="wide")

# --- Header ---
st.markdown("<h1 style='color:#bc6c25;'>Streamlit‑Powered Websites</h1>", unsafe_allow_html=True)
st.image("assets/streamlit_sites.png", width=300)

st.markdown("""
<p style='color:#333333; font-size:17px;'>
Streamlit-powered websites turn your data into interactive, living tools.  
Instead of static reports or spreadsheets, you get a fast, modern web app that updates instantly, 
lets users explore information intuitively, and can be deployed securely inside or outside your organization.
</p>
""", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)


# ============================================================
#   WHO THIS IS FOR
# ============================================================

st.markdown("<h2 style='color:#333333;'>Who This Is For</h2>", unsafe_allow_html=True)

st.markdown("""
<ul style='color:#333333; font-size:16px;'>
    <li>Organizations with data trapped in spreadsheets or static reports</li>
    <li>Teams that need dashboards, tools, or calculators built quickly</li>
    <li>Leaders who want clearer visibility into operations, finance, or performance</li>
    <li>Companies that want to share data publicly in a polished, branded way</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)


# ============================================================
#   REQUIREMENTS
# ============================================================

st.markdown("<h2 style='color:#333333;'>What I Need From You</h2>", unsafe_allow_html=True)

st.markdown("""
<ul style='color:#333333; font-size:16px;'>
    <li>Access to the data source (CSV, Excel, SQL, API, etc.)</li>
    <li>A clear understanding of who will use the tool</li>
    <li>Any branding preferences (colors, logos, layout style)</li>
    <li>Optional: examples of dashboards or tools you like</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)


# ============================================================
#   PROCESS
# ============================================================

st.markdown("<h2 style='color:#333333;'>The Process</h2>", unsafe_allow_html=True)

st.markdown("""
<ol style='color:#333333; font-size:16px;'>
    <li><strong>Discovery</strong> — We define the purpose, users, and required features.</li>
    <li><strong>Data Intake</strong> — You provide the data source and any documentation.</li>
    <li><strong>Prototype</strong> — I build a working version quickly so you can react to something real.</li>
    <li><strong>Refinement</strong> — We iterate on layout, visuals, and functionality.</li>
    <li><strong>Deployment</strong> — Your site goes live with secure hosting and optional authentication.</li>
</ol>
""", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)


# ============================================================
#   DELIVERABLES
# ============================================================

st.markdown("<h2 style='color:#333333;'>Deliverables</h2>", unsafe_allow_html=True)

st.markdown("""
<ul style='color:#333333; font-size:16px;'>
    <li>A fully functional, branded Streamlit website</li>
    <li>Interactive charts, filters, and user controls</li>
    <li>Secure deployment (public or private)</li>
    <li>Documentation for ongoing use</li>
    <li>Optional: training session for your team</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)


# ============================================================
#   EXAMPLE OUTCOMES
# ============================================================

st.markdown("<h2 style='color:#333333;'>Example Outcomes</h2>", unsafe_allow_html=True)

st.markdown("""
<ul style='color:#333333; font-size:16px;'>
    <li>Real-time KPI dashboards for leadership</li>
    <li>Interactive calculators for pricing, forecasting, or planning</li>
    <li>Public-facing data portals for transparency or marketing</li>
    <li>Internal tools that replace manual spreadsheet workflows</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)


# ============================================================
#   CONSULTATION FORM
# ============================================================

st.markdown("<h2 style='color:#005f73;'>Request a Free Consultation</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#333333;'>Enter your information below and I’ll reach out with a quote and next steps.</p>", unsafe_allow_html=True)

with st.form("consultation_form"):
    col1, col2 = st.columns(2)
    with col1:
        first = st.text_input("First Name")
    with col2:
        last = st.text_input("Last Name")

    phone = st.text_input("Phone Number")
    email = st.text_input("Email Address")
    comment = st.text_area("Optional Comment")

    submitted = st.form_submit_button("Request Consultation")

    if submitted:
        if first and last and phone and email:
            save_submission(first, last, phone, email, comment)
            webhook_ok = send_to_webhook(first, last, phone, email, comment)

            if webhook_ok:
                st.success("Your request has been sent. I’ll reach out shortly.")
            else:
                st.warning("Saved locally, but the webhook did not respond.")
        else:
            st.warning("Please fill out all required fields.")