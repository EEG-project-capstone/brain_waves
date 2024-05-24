import streamlit as st
from stimulus_package3 import *
import pandas as pd
import os
import json 

def start_stimulus(patient_id):
    """
    input: patient_id
    ADD HOW MANY SENTENCES TO ADD AS START_STIMULUS ARGUMENT
    """
    if patient_id.strip() == "":
        st.error("Please enter a patient ID.")
    else:
        # Create placeholders for the messages
        administering_placeholder = st.empty()
        running_placeholder = st.empty()

        # Change the screen to "Administering Stimulus"
        administering_placeholder.write("Administering Stimulus...")
        running_placeholder.write("Stimulus is running...")  # Placeholder for actual stimulus running

        # Generate and play sentences
        _, administered_sentences_dict = generate_and_play_stimuli(patient_id=patient_id)  # Hardcoded number of sentences to 10
        #update_patient_dict(patient_id, administered_sentences_dict)

        # Clear the previous messages
        administering_placeholder.empty()
        running_placeholder.empty()

        # Show success message
        st.success("Stimulus protocol successfully administered.")

### Streamlit Interface ####
#defining patient_dict
#current_directory = os.path.dirname(os.path.abspath(__file__))
#patient_dict_path = os.path.join(current_directory, "patient_dict.json")
#with open(patient_dict_path, 'r') as f:
#    patient_dict = json.load(f)
patient_df = pd.read_csv("patient_df.csv")

# Streamlit app title
st.title("EEG Stimulus Package")

# Patient ID input
patient_id = st.text_input("Patient ID")

# Start button
if st.button("Start Stimulus"):
    start_stimulus(patient_id)

    # Add searchable dropdown menu of patient IDs
    st.subheader("Search Patient ID")
    selected_patient = st.selectbox("Select Patient ID", patient_df.patient_id.value_counts().index.tolist())
    
# Button to search for patient data
if st.button("Search Patient"):
    st.write("Stimulus Dates for Patient ID:", selected_patient)
    st.write(patient_df[patient_df.patient_id == selected_patient].date.tolist())  # Display dates when stimulus was run
