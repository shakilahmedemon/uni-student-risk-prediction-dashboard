# Proactive Student Risk Prediction System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Predictive-green)
![Explainable AI](https://img.shields.io/badge/XAI-Enabled-purple)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

A **machine learning–powered academic early-warning system** built with **Streamlit** to proactively identify, analyze, and explain academic risk among university students.  
The system integrates **predictive analytics**, **explainable AI**, **multilingual UI (English / 中文)**, and **secure authentication** to support data-driven academic decision-making.


## Overview

The Proactive Student Risk Monitoring System predicts whether a student is academically at risk by analyzing performance and behavioral indicators.  
Unlike black-box models, the system provides **explainable insights**, allowing educators and administrators to understand *why* a student is flagged as high risk.

The application is fully interactive, web-based, modular, and designed following clean software engineering practices.


## Key Features

- Machine learning–based student risk prediction  
- Explainable AI (XAI) for transparent decision-making  
- Multilingual interface (English / 中文)  
- Secure login-based authentication  
- Interactive dashboards and reports  
- Modular, scalable, and maintainable architecture  


## Prediction Factors

The predictive model evaluates multiple student-related indicators, including:
- Attendance percentage  
- Midterm examination score  
- Number of late submissions  
- Number of previous academic failures  
- Stress level indicators  

These factors are processed by a trained machine learning model to generate a **risk score**, **risk classification**, and **explanation of contributing factors**.


## Installation

Clone the repository:

git clone https://github.com/your-username/your-repo-name.git

cd your-repo-name


## Create and activate a virtual environment (recommended):

python -m venv venv

source venv/bin/activate   # Linux / macOS

venv\Scripts\activate      # Windows


## Install dependencies:

pip install -r requirements.txt


## Running the Application

streamlit run app.py

The application will open in your default web browser.

## Model Training

If the trained model file is not working, generate it using:

python model/train_model.py

This will create trained_model.pkl inside the model/ directory.


## Author

AHMED MD SHAKIL

studying Software Engineering at Yangzhou University, China.
