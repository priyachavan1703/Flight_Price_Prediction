import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("Decision_tree_regression.pkl", "rb") as f:
    model = pickle.load(f)

# Encoding dictionaries (same as used in training)
airline_map = {
    'IndiGo': 1, 'Air India': 2, 'Jet Airways': 3, 'SpiceJet': 4,
    'Multiple carriers': 5, 'GoAir': 6, 'Vistara': 7, 'Air Asia': 8,
    'Vistara Premium economy': 9, 'Jet Airways Business': 10,
    'Multiple carriers Premium economy': 11, 'Trujet': 12
}
source_map = {
    'Banglore': 1, 'Kolkata': 2, 'Delhi': 3, 'Mumbai': 4, 'Chennai': 5
}
destination_map = {
    'New Delhi': 0, 'Banglore': 1, 'Cochin': 2, 'Kolkata': 3,
    'Hyderabad': 4, 'Delhi': 5
}
stops_map = {
    'non-stop': 0, '1 stop': 1, '2 stops': 2, '3 stops': 3, '4 stops': 4
}

# Streamlit UI
st.title("✈️ Flight Price Predictor")
st.markdown("Fill in the flight details below to predict ticket charges.")

# Inputs
Airline = st.selectbox("Airline", list(airline_map.keys()))
Source = st.selectbox("Source", list(source_map.keys()))
Destination = st.selectbox("Destination", list(destination_map.keys()))
Total_Stops = st.selectbox("Total Stops", list(stops_map.keys()))

Date = st.number_input("Journey Date (1-31)", min_value=1, max_value=31)
Month = st.number_input("Journey Month (1-12)", min_value=1, max_value=12)
Year = st.number_input("Journey Year", min_value=2023, max_value=2030, value=2024)

Dep_hours = st.number_input("Departure Hour (0-23)", min_value=0, max_value=23)
Dep_min = st.number_input("Departure Minute (0-59)", min_value=0, max_value=59)

Arrival_hours = st.number_input("Arrival Hour (0-23)", min_value=0, max_value=23)
Arrival_min = st.number_input("Arrival Minute (0-59)", min_value=0, max_value=59)

Duration_hours = st.number_input("Duration Hours", min_value=0, max_value=50)
Duration_min = st.number_input("Duration Minutes", min_value=0, max_value=59)

if st.button("Predict Flight Price"):
    try:
        # Encode user input
        input_data = pd.DataFrame({
            'Airline': [airline_map[Airline]],
            'Source': [source_map[Source]],
            'Destination': [destination_map[Destination]],
            'Total_Stops': [stops_map[Total_Stops]],
            'Date': [Date],
            'Month': [Month],
            'Year': [Year],
            'Dep_hours': [Dep_hours],
            'Dep_min': [Dep_min],
            'Arrival_hours': [Arrival_hours],
            'Arrival_min': [Arrival_min],
            'Duration_hours': [Duration_hours],
            'Duration_min': [Duration_min]
        })

        prediction = model.predict(input_data)[0]
        st.success(f"🎯 Predicted Flight Price: ₹{round(prediction, 2)}")

    except Exception as e:
        st.error(f"Prediction failed: {e}")
