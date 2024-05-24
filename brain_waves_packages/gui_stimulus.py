import streamlit as st
from stimulus_package3 import *
import pandas as pd
import os
import time

patient_df = pd.read_csv("patient_df.csv")
current_date = time.strftime("%Y-%m-%d")

def start_stimulus(input_patient_id):
    """
    input: patient_id
    ADD HOW MANY SENTENCES TO ADD AS START_STIMULUS ARGUMENT
    """
    if patient_id.strip() == "":
        st.error("Please enter a patient ID.")
    
    elif ((patient_df['patient_id'] == patient_id) & (patient_df['date'] == current_date)).any():
        st.error("Patient has already been administered stimulus protocol today")

    else:
        # Create placeholders for the messages
        administering_placeholder = st.empty()
        running_placeholder = st.empty()

        # Change the screen to "Administering Stimulus"
        administering_placeholder.write("Administering Stimulus...")
        running_placeholder.write("Stimulus is running...")  # Placeholder for actual stimulus running

        # Generate and play sentences
        generate_and_play_stimuli(input_patient_id)
        #update_patient_dict(patient_id, administered_sentences_dict)

        # Clear the previous messages
        administering_placeholder.empty()
        running_placeholder.empty()

        # Show success message
        st.success("Stimulus protocol successfully administered and data saved to patient_df.csv.")

### Streamlit Interface ####

# Streamlit app title
st.title("EEG Stimulus Package")

st.header("Administer Auditory Stimuli", divider='rainbow')
# Patient ID input
patient_id = st.text_input("Enter Patient/EEG ID")

# Start button
if st.button("Start Stimulus"):
    start_stimulus(patient_id)


st.header("Search Patients Already Administered Stimuli", divider='rainbow')

# Add searchable dropdown menu of patient IDs
selected_patient = st.selectbox("Select Patient ID", patient_df.patient_id.value_counts().index.sort_values())

selected_date = st.selectbox("Select Administered Date", patient_df[patient_df.patient_id == selected_patient].date.value_counts().index.sort_values())

st.subheader("The following auditory stimuli were administered:")
for stimulus in patient_df[(patient_df.patient_id == selected_patient) & (patient_df.date == selected_date)].stimulus.tolist():
    st.write(stimulus)

st.subheader("Stimuli were administered in the following order:")
for order in patient_df[(patient_df.patient_id == selected_patient) & (patient_df.date == selected_date)].order.value_counts().index.tolist():
    st.write(order)