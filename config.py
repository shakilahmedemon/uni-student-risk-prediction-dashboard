# ======================================================
# GLOBAL CONFIG
# ======================================================
import streamlit as st

# --- DATA FOR STATS ---
TOTAL_STUDENTS = 2500
HIGH_RISK_RATE = 0.12
AT_RISK_STUDENTS = int(TOTAL_STUDENTS * HIGH_RISK_RATE)
ON_TRACK_STUDENTS = TOTAL_STUDENTS - AT_RISK_STUDENTS
PREDICTION_ACCURACY = 97

# --- PAGE CONFIG ---
def set_page_config():
    st.set_page_config(
        page_title="Yangzhou University Students Proactive Risk Predictor",
        page_icon="🎓",
        layout="wide",
    )

# --- SESSION STATE INITIALIZATION ---
def init_session_state():
    if 'prediction_history' not in st.session_state:
        st.session_state.prediction_history = []
    if 'page' not in st.session_state:
        st.session_state.page = "Home"
    if 'theme' not in st.session_state:
        st.session_state.theme = "Light"  # Default theme
    if 'background_url' not in st.session_state:
        # Default URL that works well
        st.session_state.background_url = 'https://wallpapers.com/images/hd/professional-background-2b3p57557lfg0y5g.jpg'
    if 'language' not in st.session_state:
        st.session_state.language = "English"
    if 'failed_login_attempts' not in st.session_state:
        st.session_state.failed_login_attempts = 0
    if 'account_locked_until' not in st.session_state:
        st.session_state.account_locked_until = None
    if 'last_login_info' not in st.session_state:
        st.session_state.last_login_info = {
            'timestamp': 'Never',
            'device': 'Web Browser',
            'location': 'Unknown'
        }
    if 'registered_users' not in st.session_state:
        st.session_state.registered_users = {
            'teacher': 'yangzhou123'
        }
    if 'remembered_credentials' not in st.session_state:
        st.session_state.remembered_credentials = {'username': '', 'password': ''}
    if 'carousel_index' not in st.session_state:
        st.session_state.carousel_index = 0
    if 'carousel_auto_rotate' not in st.session_state:
        st.session_state.carousel_auto_rotate = True
    if 'teacher_info' not in st.session_state:
        st.session_state.teacher_info = {
            'full_name': 'Teacher',
            'email': 'teacher@yangzhou.edu',
            'department': 'Academic Affairs',
            'phone': '+86-514-8730-8888'
        }
