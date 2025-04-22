import streamlit as st

# Title
st.title("Maryams BMI Calculator")

# User input
st.markdown("Enter your **height** (in cm) and **weight** (in kg) below:")

height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0)

# Calculate BMI
if height > 0 and weight > 0:
    bmi = weight / ((height / 100) ** 2)
    st.success(f"Your BMI is: **{bmi:.2f}**")

    # BMI Category
    if bmi < 18.5:
        st.warning("🔎 You are **Underweight**.")
    elif 18.5 <= bmi < 25:
        st.info("✅ You are in the **Normal** range.")
    elif 25 <= bmi < 30:
        st.warning("⚠️ You are **Overweight**.")
    else:
        st.error("🚨 You are in the **Obese** range.")

