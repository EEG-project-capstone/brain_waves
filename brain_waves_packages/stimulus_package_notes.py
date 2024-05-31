import os
import time
import pandas as pd


def add_notes(patient_id="patient0", note="blank test note"):
    """
    Adds a note for a patient to a CSV file if the
    patient has already been administered stimulus.

    Parameters:
    - patient_id (str): The identifier for the
    patient, such as a patient ID or EEG ID.
    - note (str): The note to be added for the patient.

    Returns:
    - None, but overwrites/updates the patient_notes.csv

    Note:
    The function checks if the patient has been administered stimulus by
    verifying if there exists a record for the patient in 'patient_df.csv'.
    If such a record exists, the note is appended to 'patient_notes.csv'. 
    If 'patient_df.csv' does not exist, it prints a message indicating
    that stimulus package hasn't been run for the patient yet.
    """
    # Retrieve current date
    current_date = time.strftime("%Y-%m-%d")

    if os.path.exists('patient_notes.csv'):
        # Open the patient notes DataFrame
        patient_notes = pd.read_csv('patient_notes.csv')
    else:
        # Create an empty DataFrame if patient_df.csv doesn't exist
        patient_notes = pd.DataFrame(columns=['patient_id', 'notes', 'date'])

    if os.path.exists('patient_df.csv'):
        # Open the patient administered sentences DataFrame
        patient_df = pd.read_csv('patient_df.csv')
    else:
        # Create an empty DataFrame if patient_df.csv doesn't exist
        print('Make sure the patient_df.csv exists, if it does not, generate sentences was never run (ie no patients have been administered stimulus yet).')

    # Check to see if patient has already been given stimulus
    if (patient_df['patient_id'] == patient_id).any():
        # Create a DataFrame with the new note
        new_note = pd.DataFrame([{'patient_id': patient_id, 'notes': note, 'date': current_date}])
        # Concatenate the new note with the existing patient notes DataFrame
        patient_notes = pd.concat([patient_notes, new_note], ignore_index=True)
        # Save the updated DataFrame to CSV
        patient_notes.to_csv("patient_notes.csv", index=False)
    else:
        print('Patient has not been administered stimulus yet, double-check patient_id number.')
