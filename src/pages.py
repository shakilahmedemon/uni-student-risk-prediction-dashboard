import streamlit as st
import pandas as pd
import time
from language import TEXTS
from utils import (
    get_risk_explanation, 
    load_model, 
    create_probability_chart, 
    get_student_data, 
    get_trend_data, 
    get_factor_data
)

def render_home_page():
    T = TEXTS[st.session_state.language]
    
    st.header(T["dash_overview"])
    st.markdown(T["home_welcome"])
    st.info(T["home_info"])
    
    st.subheader(T["recent_history"])
    if st.session_state.prediction_history:
        history_df = pd.DataFrame(st.session_state.prediction_history)
        
        # Rename columns based on language for display
        display_columns = {
            "Timestamp": T["hist_timestamp"], 
            "Student ID": T["hist_id"], 
            "Student Name": T["hist_name"], 
            "Risk Level": T["hist_risk"], 
            "Confidence": T["hist_conf"]
        }
        
        # Show top 5 recent predictions
        st.dataframe(
            history_df.tail(5)[list(display_columns.keys())].rename(columns=display_columns), 
            use_container_width=True, 
            hide_index=True
        )
    else:
        st.markdown(T["no_history"])

def render_predictions_page():
    T = TEXTS[st.session_state.language]
    
    st.header(T["risk_assessment"])
    
    # Load Trained Model
    model = load_model()
    if model is None:
        st.error(T["model_missing"])
        return

    # Input Section
    st.subheader(T["enter_details"])

    col_id, col_name = st.columns(2)
    with col_id:
        student_id = st.text_input(T["hist_id"], placeholder=T["id_placeholder"], key="pred_id")
    with col_name:
        student_name = st.text_input(T["hist_name"], placeholder=T["name_placeholder"], key="pred_name")

    # Mapping complexity strings to display texts
    complexity_options = [T["comp_low"], T["comp_medium"], T["comp_high"]]
    complexity_map = {T["comp_low"]: 0, T["comp_medium"]: 1, T["comp_high"]: 2}
    
    col1, col2 = st.columns(2)
    with col1:
        attendance = st.slider(T["attendance"], 0, 100, 80, key="att")
        behavior_score = st.slider(T["behavior_score"], 0, 10, 7, key="behav")
        midterm_score = st.slider(T["midterm_score"], 0, 100, 70, key="midterm")
        avg_assignment_score = st.slider(T["avg_assign_score"], 0, 100, 75, key="assign")
        late_submissions = st.slider(T["late_subs"], 0, 10, 1, key="late")
    with col2:
        team_collaboration = st.slider(T["team_collab"], 0, 10, 8, key="collab")
        project_complexity_display = st.selectbox(T["project_comp"], complexity_options, key="comp")
        hours_studied = st.slider(T["hours_studied"], 0, 50, 12, key="hours")
        previous_failures = st.number_input(T["prev_failures"], min_value=0, max_value=10, value=0, key="failures")
        stress_level = st.slider(T["stress_level"], 0, 10, 3, key="stress")

    # Encode Project Complexity
    project_complexity_encoded = complexity_map[project_complexity_display]

    # Create DataFrame for prediction
    input_data = pd.DataFrame({
        "Attendance": [attendance],
        "Behavior / Discipline Score": [behavior_score],
        "Midterm Exam Score": [midterm_score],
        "Average Assignment Score": [avg_assignment_score],
        "Late Submissions": [late_submissions],
        "Team Collaboration": [team_collaboration],
        "Project Complexity": [project_complexity_encoded],
        "Hours Studied per Week": [hours_studied],
        "Number of Previous Failures": [previous_failures],
        "Stress Level": [stress_level],
        "Average Submission Delay": [st.slider(T["avg_delay"], 0, 30, 2, key="delay")]
    })

    st.divider()
    if st.button(T["predict_btn"], type="primary"):
        if not student_id or not student_name:
            st.warning(T["warn_input"])
            return

        try:
            prediction = model.predict(input_data)[0]
            probabilities = model.predict_proba(input_data)[0]
            
            risk_level = T["high_risk"] if prediction == 1 else T["low_risk"]
            confidence = probabilities[prediction]

            st.subheader(f"{T['hist_risk']} ({student_id})")

            result_col, explanation_col = st.columns([1, 1.5])

            with result_col:
                if prediction == 1:
                    st.markdown(f"<p class='risk-high'>⚠️ {risk_level} (Confidence: {confidence*100:.2f}%)</p>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<p class='risk-low'>✅ {risk_level} (Confidence: {confidence*100:.2f}%)</p>", unsafe_allow_html=True)

                # Send Email Alert Feature
                if prediction == 1:
                    st.warning(T["warning_intervene"])
                    if st.button(T["email_btn"]):
                        st.success(T["email_success"].format(name=student_name))
                else:
                    st.info(T["info_ontrack"])

            with explanation_col:
                st.markdown(f"#### {T['top_factors']}")
                if prediction == 1:
                    explanation = get_risk_explanation(input_data, st.session_state.language)
                    for item in explanation:
                        st.markdown(f"- {item}")
                else:
                    st.markdown(T["explanation_low"])

            st.divider()

            # --- LOG TO HISTORY ---
            st.session_state.prediction_history.append({
                "Timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Student ID": student_id,
                "Student Name": student_name,
                "Risk Level": risk_level,
                "Confidence": f"{confidence*100:.2f}%",
                "Attendance (%)": attendance,
                "Midterm Score": midterm_score,
                "Stress Level": stress_level,
            })
            # ----------------------

            # Probability Visualization
            fig = create_probability_chart(probabilities, st.session_state.language)
            st.pyplot(fig)

        except Exception as e:
            st.error(f"{T['error_prediction']} {e}")

def render_students_page():
    T = TEXTS[st.session_state.language]
    
    st.header(T["mgmt_console"])
    st.info(T["mgmt_info"])
    
    st.subheader(T["current_list"].format(TOTAL_STUDENTS=2500))
    
    # Get student data
    df = get_student_data()
    
    # Localize column names for display
    df_display = df.copy()
    df_display.columns = [
        T["table_id"], 
        T["table_name"], 
        T["table_major"], 
        T["table_status"], 
        T["table_score"]
    ]
    
    # Simple search bar
    search_term = st.text_input(T["search_placeholder"], placeholder=T["search_placeholder"], key="search_term")
    if search_term:
        df_filtered = df[
            df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
        ]
        df_filtered_display = df_filtered.copy()
        df_filtered_display.columns = df_display.columns
    else:
        df_filtered = df
        df_filtered_display = df_display
        
    st.dataframe(df_filtered_display, use_container_width=True, hide_index=True)
    
    if st.button(T["report_btn"]):
        st.success(T["report_success"].format(count=len(df_filtered)))

def render_reports_page():
    T = TEXTS[st.session_state.language]
    
    st.header(T["reports_analytics"])
    st.subheader(T["model_summary"])
    
    from config import PREDICTION_ACCURACY
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(T["model_accuracy"], f"{PREDICTION_ACCURACY:.3f}")
        st.write(T["model_info"])
        
        # Dummy chart for overall risk trend
        st.subheader(T["risk_trend"])
        trend_data = get_trend_data()
        st.line_chart(trend_data)
        
    with col_b:
        st.subheader(T["key_risk_dist"])
        
        # Dummy bar chart for risk factors
        factor_data = get_factor_data()
        st.bar_chart(factor_data)

    st.divider()
    
    st.subheader(T["session_history"])
    if st.session_state.prediction_history:
        history_df = pd.DataFrame(st.session_state.prediction_history)
        
        # Rename columns based on language for reports page
        display_columns = {
            "Timestamp": T["hist_timestamp"], 
            "Student ID": T["hist_id"], 
            "Student Name": T["hist_name"], 
            "Risk Level": T["hist_risk"], 
            "Confidence": T["hist_conf"],
            "Attendance (%)": T["attendance"],
            "Midterm Score": T["midterm_score"],
            "Stress Level": T["stress_level"]
        }

        st.dataframe(
            history_df.rename(columns=display_columns), 
            use_container_width=True, 
            hide_index=True
        )
        csv = history_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label=T["download_btn"],
            data=csv,
            file_name='student_risk_history.csv',
            mime='text/csv',
        )
    else:
        st.info(T["no_report_data"])

def render_settings_page():
    T = TEXTS[st.session_state.language]
    
    st.header(T["user_settings"])
    
    # --- INTERFACE SETTINGS ---
    st.subheader(T["interface_settings"])
    
    # Theme Toggle with callback
    def update_theme():
        st.session_state.theme = st.session_state.theme_toggle
    
    st.radio(
        T["theme_select"], 
        ["Light", "Dark"], 
        key="theme_toggle",
        index=0 if st.session_state.theme == "Light" else 1,
        on_change=update_theme,
        horizontal=True
    )
    
    # Custom Background URL Input
    new_url = st.text_input(
        T["bg_url"],
        value=st.session_state.background_url,
        help=T["bg_url_tip"]
    )
    
    if st.button(T["apply_bg"]):
        if st.session_state.background_url != new_url:
            st.session_state.background_url = new_url
            st.rerun() 
        else:
            st.info("Background URL is already set to this value.")
    
    st.divider()
    
    # --- ACCOUNT SETTINGS ---
    st.subheader(T["account_settings"])
    st.markdown(T["logged_in_as"])
    st.markdown(f"{T['last_login']} **" + pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S") + "**")
    
    # Tabs for different account actions
    tab1, tab2 = st.tabs(["Update Profile", "Change Password"])
    
    with tab1:
        st.markdown("#### Update Your Profile Information")
        
        col1, col2 = st.columns(2)
        with col1:
            new_name = st.text_input(
                "Full Name",
                value=st.session_state.teacher_info['full_name'],
                key="new_name_input"
            )
        with col2:
            new_email = st.text_input(
                "Email Address",
                value=st.session_state.teacher_info['email'],
                key="new_email_input"
            )
        
        col3, col4 = st.columns(2)
        with col3:
            new_dept = st.text_input(
                "Department",
                value=st.session_state.teacher_info['department'],
                key="new_dept_input"
            )
        with col4:
            new_phone = st.text_input(
                "Phone Number",
                value=st.session_state.teacher_info['phone'],
                key="new_phone_input"
            )
        
        if st.button("Save Profile Changes", key="save_profile_btn"):
            # Validate inputs
            if not new_name or not new_email:
                st.error("Full Name and Email are required fields.")
            elif "@" not in new_email:
                st.error("Please enter a valid email address.")
            else:
                # Update the teacher info
                st.session_state.teacher_info['full_name'] = new_name
                st.session_state.teacher_info['email'] = new_email
                st.session_state.teacher_info['department'] = new_dept
                st.session_state.teacher_info['phone'] = new_phone
                st.success("✅ Profile information updated successfully!")
                st.info(f"Updated details:\n- Name: {new_name}\n- Email: {new_email}\n- Department: {new_dept}\n- Phone: {new_phone}")
    
    with tab2:
        st.markdown("#### Change Your Password")
        
        current_password = st.text_input(
            "Current Password",
            type="password",
            key="current_pwd"
        )
        
        new_password = st.text_input(
            "New Password",
            type="password",
            key="new_pwd",
            help="Password must be at least 8 characters long"
        )
        
        confirm_password = st.text_input(
            "Confirm New Password",
            type="password",
            key="confirm_pwd"
        )
        
        if st.button("Change Password", key="change_pwd_btn"):
            # Validate current password (hardcoded for demo)
            if current_password != "yangzhou123":
                st.error("❌ Current password is incorrect. Please try again.")
            elif len(new_password) < 8:
                st.error("❌ New password must be at least 8 characters long.")
            elif new_password != confirm_password:
                st.error("❌ New passwords do not match. Please try again.")
            elif new_password == current_password:
                st.error("❌ New password must be different from current password.")
            else:
                # In a real application, you would hash and store this securely
                # For now, we'll just update it in session state
                st.session_state.teacher_password = new_password
                st.success("✅ Password changed successfully!")
                st.info("Your new password will be used for your next login.")
                st.warning("For security reasons, you will be logged out. Please log in again with your new password.", icon="⚠️")
