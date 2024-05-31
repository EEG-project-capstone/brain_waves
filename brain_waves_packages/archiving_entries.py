import json

def load_patient_data(filepath):
    """Load patient data from a JSON file."""
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def archive_entry(patient_dict_path, patient_id):
    """Archive a patient entry in the patient dictionary JSON file."""
    # Load existing patient data
    patient_data = load_patient_data(patient_dict_path)

    # Check if the patient ID exists
    if patient_id in patient_data:
        # Archive the entry by setting an 'archived' flag
        patient_data[patient_id]['archived'] = True

        # Save the updated data back to the JSON file
        with open(patient_dict_path, 'w') as file:
            json.dump(patient_data, file, indent=4)
        print(f"Patient ID {patient_id} has been archived.")
    else:
        print("Patient ID not found in the database.")

# Usage example (You might need to adjust these details based on actual implementation)
if __name__ == "__main__":
    patient_dict_path = 'path_to_patient_dict.json'
    patient_id = 'patient1234'
    archive_entry(patient_dict_path, patient_id)

