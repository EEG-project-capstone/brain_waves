import streamlit as st
from stimulus_package import generate_and_play_sentences, update_patient_dict
import os
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

def load_patient_dict(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                patient_dict = json.load(f)
            except json.JSONDecodeError:
                patient_dict = {}
    else:
        patient_dict = {}
    return patient_dict

def main():
    # Load patient_dict from JSON file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    patient_dict_path = os.path.join(current_directory, "patient_dict.json")


    patient_dict = load_patient_dict(patient_dict_path)


	with open(patient_dict_path, 'r') as f:
        	patient_dict = json.load(f)

	if __name__ = "__main__":
		main()


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

    if st.button("Search Patient"):
        st.write("Stimulus Dates for Patient ID:", selected_patient)
        st.write(patient_dict[selected_patient])  # Display dates when stimulus was run

    # Button to add patient note
    page = st.sidebar.selectbox("Select a page", ["Home", "Patient Notes"])
    if page == "Home":
        st.title("Welcome to Patient Management System")
        if st.button("Add Patient Note"):
            show_patient_note_page()

    elif page == "Patient Notes":
        st.title("Patient Notes")
        show_patient_note_page()

def show_patient_note_page():
    st.write("Input Patient Note:")
    patient_note = st.text_area("Patient Note")

    st.write("Select Date:")
    note_date = st.date_input("Date")

    if st.button("Submit"):
        # Add note to patient_notes dictionary with date as key
        st.session_state.patient_notes[note_date] = patient_note
        st.success("Note added successfully!")

if __name__ == "__main__":
    main()
