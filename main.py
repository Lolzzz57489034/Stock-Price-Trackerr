import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏏 Cricket Match Predictor")

# User Inputs
team1 = st.selectbox("Select Team 1", ["India", "Australia", "England", "Pakistan", "South Africa"])
team2 = st.selectbox("Select Team 2", ["India", "Australia", "England", "Pakistan", "South Africa"])
venue = st.selectbox("Select Venue", ["Mumbai", "Sydney", "Lahore", "London", "Cape Town"])
toss_winner = st.selectbox("Who won the toss?", [team1, team2])
bat_or_bowl = st.radio("Choose Toss Decision", ["Bat", "Bowl"])

# Convert inputs to model format
input_data = pd.DataFrame([[team1, team2, venue, toss_winner, bat_or_bowl]],
                          columns=["team1", "team2", "venue", "toss_winner", "bat_or_bowl"])

# Make Prediction
if st.button("Predict Winner"):
    prediction = model.predict(input_data)[0]
    st.success(f"🏆 Predicted Winner: **{prediction}**")
