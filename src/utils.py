import pandas as pd
import numpy as np
import time
import os
import joblib
import matplotlib.pyplot as plt
from config import TOTAL_STUDENTS

# Function to calculate feature importance for explanation (using dummy data as model is basic)
def get_risk_explanation(input_data, current_language):
    # This simulates a SHAP-like feature contribution calculation
    
    # Inputs: Attendance, Behavior, Midterm, Avg Assignment, Team Collab (Higher is better)
    contributions = {}
    
    # Use localized keys for display
    from language import TEXTS
    factors_map = {
        "Attendance": TEXTS[current_language]["attendance"],
        "Midterm Exam Score": TEXTS[current_language]["midterm_score"],
        "Late Submissions": TEXTS[current_language]["late_subs"],
        "Number of Previous Failures": TEXTS[current_language]["prev_failures"],
        "Stress Level": TEXTS[current_language]["stress_level"]
    }

    # Calculate contributions (Higher score here means higher risk)
    contributions[factors_map["Attendance"]] = (100 - input_data["Attendance"][0]) * 0.05 
    contributions[factors_map["Midterm Exam Score"]] = (100 - input_data["Midterm Exam Score"][0]) * 0.04
    contributions[factors_map["Late Submissions"]] = input_data["Late Submissions"][0] * 0.1
    contributions[factors_map["Number of Previous Failures"]] = input_data["Number of Previous Failures"][0] * 0.2
    contributions[factors_map["Stress Level"]] = input_data["Stress Level"][0] * 0.08

    # Identify top 3 contributing factors to risk
    sorted_contributions = sorted(contributions.items(), key=lambda item: item[1], reverse=True)
    
    explanation = []
    
    # Define generic explanation for low risk contribution
    generic_explanation = ["The predictive model identified multiple minor factors that collectively raised the risk score."]
    if current_language == "中文":
        generic_explanation = ["预测模型识别出多个次要因素共同提高了风险评分。"]

    for factor, score in sorted_contributions:
        if score > 0.5: # Threshold for significant contribution
            explanation.append(f"**{factor}:** " + ("Contributed significantly due to an unfavorable score/count." if current_language == "English" else "因分数/次数不利而贡献显著。"))

    if not explanation:
        return generic_explanation
    
    return explanation[:3] # Return top 3 risk factors

def load_model():
    model_path = os.path.join("model", "trained_model.pkl")
    try:
        return joblib.load(model_path)
    except FileNotFoundError:
        return None

def create_probability_chart(probabilities, current_language):
    from language import TEXTS
    T = TEXTS[current_language]
    
    labels = [T["prob_low_label"], T["prob_high_label"]]
    colors = ["#2ECC71", "#E74C3C"]
    fig, ax = plt.subplots(figsize=(4, 2.5)) 
    bars = ax.bar(labels, probabilities, color=colors)
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.05, 
                f'{yval*100:.1f}%', 
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_title(T["prob_title"], fontsize=14)
    ax.set_ylabel("", visible=False)
    ax.set_yticks([])
    ax.set_ylim(0, 1.05)
    
    return fig

def get_student_data():
    # Dummy Data Table
    from language import TEXTS
    T = TEXTS["English"]  # Using English for internal data representation
    
    data = {
        'ID': ['MH25061', 'JS25012', 'LW25088', 'ZH25045', 'FG25091'],
        'Name': ['AHMED MD SHAKIL', 'Jiang Siyu', 'Li Wei', 'Zhang Hui', 'Fan Guang'],
        'Major': ['Computer Science', 'Engineering', 'Business', 'Medicine', 'Arts'],
        'Status': ['At Risk', 'On Track', 'On Track', 'At Risk', 'On Track'],
        'Last Score': [65, 92, 85, 58, 78],
    }
    return pd.DataFrame(data)

def get_trend_data():
    # Dummy chart for overall risk trend
    trend_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "High Risk Count": [250, 220, 235, 260, 210, 275]
    }).set_index('Month')
    return trend_data

def get_factor_data():
    # Dummy bar chart for risk factors
    factor_data = pd.DataFrame({
        "Factor": ["Low Attendance", "Low Midterm", "High Stress", "Many Failures"],
        "Impact Score": [0.35, 0.25, 0.20, 0.15]
    }).set_index('Factor')
    return factor_data
