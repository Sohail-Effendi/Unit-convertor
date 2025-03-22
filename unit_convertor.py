import streamlit as st

st.title("Unit Convertor App")
st.markdown("### Converts length, weight and time instantly ")
st.write("Welcome select a category, enter a value and get the converted result in real time. ")
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometer to miles":
            return value * 0.621371
        elif unit == "Miles to Kilometer":
            return value / 0.621371
    
    if category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        
    if category == "Time":
        if unit == "Hours to minutes":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        
if category == "Length":
    unit = st.selectbox("Select conversation", ["Kilometer to miles", "Miles to Kilometer"])
elif category == "Weight":
    unit = st.selectbox("Select conversation", ["Kilograms to pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select conversation", ["Hours to minutes", "Minutes to hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"result is {result:.2f}")