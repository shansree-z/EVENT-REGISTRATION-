import streamlit as st
import requests

# 1. UI & THEME (Hiding GitHub chrome for a clean look)
st.set_page_config(page_title="ShanEventz", layout="centered")

st.markdown("""
    <style>
    header, footer, #MainMenu, #GithubIcon {visibility: hidden;}
    .stApp { background: linear-gradient(135deg, #000000 0%, #8b0000 100%); color: white; }
    [data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid #ff4b4b;
        padding: 25px;
    }
    label { color: #ff4b4b !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("ShanEventz Registration")

# Submission endpoint
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc88KKudFh42JScl6jNf_mchbespeaIChDLrv7OSmMfYmx1uA/formResponse"

with st.form("registration_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        fname = st.text_input("First Name")
        lname = st.text_input("Last Name")
        age = st.number_input("Age", 1, 100)
    with col2:
        email = st.text_input("Email ID")
        phone = st.text_input("Phone Number")
        dob = st.date_input("Date of Birth")

    st.write("### Choose Your Tracks")
    tech = st.multiselect("Technical", ["Coding War", "Ai Hackathon", "Web Design", "Robot Race", "Data Quiz"])
    non_tech = st.multiselect("Non-Technical", ["Photography", "Gaming (BGMI)", "Standup Comedy", "Treasure Hunt"])

    if st.form_submit_button("REGISTER NOW"):
        if fname and email:
            # Check these IDs against your 'Inspect' results
            form_payload = {
                "entry.290432123": fname,
                "entry.37629806": lname,
                "entry.1833594203": age,
                "entry.1720808553": str(dob),
                "entry.743410951": phone,
                "entry.1526759683": email,
                "entry.1830788331": ", ".join(tech),
                "entry.1742901975": ", ".join(non_tech)
            }
            
            headers = {'Referer': FORM_URL, 'User-Agent': "Mozilla/5.0"}
            
            try:
                # We expect a 200 (Success) or 302 (Redirect to success page)
                r = requests.post(FORM_URL, data=form_payload, headers=headers, timeout=10)
                if r.status_code in [200, 302]:
                    st.success(f"🎉 Success! {fname}, your registration is recorded.")
                    st.balloons()
                else:
                    st.error(f"Error {r.status_code}: Please check 'Collect Email' is OFF in settings.")
            except Exception as e:
                st.error("Connection error. Please check your internet.")
        else:
            st.error("Please fill in the required fields.")
            
