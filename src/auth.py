import streamlit as st
import numpy as np
import time
import qrcode
import io
from language import TEXTS

def render_login_page():
    # Get current language texts
    T = TEXTS[st.session_state.language]
    
    # ===================== Multi-language Support in Top-Right =====================
    col_left, col_center, col_right = st.columns([6, 6, 1])
    with col_right:
        # Update session state language when selection changes
        st.session_state.language = st.selectbox(
            "Select Language", 
            ["English", "中文"], 
            key="language_topright", 
            label_visibility="collapsed",
            index=["English", "中文"].index(st.session_state.language)
        )
    
    # ===================== Login Header =====================
    st.markdown(f"""
    <div class="login-box">
        <div class="login-title" style="text-align:center;">{T["title_text"]}</div>
        <div class="login-subtitle" style="text-align:center;">{T["login_subtitle"]}</div>
    </div>

    <div class="teacher-header" style="text-align:center;">{T["login_portal_text"]}</div>
    """, unsafe_allow_html=True)

    # Center the login form
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Tab-based login mode selection
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Username/Password", "OTP", T["qr_login_text"], "WeChat", "Register"])

        with tab1:
            with st.form("login_form_user_pass"):
                username = st.text_input("Username", placeholder=T["username_placeholder"], key="username")
                password = st.text_input("Password", placeholder=T["password_placeholder"], type="password", key="password")
                remember = st.checkbox(T["remember_text"])
                submit_user_pass = st.form_submit_button(T["login_button_text"])
                if submit_user_pass:
                    if username == "teacher" and password == "yangzhou123":
                        st.session_state.authenticated = True
                        st.success(T["login_success"])
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error(T["invalid_credentials"])

        with tab2:
            with st.form("login_form_otp"):
                email = st.text_input(T["email_placeholder"], key="otp_email")
                if st.form_submit_button(T["send_otp_text"]):
                    st.session_state.generated_otp = np.random.randint(100000, 999999)
                    st.success(T["otp_success"].format(otp=st.session_state.generated_otp))
                otp_input = st.text_input("Enter OTP", key="otp_input")
                submit_otp = st.form_submit_button(T["verify_otp_text"])
                if submit_otp:
                    if str(otp_input) == str(st.session_state.get("generated_otp", "")):
                        st.session_state.authenticated = True
                        st.success(T["otp_verified"])
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error(T["invalid_otp"])

        with tab3:
            with st.form("login_form_qr"):
                # Generate QR Code for demo authentication
                qr_data = f"TeacherLogin-{int(time.time())}"
                qr_img = qrcode.make(qr_data)
                buf = io.BytesIO()
                qr_img.save(buf)
                buf.seek(0)
                st.image(buf, caption="Scan this QR with your mobile app")
                submit_qr = st.form_submit_button(T["qr_scan_text"])
                if submit_qr:
                    # In real scenario, check QR scan authentication
                    st.session_state.authenticated = True
                    st.success(T["qr_verified"])
                    time.sleep(1)
                    st.rerun()

        with tab4:
            with st.form("login_form_wechat"):
                col_wechat_left, col_wechat_right = st.columns(2)
                with col_wechat_left:
                    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/WeChat_logo.svg/1024px-WeChat_logo.svg.png", width=80)
                    st.markdown("<p style='text-align:center; color:white; font-weight:600;'>WeChat</p>", unsafe_allow_html=True)
                with col_wechat_right:
                    # Display QR code for WeChat
                    st.image("https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://yangzhou.edu/wechat-login", width=120, caption="Scan with WeChat")
                st.markdown("Scan with WeChat to log in", unsafe_allow_html=True)
                submit_wechat = st.form_submit_button("Login with WeChat")
                if submit_wechat:
                    # Placeholder for WeChat login logic
                    st.success("WeChat login successful!")
                    time.sleep(1)
                    st.rerun()
        
        with tab5:
            st.markdown("### 📋 Create New Account")
            with st.form("registration_form"):
                new_username = st.text_input("Choose Username", placeholder="Enter desired username", key="reg_username")
                new_email = st.text_input("Email Address", placeholder="Enter your email", key="reg_email")
                new_password = st.text_input("Create Password", type="password", placeholder="At least 8 characters", key="reg_password")
                confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter password", key="reg_confirm")
                department = st.selectbox("Department", ["Academic Affairs", "Administration", "IT Support", "Finance", "Other"], key="reg_department")
                
                # Password strength indicator for registration
                if new_password:
                    password_strength = "Weak"
                    strength_color = "🔴"
                    if len(new_password) >= 8:
                        if any(c.isupper() for c in new_password) and any(c.isdigit() for c in new_password):
                            password_strength = "Strong"
                            strength_color = "🟢"
                        else:
                            password_strength = "Medium"
                            strength_color = "🟡"
                    st.caption(f"Password Strength: {strength_color} {password_strength}")
                
                submit_register = st.form_submit_button("Register Account", use_container_width=True)
                if submit_register:
                    if not new_username or not new_email or not new_password:
                        st.error("❌ All fields are required.")
                    elif len(new_password) < 8:
                        st.error("❌ Password must be at least 8 characters long.")
                    elif new_password != confirm_password:
                        st.error("❌ Passwords do not match.")
                    elif new_username in st.session_state.registered_users:
                        st.error("❌ Username already exists. Please choose another.")
                    elif "@" not in new_email:
                        st.error("❌ Please enter a valid email address.")
                    else:
                        # Register new user
                        st.session_state.registered_users[new_username] = new_password
                        st.success("✅ Account created successfully!")
                        st.info(f"📝 Your username: **{new_username}**\n\n🔐 You can now log in using your username and password in the 'Username/Password' tab.")

        # Forgot Password link under the tabs
        st.markdown(f"<a href='#' style='color:white; font-size:14px; display:block; text-align:center; margin-top:10px;'>{T['forgot_password_text']}</a>", unsafe_allow_html=True)

    st.markdown(f"<p class='footer'>{T['footer']}</p>", unsafe_allow_html=True)
