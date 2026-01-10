import streamlit as st
from config import TOTAL_STUDENTS, AT_RISK_STUDENTS, ON_TRACK_STUDENTS, PREDICTION_ACCURACY

def set_styles(theme, background_url):
    bg_color = "rgba(255, 255, 255, 0.95)" if theme == "Light" else "rgba(18, 18, 18, 0.95)"
    text_color = "#1F618D" if theme == "Light" else "#FFFFFF"
    card_bg = "rgba(255, 255, 255, 0.7)" if theme == "Light" else "rgba(60, 60, 60, 0.5)"
    card_text_color = "#333333" if theme == "Light" else "#FFFFFF"
    
    st.markdown(f"""
    <style>
    /* Global Theme Vars */
    :root {{
        --main-text-color: {text_color};
        --card-bg-color: {card_bg};
        --card-text-color: {card_text_color};
    }}

    /* Solid Background for Main App (No Image) */
    [data-testid="stAppViewContainer"] {{
        background-color: {'#F5F7FA' if theme == 'Light' else '#0F1419'};
    }}

    /* Target the main content wrapper (the white/dark card) */
    .main .block-container {{
        background-color: {bg_color};
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 8px 40px rgba(0, 0, 0, 0.15);
        color: {card_text_color};
    }}

    /* Sidebar Styling */
    [data-testid="stSidebar"] {{
        background-color: {bg_color};
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 8px 40px rgba(0, 0, 0, 0.15);
        color: {card_text_color};
    }}

    /* --- TEXT HIGHLIGHTING --- */
    .main-title {{
        text-align: center;
        font-size: 42px;
        font-weight: 900;
        color: {text_color};
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
        margin-top: -10px; 
    }}
    .subtitle {{
        text-align: center;
        font-size: 22px;
        color: {'#34495E' if theme == 'Light' else '#E8E8E8'};
        font-weight: 500;
        margin-bottom: 30px;
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: {text_color} !important; 
        font-weight: 700 !important;
    }}
    
    /* Paragraph and text elements */
    p, div, span, label {{
        color: {card_text_color} !important;
    }}
    
    .risk-low {{
        color: #27AE60;
        font-weight: 900;
        font-size: 28px;
        text-shadow: 0 0 5px rgba(39, 174, 96, 0.4);
    }}
    .risk-high {{
        color: #C0392B;
        font-weight: 900;
        font-size: 28px;
        text-shadow: 0 0 5px rgba(192, 57, 43, 0.4);
    }}

    /* Card Styling */
    .stat-card {{
        background: var(--card-bg-color);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border-left: 5px solid {text_color};
        transition: transform 0.3s ease-in-out;
    }}
    .stat-card:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    }}
    .stat-title {{
        font-size: 14px;
        color: {'#566573' if theme == 'Light' else '#FFFFFF'};
        font-weight: 600;
        margin-bottom: 5px;
    }}
    .stat-number {{
        font-size: 26px;
        font-weight: 900;
        color: {text_color};
    }}

    /* ===== Header Section ===== */
    .dashboard-header {{
        background: linear-gradient(135deg, {card_bg} 0%, rgba(40, 116, 166, 0.15) 100%);
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border-left: 5px solid {text_color};
    }}

    .header-title {{
        font-size: 32px;
        font-weight: 900;
        color: {text_color};
        margin: 0 0 5px 0;
    }}

    .header-subtitle {{
        font-size: 16px;
        color: {'#566573' if theme == 'Light' else '#ABB2B9'};
        margin: 0;
    }}

    /* ===== Navigation Box ===== */
    .nav-container {{
        background: {card_bg};
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        border: 2px solid {text_color};
    }}

    /* Top Navigation Radio Buttons */
    div[role="radiogroup"] {{
        flex-direction: row !important;
        justify-content: center !important;
    }}
    /* Style for the button inside the radio group */
    label[data-baseweb="radio"] span {{
        padding: 8px 20px;
        border-radius: 8px;
        background-color: rgba(255, 255, 255, 0.1);
        color: {text_color} !important;
        font-weight: 600;
        margin: 0 5px;
        border: 1px solid {text_color};
        transition: all 0.3s;
    }}
    label[data-baseweb="radio"]:hover span {{
        background-color: {'#D6EAF8' if theme == 'Light' else '#454545'} !important;
        transform: translateY(-2px);
    }}
    /* Style for the SELECTED radio button */
    label[data-baseweb="radio"] input:checked + span {{
        background-color: {text_color} !important;
        color: {'white' if theme == 'Light' else '#111111'} !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }}
    </style>
    """, unsafe_allow_html=True)
    
    # --- JAVASCRIPT FOR COUNTER ANIMATION ---
    st.components.v1.html(f"""
    <script>
        function animateValue(id, start, end, duration) {{
            let range = end - start;
            let current = start;
            let increment = end > start ? 1 : -1;
            let stepTime = Math.abs(Math.floor(duration / range));
            let obj = document.getElementById(id);

            if (!obj) return; // Exit if element not found

            let timer = setInterval(function() {{
                current += increment;
                if (id === 'stat-accuracy') {{
                     obj.innerHTML = (current / 1000).toFixed(3); 
                }} else {{
                    obj.innerHTML = current.toLocaleString();
                }}
                
                if (current == end) {{
                    clearInterval(timer);
                }}
            }}, stepTime);
        }}
        
        // Only run animation once on page load
        if (!window.sessionStorage.getItem('counters_ran')) {{
            animateValue('stat-total', 0, {TOTAL_STUDENTS}, 2000);
            animateValue('stat-at-risk', 0, {AT_RISK_STUDENTS}, 2000);
            animateValue('stat-on-track', 0, {ON_TRACK_STUDENTS}, 2000);
            animateValue('stat-accuracy', 0, {int(PREDICTION_ACCURACY * 1000)}, 2000); // Animate scaled value
            window.sessionStorage.setItem('counters_ran', 'true');
        }}
    </script>
    """, height=0)

def set_login_styles():
    st.markdown("""
    <style>
    /* ===== Background Image for Login Page Only ===== */
    [data-testid="stAppViewContainer"] {
        background-image: url("https://scontent-lax3-1.xx.fbcdn.net/v/t39.30808-6/590429173_122113425153037920_7456146715077751058_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=127cfc&_nc_ohc=KgJiJpS5U4YQ7kNvwFkC7nB&_nc_oc=AdlyCRYPdLHgoPKoOEGXGAqLXu0MivBxz_LEag0VAr-C2QZN5MVg-iJtZnfYFUusBzs&_nc_zt=23&_nc_ht=scontent-lax3-1.xx&_nc_gid=6fa5dvfF1oDTQsHjJE2JLA&oh=00_AfhihFM_MnLXDZGYtZpiXSGOvK6l_kjt-vdxxC8OQNWsRg&oe=693111A3");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* ===== Single Frosted Glass Layer for Login Box and Form Only ===== */
    .login-box, .teacher-header {
        backdrop-filter: blur(10px);
        background-color: rgba(255, 255, 255, 0.12);
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* ===== Frosted Glass Only for Form Container ===== */
    [data-testid="stForm"] {
        backdrop-filter: blur(8px);
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.15);
    }

    /* ===== Frosted Glass Login Box Adjustments ===== */
    .login-box {
        width: 600px;
        margin: 1vh auto 5px auto;
        padding: 15px;
        text-align: center;
        animation: fadeSlide 1.5s ease-out;
    }

    /* ===== Teacher Login Header Adjustments ===== */
    .teacher-header {
        width: 400px;
        margin: 0 auto 15px auto;
        font-size: 24px;
        font-weight: bold;
        color: #FFFFFF;
        text-align: center;
        animation: fadeSlide 1.5s ease-out 0.6s both;
    }
    
    /* ===== Login Titles ===== */
    .login-title {
        font-size: 36px;
        color: #FFFFFF;
        font-weight: 800;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.4);
        animation: fadeSlide 1.5s ease-out 0.2s both;
    }

    .login-subtitle {
        font-size: 20px;
        color: #EAF2F8;
        margin-bottom: 15px;
        animation: fadeSlide 1.5s ease-out 0.4s both;
    }

    /* ===== Animation ===== */
    @keyframes fadeSlide {
        0% {opacity: 0; transform: translateY(-50px);}
        100% {opacity: 1; transform: translateY(0);}
    }

    /* ===== Tab Button Styling ===== */
    button[data-baseweb="tab"] {
        color: rgba(255, 255, 255, 0.9) !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        margin: 5px !important;
    }

    button[data-baseweb="tab"]:hover {
        color: #FFFFFF !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #FFFFFF !important;
        border-bottom: 3px solid #2874A6 !important;
    }

    /* ===== Form Inputs ===== */
    input {
        text-align: center;
        border-radius: 10px !important;
        font-size: 16px !important;
        border: none !important;
        background-color: rgba(255, 255, 255, 0.15) !important;
        color: black !important;
    }

    input::placeholder {
        color: rgba(0, 0, 0, 0.5) !important;
    }

    input:focus {
        background-color: rgba(255, 255, 255, 0.25) !important;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.3) !important;
    }

    /* ===== Checkbox Styling ===== */
    [data-baseweb="checkbox"] {
        color: rgba(255, 255, 255, 0.9) !important;
    }

    /* ===== Login Button ===== */
    div.stButton > button:first-child {
        background-color: #2874A6 !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        border: none !important;
        width: 100% !important;
        height: 40px !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #1F618D !important;
        transform: scale(1.03) !important;
    }

    /* ===== Footer ===== */
    .footer {
        text-align: center;
        color: #ffffff;
        font-size: 12px;
        margin-top: 1rem;
        animation: fadeSlide 1.5s ease-out 1.2s both;
        text-shadow: 0 1px 3px rgba(0,0,0,0.3);
    }

    /* ===== Message Containers ===== */
    [data-testid="stAlert"] {
        backdrop-filter: blur(10px) !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)
