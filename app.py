import sys
import os
import streamlit as st

# ----------------------------
# Fix module import paths
# ----------------------------
# Add parent folder to Python path so 'src' can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_processing import load_budget_data, preprocess_data
from src.analysis import compare_budget
from src.prediction import predict_utilization
from src.reallocation import suggest_reallocation

# ----------------------------
# Streamlit App
# ----------------------------
st.title("💰 Smart Budget Utilization Monitoring System")

# Upload CSV
data_file = st.file_uploader("Upload Budget Data CSV", type="csv")

if data_file:
    # Load and preprocess
    df = load_budget_data(data_file)
    df = preprocess_data(df)

    # ----------------------------
    # Budget vs Actual Expenditure
    # ----------------------------
    st.subheader("📊 Budget vs Actual Expenditure")
    st.dataframe(df)

    # ----------------------------
    # Under-Utilized Departments
    # ----------------------------
    st.subheader("⚠️ Under-Utilized Departments")
    under_utilized = compare_budget(df)
    st.dataframe(under_utilized)

    # ----------------------------
    # Predicted Utilization
    # ----------------------------
    st.subheader("🔮 Predicted Utilization")
    df = predict_utilization(df)
    st.dataframe(df[['department', 'predicted_utilization']])

    # ----------------------------
    # Save predictions to CSV
    # ----------------------------
    predictions_file = os.path.join('data', 'predictions.csv')
    df.to_csv(predictions_file, index=False)
    st.success(f"Predictions saved to {predictions_file}")

    # ----------------------------
    # Suggested Fund Reallocation
    # ----------------------------
    st.subheader("💡 Suggested Fund Reallocation")
    suggestions = suggest_reallocation(df)
    st.dataframe(suggestions)