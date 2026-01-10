# --- LANGUAGE DICTIONARY ---
TEXTS = {
    "English": {
        # General/Navigation
        "nav_options": ["Home", "Students", "Predictions", "Reports", "Settings"],
        "logout": "🔑 Logout", "hi_teacher": "Hi, Teacher!", "main_title": "Yangzhou University Student's Proactive Risk Predictor",
        "subtitle": "Predictive Analytics Dashboard for Faculty",
        "system_status": "System Status", "total_students": "🧑‍🎓 Total Students Monitored", "at_risk": "⚠️ At-Risk Students (Intervention Needed)",
        "on_track": "✅ On-Track Students", "accuracy": "📈 Prediction Accuracy (ROC-AUC)",
        "footer": "© 2025 Yangzhou University | Developed by AHMED MD SHAKIL (文龙), Student ID: MH25061 for Software Project Management",
        
        # Login Page
        "title_text": "Yangzhou University (扬州大学)", "login_subtitle": "Student's Service System",
        "login_portal_text": "Teacher's Login Portal", "username_placeholder": "Enter Username",
        "password_placeholder": "Enter Password", "login_button_text": "Login", "remember_text": "Remember Me",
        "forgot_password_text": "Forgot Password?", "otp_login_text": "Login with OTP", "email_placeholder": "Enter Email",
        "send_otp_text": "Send OTP", "verify_otp_text": "Verify OTP", "qr_login_text": "Login with QR Code",
        "qr_scan_text": "I have scanned the QR", "invalid_credentials": "❌ Invalid username or password",
        "otp_success": "OTP sent! (Demo OTP: {otp})", "otp_verified": "✅ OTP verified, login successful!",
        "invalid_otp": "❌ Invalid OTP", "qr_verified": "✅ QR code verified, login successful!",
        "login_success": "✅ Login successful! Redirecting...",

        # Home Page
        "dash_overview": "Dashboard Overview", "home_welcome": "Welcome to the Yangzhou University Proactive Risk Predictor Dashboard. Use the navigation bar above to switch between modules.",
        "home_info": "💡 Quick Start: Navigate to the 'Predictions' tab to analyze a student's risk profile.",
        "recent_history": "Recent Prediction History", "no_history": "No predictions made yet in this session.",
        "hist_timestamp": "Timestamp", "hist_id": "Student ID", "hist_name": "Student Name", "hist_risk": "Risk Level", "hist_conf": "Confidence",
        
        # Predictions Page
        "risk_assessment": "Student Risk Assessment", "model_missing": "Trained model not found! Please run train_model.py first.",
        "enter_details": "Enter Student Details for Prediction", "id_placeholder": "Enter Student ID (e.g., MH25061)",
        "name_placeholder": "Enter Full Name (e.g., AHMED MD SHAKIL)", "attendance": "Attendance (%)", 
        "behavior_score": "Behavior / Discipline Score (0–10)", "midterm_score": "Midterm Exam Score (0–100)",
        "avg_assign_score": "Average Assignment Score (0–100)", "late_subs": "Late Submissions (number)", 
        "team_collab": "Team Collaboration (0–10)", "project_comp": "Project Complexity", "hours_studied": "Hours Studied per Week",
        "prev_failures": "Number of Previous Failures", "stress_level": "Stress Level (0–10)", "avg_delay": "Average Submission Delay (days)",
        "comp_low": "Low", "comp_medium": "Medium", "comp_high": "High", "predict_btn": "Predict Student Risk",
        "warn_input": "Please enter both Student ID and Student Name before prediction.", "high_risk": "High Risk of Failure",
        "low_risk": "Low Risk of Failure", "top_factors": "Top Risk Contributing Factors", 
        "explanation_low": "All major indicators are positive. Key factors are sufficient **Attendance** and **Midterm Exam Score**.",
        "warning_intervene": "Immediate intervention may be required.", "email_btn": "📧 Send Email Alert to Advisor",
        "email_success": "Email alert successfully simulated for **{name}** and their academic advisor.",
        "info_ontrack": "Student is on track. Good work!", "prob_title": "Prediction Probability Distribution",
        "prob_low_label": "Low Risk", "prob_high_label": "High Risk", "error_prediction": "Error during prediction: ",
        
        # Students Page
        "mgmt_console": "Student Management Console", "mgmt_info": "This section would integrate with the University's Student Information System (SIS).",
        "current_list": "Current Student List ({TOTAL_STUDENTS} Records)", "search_placeholder": "Search Student by Name or ID (e.g., AHMED MD SHAKIL or MH25061)",
        "report_btn": "Generate Detailed Report for Filtered Students", "report_success": "Detailed reports for {count} students are being generated.",
        "table_id": "ID", "table_name": "Name", "table_major": "Major", "table_status": "Status", "table_score": "Last Score",
        
        # Reports Page
        "reports_analytics": "Academic Reports and Analytics", "model_summary": "Model Performance Summary",
        "model_accuracy": "Model Accuracy (ROC-AUC)", "model_info": "The model shows high confidence in distinguishing between high and low-risk students.",
        "risk_trend": "Monthly Risk Trend (Last 6 Months)", "key_risk_dist": "Key Risk Factor Distribution",
        "session_history": "Session Prediction History", "download_btn": "Download Full History as CSV",
        "no_report_data": "No prediction data to generate reports from yet.",
        
        # Settings Page
        "user_settings": "User and Application Settings", "interface_settings": "Interface Settings",
        "theme_select": "Select Theme:", "account_settings": "Account Settings (Teacher)", "logged_in_as": "Logged in as **teacher**.",
        "last_login": "Last login:", "change_password": "Change Password (Simulated)", "update_profile": "Update Profile Information (Simulated)",
        "bg_url": "Custom Background Image URL", "bg_url_tip": "Enter a high-resolution image URL (e.g., from Unsplash, ImageKit, etc.)",
        "apply_bg": "Apply New Background"
    },
    "中文": {
        # General/Navigation
        "nav_options": ["主页", "学生管理", "风险预测", "报告分析", "设置"],
        "logout": "🔑 登出", "hi_teacher": "老师，您好！", "main_title": "扬州大学学生主动风险预测系统",
        "subtitle": "教职员工预测分析仪表板",
        "system_status": "系统状态", "total_students": "🧑‍🎓 监测学生总数", "at_risk": "⚠️ 需干预的高风险学生",
        "on_track": "✅ 正常学习中的学生", "accuracy": "📈 预测准确率 (ROC-AUC)",
        "footer": "© 2025 扬州大学 | 由 AHMED MD SHAKIL(文龙) 开发 (学号: MH25061) 用于软件项目管理",
        
        # Login Page
        "title_text": "扬州大学 (Yangzhou University)", "login_subtitle": "学生服务系统",
        "login_portal_text": "教师登录门户", "username_placeholder": "输入用户名",
        "password_placeholder": "输入密码", "login_button_text": "登录", "remember_text": "记住我",
        "forgot_password_text": "忘记密码?", "otp_login_text": "验证码登录", "email_placeholder": "输入邮箱",
        "send_otp_text": "发送验证码", "verify_otp_text": "验证验证码", "qr_login_text": "二维码登录",
        "qr_scan_text": "我已扫描二维码", "invalid_credentials": "❌ 无效的用户名或密码",
        "otp_success": "验证码已发送! (演示验证码: {otp})", "otp_verified": "✅ 验证码验证成功，登录成功！",
        "invalid_otp": "❌ 无效的验证码", "qr_verified": "✅ 二维码验证成功，登录成功！",
        "login_success": "✅ 登录成功！正在重定向...",

        # Home Page
        "dash_overview": "仪表板概览", "home_welcome": "欢迎使用扬州大学主动风险预测仪表板。使用上方的导航栏切换模块。",
        "home_info": "💡 快速开始：导航到"风险预测"选项卡以分析学生的风险概况。",
        "recent_history": "最近预测历史记录", "no_history": "本会话中尚未进行任何预测。",
        "hist_timestamp": "时间戳", "hist_id": "学生ID", "hist_name": "学生姓名", "hist_risk": "风险等级", "hist_conf": "置信度",
        
        # Predictions Page
        "risk_assessment": "学生风险评估", "model_missing": "未找到训练模型！请先运行 train_model.py。",
        "enter_details": "输入学生信息进行预测", "id_placeholder": "输入学生ID (例如: MH25061)",
        "name_placeholder": "输入全名 (例如: AHMED MD SHAKIL)", "attendance": "出勤率 (%)",
        "behavior_score": "行为/纪律分数 (0–10)", "midterm_score": "期中考试分数 (0–100)",
        "avg_assign_score": "平均作业分数 (0–100)", "late_subs": "迟交次数", 
        "team_collab": "团队协作 (0–10)", "project_comp": "项目复杂度", "hours_studied": "每周学习小时数",
        "prev_failures": "先前不及格次数", "stress_level": "压力水平 (0–10)", "avg_delay": "平均提交延迟 (天)",
        "comp_low": "低", "comp_medium": "中", "comp_high": "高", "predict_btn": "预测学生风险",
        "warn_input": "请在预测前输入学生ID和学生姓名。", "high_risk": "高失败风险",
        "low_risk": "低失败风险", "top_factors": "主要风险贡献因素", 
        "explanation_low": "所有主要指标均为正面。关键因素是足够的**出勤率**和**期中考试成绩**。",
        "warning_intervene": "可能需要立即干预。", "email_btn": "📧 发送邮件提醒给导师",
        "email_success": "已成功模拟向**{name}**及其学术导师发送邮件提醒。",
        "info_ontrack": "学生表现良好，继续保持！", "prob_title": "预测概率分布",
        "prob_low_label": "低风险", "prob_high_label": "高风险", "error_prediction": "预测时出错: ",
        
        # Students Page
        "mgmt_console": "学生管理控制台", "mgmt_info": "此部分将与大学的学生信息系统 (SIS) 集成。",
        "current_list": "当前学生列表 ({TOTAL_STUDENTS} 条记录)", "search_placeholder": "按姓名或ID搜索学生 (例如: AHMED MD SHAKIL 或 MH25061)",
        "report_btn": "生成过滤学生的详细报告", "report_success": "正在为 {count} 名学生生成详细报告。",
        "table_id": "ID", "table_name": "姓名", "table_major": "专业", "table_status": "状态", "table_score": "最近分数",
        
        # Reports Page
        "reports_analytics": "学术报告与分析", "model_summary": "模型性能摘要",
        "model_accuracy": "模型准确率 (ROC-AUC)", "model_info": "该模型在区分高风险和低风险学生方面显示出高置信度。",
        "risk_trend": "月度风险趋势 (过去 6 个月)", "key_risk_dist": "关键风险因素分布",
        "session_history": "会话预测历史记录", "download_btn": "下载完整历史记录 (CSV)",
        "no_report_data": "尚无预测数据可生成报告。",
        
        # Settings Page
        "user_settings": "用户和应用程序设置", "interface_settings": "界面设置",
        "theme_select": "选择主题:", "account_settings": "账户设置 (教师)", "logged_in_as": "当前登录用户: **teacher**。",
        "last_login": "上次登录时间:", "change_password": "更改密码 (模拟)", "update_profile": "更新个人信息 (模拟)",
        "bg_url": "自定义背景图片 URL", "bg_url_tip": "输入高分辨率图片 URL (例如: 来自 Unsplash, ImageKit 等)",
        "apply_bg": "应用新背景"
    }
}
