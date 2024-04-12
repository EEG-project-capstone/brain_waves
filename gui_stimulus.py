pip install streamlit
import streamlit as st
from stimulus_package import generate_and_play_sentences, update_patient_dict

def start_stimulus(patient_id):
    if patient_id.strip() == "":
        st.error("Please enter a patient ID.")
    else:
        _, administered_sentences_dict = generate_and_play_sentences(patient_id=patient_id)
        update_patient_dict(patient_id, administered_sentences_dict)
        st.success("Stimulus protocol successfully administered.")

# Streamlit app title
st.title("EEG Stimulus Package")

# Patient ID input
patient_id = st.text_input("Patient ID")

# Start button
if st.button("Start Stimulus"):
    start_stimulus(patient_id)
