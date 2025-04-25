import streamlit as st

st.title("Body mass index calculator application")

h = st.radio("Pick one", ["Male", "Female"])
Height = st.number_input(" please enter your height")
Weight = st.number_input("Please enter your weight", min_value=1.0)
Age = st.number_input("Please enter your age", min_value=1)

if st.button("Calculate BMI"):
    bmi = (Weight) / (Height * Height)

    if h == "Male" and Age <= 5:
        if bmi >= 13.8 and bmi <= 17.8:
            st.success("Healthy")
        elif bmi > 17.5 and bmi <= 18.6:
            st.success("Overweight")
        elif bmi < 13.8:
            st.success("Underweight")
        else:
            st.success("Obesity")

    elif h == "Male" and Age > 5 and Age <= 10:
        if bmi >= 14.2 and bmi <= 19.2:
            st.success("Healthy")
        elif bmi > 19.3 and bmi <= 21.0:
            st.success("Overweight")
        elif bmi < 14.2:
            st.success("Underweight")
        else:
            st.success("Obesity")

    elif h == "Male" and Age > 10 and Age <= 15:
        if bmi >= 17.0 and bmi <= 23.3:
            st.success("Healthy")
        elif bmi > 23.4 and bmi <= 25.0:
            st.success("Overweight")
        elif bmi < 17.0:
            st.success("Underweight")
        else:
            st.success("Obesity")

    elif h == "Male" and Age > 15 and Age <= 25:
        if bmi < 18.5:
            st.success("Underweight")
        elif bmi >= 18.5 and bmi <= 24.9:
            st.success("Healthy")
        elif bmi >= 25.0 and bmi <= 29.9:
            st.success("Overweight")
        else:
            st.success("Obesity")

    elif h == "Male" and Age > 25 and Age <= 32:
        if bmi < 18.5:
            st.success("Underweight")
        elif bmi >= 18.5 and bmi <= 24.9:
            st.success("Healthy")
        elif bmi >= 25.0 and bmi <= 29.9:
            st.success("Overweight")
        else:
            st.success("Obesity")

    elif h == "Male" and Age > 32 and Age <= 40:
        if bmi < 18.5:
            st.success("Underweight")
        elif bmi >= 18.5 and bmi <= 24.9:
            st.success("Healthy")
        elif bmi >= 25.0 and bmi <= 29.9:
            st.success("Overweight")
        else:
            st.success("Obesity")

    elif h == "Female" and Age <= 5:
        if bmi < 13.6:
            st.write("Underweight")
        elif bmi >= 13.6 and bmi <= 17.2:
            st.success("Healthy")
        elif bmi >= 17.3 and bmi <= 18.3:
            st.write("Overweight")
        else:
            st.write("Obesity")

    elif h == "Female" and Age > 5 and Age <= 10:
        if bmi < 14.0:
            st.write("Underweight")
        elif bmi >= 14.0 and bmi <= 19.0:
            st.write("Healthy")
        elif bmi >= 19.1 and bmi <= 21:
            st.write("Overweight")
        else:
            st.write("Obesity")

    elif h == "Female" and Age > 10 and Age <= 15:
        if bmi < 17.5:
            st.write("Underweight")
        elif bmi >= 17.5 and bmi <= 24.0:
            st.write("Healthy")
        elif bmi >= 24.1 and bmi <= 26.0:
            st.write("Overweight")
        else:
            st.write("Obesity")

    elif h == "Female" and Age > 15 and Age <= 25:
        if bmi < 18.5:
            st.write("Underweight")
        elif bmi >= 18.5 and bmi <= 24.9:
            st.write("Healthy")
        elif bmi >= 25.0 and bmi <= 29.9:
            st.write("Overweight")
        else:
            st.write("Obesity")

    elif h == "Female" and Age > 25 and Age <= 32:
        if bmi < 18.5:
            st.write("Underweight")
        elif bmi >= 18.5 and bmi <= 24.9:
            st.write("Healthy")
        elif bmi >= 25.0 and bmi <= 29.9:
            st.write("Overweight")
        else:
            st.write("Obesity")

    elif h == "Female" and Age > 32 and Age <= 40:
        if bmi < 18.5:
            st.write("Underweight")
        elif bmi >= 18.5 and bmi <= 24.9:
            st.write("Healthy")
        elif bmi >= 25.0 and bmi <= 29.9:
            st.write("Overweight")
        else:
            st.write("Obesity")
