import streamlit as st
import pandas as pd
import time
 
# Import modules
from config import set_page_config, init_session_state
from language import TEXTS
from styles import set_styles, set_login_styles
from auth import render_login_page
from pages import (
    render_home_page, 
    render_predictions_page, 
    render_students_page, 
    render_reports_page, 
    render_settings_page
)

# Set page configuration
set_page_config()

# Initialize session state
init_session_state()

# ======================================================
# LOGIN PAGE
# ======================================================
if not st.session_state.get("authenticated", False):
    set_login_styles()
    render_login_page()
    st.stop()

# ======================================================
# MAIN APPLICATION
# ======================================================
if st.session_state.get("authenticated", True):
    # Get the current language texts for the main app
    T = TEXTS[st.session_state.language]
    
    # 1. Apply Dynamic CSS based on state
    set_styles(st.session_state.theme, st.session_state.background_url)
    
    # 2. Professional Header Section with Logo
    header_col1, header_col2 = st.columns([0.5, 5])
    with header_col1:
        st.image("assets/yangzhou_logo.png", width=80)
    with header_col2:
        st.markdown(f"""
        <div class="dashboard-header">
            <div class="header-title">{T['main_title']}</div>
            <div class="header-subtitle">{T['subtitle']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # 3. Top Controls Row (User Info, Language, Logout)
    col_spacer, col_user, col_lang, col_logout = st.columns([4, 1.5, 1, 1])
    with col_user:
        st.markdown(f"<p style='text-align: right; margin-top: 10px; font-weight: 600;'>{T['hi_teacher']}</p>", unsafe_allow_html=True)
    with col_lang:
        st.session_state.language = st.selectbox(
            "Select Language",
            ["English", "中文"],
            key="dashboard_language_selector",
            label_visibility="collapsed",
            index=["English", "中文"].index(st.session_state.language),
            on_change=st.rerun
        )
    with col_logout:
        if st.button(T["logout"], key="logout_btn"):
            st.session_state.authenticated = False
            st.session_state.prediction_history = []
            st.rerun()
    
    # 4. Professional Navigation Box
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    st.session_state.page = st.radio(
        "Navigation",
        options=T["nav_options"],
        index=TEXTS["English"]["nav_options"].index(st.session_state.page),
        horizontal=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.divider()

    # 5. Sidebar with Animated Stats
    with st.sidebar:
        from config import TOTAL_STUDENTS, AT_RISK_STUDENTS, ON_TRACK_STUDENTS, PREDICTION_ACCURACY
        
        st.markdown(f"<h2 style='text-align: center; color: var(--main-text-color);'>{T['system_status']}</h2>", unsafe_allow_html=True)
        
        # Total Students Card
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-title">{T['total_students']}</div>
            <div class="stat-number" id="stat-total">0</div>
        </div>
        """, unsafe_allow_html=True)
        
        # At-Risk Students Card
        st.markdown(f"""
        <div class="stat-card" style="border-left: 5px solid #C0392B;">
            <div class="stat-title">{T['at_risk']}</div>
            <div class="stat-number" id="stat-at-risk">0</div>
        </div>
        """, unsafe_allow_html=True)
        
        # On-Track Students Card
        st.markdown(f"""
        <div class="stat-card" style="border-left: 5px solid #27AE60;">
            <div class="stat-title">{T['on_track']}</div>
            <div class="stat-number" id="stat-on-track">0</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Accuracy Card
        st.markdown(f"""
        <div class="stat-card" style="border-left: 5px solid #F39C12;">
            <div class="stat-title">{T['accuracy']}</div>
            <div class="stat-number" id="stat-accuracy">0.000</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)
        st.caption(f"Current Theme: **{st.session_state.theme}**")

    # 6. Render Selected Page Content
    page_index = T["nav_options"].index(st.session_state.page)
    page_key = TEXTS["English"]["nav_options"][page_index]
    
    if page_key == "Home":
        render_home_page()
    elif page_key == "Predictions":
        render_predictions_page()
    elif page_key == "Students":
        render_students_page()
    elif page_key == "Reports":
        render_reports_page()
    elif page_key == "Settings":
        render_settings_page()

    st.markdown("<hr style='border: 1px solid #2874A6;'>", unsafe_allow_html=True)
    st.caption(T["footer"])
