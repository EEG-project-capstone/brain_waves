# IN PROGRESS COMPONENTS FOR NEW USE CASES
## Use Cases

### Archive Entries [NOT WORKING]:
- **Description:** Users can archive/hide specific patient entries in the system.
- **Actor:** Administrator/User
- **Trigger:** User decides to archive an entry.
- **Basic Flow:**
  1. User selects the patient/EEG entry to be archived.
  2. User triggers the archive function.
  3. The selected entry is hidden/archived from the system.
- **Alternate Flow:** None
- **Post-conditions:** The archived entry is no longer visible in the system.

#### Components:
- **Component Name:** `archive_entry`
  - **Input:**
    - `patient_dict_path` (str): Path to the patient_dict.json file.
    - `patient_id` (str): Identifier for the patient/EEG.
  - **Output:**
    - None

### Annotating Entries - Adding Notes [WORKS]:
- **Description:** Users can add notes to patient entries for reference or additional information.
- **Actor:** Administrator/User
- **Trigger:** User decides to add a note to a patient entry.
- **Basic Flow:**
  1. User selects the patient/EEG entry to add a note.
  2. User enters the note content and the date of the note.
  3. User triggers the add note function.
  4. The note is added to the selected patient entry.
- **Alternate Flow:** None
- **Post-conditions:** The note is appended to the patient's entry.

#### Components:
- **Component Name:** `add_notes`
  - **Input:**
    - `patient_notes_path` (str): Path to the patient_notes.json file.
    - `patient_id` (str): Identifier for the patient/EEG.
    - `note` (str): Note to be added.
    - `date` (str): Date of the note.
  - **Output:**
    - None

### Search/Query Function [WORKS]:
- **Description:** Users can search and query patient entries based on various criteria.
- **Actor:** Administrator/User
- **Trigger:** User initiates a search/query action.
- **Basic Flow:**
  1. User enters the search query (e.g., date, words from notes, patient/EEG ID).
  2. User triggers the search function.
  3. The system retrieves entries matching the query criteria.
- **Alternate Flow:** None
- **Post-conditions:** The system displays entries matching the search/query criteria.

#### Components:
- **Component Name:** `search_entries`
  - **Input:**
    - `patient_dict_path` (str): Path to the patient_dict.json file.
    - `patient_notes_path` (str): Path to the patient_notes.json file.
    - `query` (str): String query to search for (date, words from notes, patient/EEG ID, etc.).
  - **Output:**
    - `result` (dict): Dictionary containing key-value pairs that match the query.
   
### Existing Functions:

#### 1. Generate and Play Sentences [WORKS]:
- **Description:** Generates random sentences and administers them as auditory stimuli for EEG patients.
- **Actor:** EEG Technician/User
- **Trigger:** User initiates the generation and administration of sentences.
- **Basic Flow:**
  1. User specifies the number of sentences to generate and play.
  2. User provides the patient ID for the EEG session.
  3. User specifies the paths to the text files containing lists of nouns, adjectives, and verbs.
  4. User triggers the function to generate and play sentences.
- **Alternate Flow:** None
- **Post-conditions:** Sentences are played as auditory stimuli, and a dictionary containing timestamped sentences is returned.

#### 2. Update Patient Dictionary [WORKS]:
- **Description:** Updates the patient_dict.json with the sentences generated and administered by the Generate and Play Sentences function.
- **Actor:** Backend System/User
- **Trigger:** After the sentences are generated and played, the user initiates the update of the patient dictionary.
- **Basic Flow:**
  1. User provides the patient ID for the EEG session.
  2. User provides the dictionary containing timestamped sentences generated during the session.
  3. User triggers the function to update the patient dictionary.
- **Alternate Flow:** None
- **Post-conditions:** The patient_dict.json is updated with the administered sentences for the specified patient ID.





# Automated Verbal Stimulus Package

## Overview

This Verbal Stimulus Package is designed to generate random sentences and administer them as auditory stimuli, particularly for EEG patients. It consists of two Python functions that facilitate this process.

## Usage guide

1. Set up a conda environment with the `environment.yml` file. Required packages are `gtts`, `psychopy`, `psychtoolbox`, and `playsound`.
     - PsychoPy no longer used due to erroring (now using `playsound`), would be great for future teams to troubleshoot this as it would allow for more specific control over stimulus.
2. Edit the word and/or sentence lists in the text files (or use the provided default words and sentence lists).
3. Launch the GUI by navigating `brain_waves_packages` directory in the terminal. Then write `streamlit run gui_stimulus.py` into the terminal and enter. This should launch the GUI in the browser.
4. Administer stimulus by entering a `patient_id` into the textbox at the top of the screen, then push the start stimulus button. Play around with the other functionalities of the GUI.

# Functions

## Graphical User Interface (GUI)

### GUI Stimulus Package

This script provides a user interface for administering auditory stimuli to patients. It utilizes the Streamlit library for creating a web-based interface. The main functionalities include administering stimuli, searching for patients who have already been administered stimuli, adding notes to patient records, and finding patient notes.

#### Usage:
Run the backend functions through the GUI web interface. Launch the GUI by following step 3 in Usage guide above.

#### Components:
- **Administer Auditory Stimuli:** Allows users to input patient/EEG ID and start administering auditory stimuli. If a patient has already been administered stimulus protocol on the current date, an error message is displayed.
- **Search Patients Already Administered Stimuli:** Enables users to search for patients who have already been administered stimuli. Users can select a patient ID and date to view the administered stimuli and their order.
- **Add Notes to Your Selected Patient and Date:** Provides a text input field for users to add notes to a selected patient and date. Users can click the "Add Note" button to append the note to the patient's record.
- **Find Patient Notes:** Allows users to find notes written for a selected patient and date. Users can select a patient ID and date to view the notes.

#### Dependencies:
- streamlit
- stimulus_package3
- stimulus_package_notes
- pandas
- os
- time

#### Output:
The script generates and saves data to 'patient_df.csv' and 'patient_notes.csv' files.


## Backend Functions

### administer_sentence

Administers a sentence stimulus to a patient.

**Parameters:**
- `sentence_list` (list): A list of sentences to choose from and play.

**Returns:**
- `sentence` (str): The administered sentence.
- `timestamp` (float): The timestamp when the sentence was administered.

---

### administer_word

Administers a word stimulus to a patient.

**Parameters:**
- `word_list` (list): A list of words to choose from and play.

**Returns:**
- `word` (str): The administered word.
- `timestamp` (float): The timestamp when the word was administered.

---

### administer_beep

Administers a beep stimulus to a patient.

**Parameters:**
- `frequency` (int): The frequency of the beep sound. Default is 1000 Hz.
- `duration` (float): The duration of the beep sound in seconds. Default is 0.5 seconds.

**Returns:**
- `beep` (str): The string "BEEP".
- `timestamp` (float): The timestamp when the beep was administered.

---

### get_random_stimulus_order

Generates a random order of stimuli to be administered.

**Returns:**
- `stimuli` (list): A list of stimuli ("sentence", "word", "beep") in random order.

---

### generate_and_play_stimuli

Generates and plays auditory stimuli for a patient.

**Parameters:**
- `patient_id` (str): The ID of the patient. Default is "patient0".

**Outputs:**
- The function plays the selected stimuli for the patient.
- The results are recorded and saved to 'patient_df.csv'.


## Notes

- GUI has been developed using Streamlit
- The functions can be used in Jupyter Notebook environments

## Future Work Ideas
- Implement an archive function to remove patient data that we don't need to access anymore
- Tactile stimulus (hand squeeze, etc.)
- Methods of editing frequency at which words and sentences are played (might require finding an alternative to PsychoPy)
- Incorporating GUI tunable method to change hyperparameters (delays, hertz, etc.)

## Contributors

- Anika Gupta
- Arielle Hancko
- Jacob Cavon
- Roni Weissman
- Annika Philomin
- Khanh Ha

## Powerpoint Presentations
Winter 2024: https://docs.google.com/presentation/d/1Kp6XUgpTHJ_MS2kLk3vIcxjNE0yz_ODsBUjHLSKQaZU/edit?usp=sharing
Spring 2024: incoming
