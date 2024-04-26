import streamlit as st
from stimulus_package import generate_and_play_sentences, update_patient_dict
import json 

def start_stimulus(num_sentences, patient_id):
    """
    input: patient_id
    ADD HOW MANY SENTENCES TO ADD AS START_STIMULUS ARGUMENT
    """
    if patient_id.strip() == "":
        st.error("Please enter a patient ID.")
    else:
        # Change the screen to "Administering Stimulus"
        st.write("Administering Stimulus...")
        st.write("Stimulus is running...")  # Placeholder for actual stimulus running
        _, administered_sentences_dict = generate_and_play_sentences(num_sentences=num_sentences, patient_id=patient_id)
        update_patient_dict(patient_id, administered_sentences_dict)
        st.success("Stimulus protocol successfully administered.")



### Streamlit Interface ####
#defining patient_dict
with open('patient_dict.json', 'r') as f:
    patient_dict = json.load(f)

# Streamlit app title
st.title("EEG Stimulus Package")

# Patient ID input
patient_id = st.text_input("Patient ID")
num_sentences = st.number_input("Number of sentences to administer")

    # Start button
if st.button("Start Stimulus"):
    start_stimulus(num_sentences, patient_id)

    # Add searchable dropdown menu of patient IDs
    st.subheader("Search Patient ID")
    selected_patient = st.selectbox("Select Patient ID", list(patient_dict.keys()))
    
# Button to search for patient data
if st.button("Search Patient"):
    st.write("Stimulus Dates for Patient ID:", selected_patient)
    st.write(patient_dict[selected_patient])  # Display dates when stimulus was run
