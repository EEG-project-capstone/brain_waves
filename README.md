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

1. Set up a conda environment with the `environment.yml` file. Required packages are `gtts`, `psychopy`, and `psychtoolbox`.
     - PsychoPy no longer used due to erroring, would be great for future teams to troubleshoot this as it would allow for more specific control over stimulus.
2. Edit the noun, adjective, and verb lists in the text files (or use the provided default words).
3. Import `generate_and_play_sentences` and `update_patient_dict` from `stimulus_package.py`.
4. Call `generate_and_play_sentences` with appropriate arguments to administer the verbal stimuli.
5. Call `update_patient_dict` with the returns from step 4 to update the patient dictionary with administered stimuli data.

## Functions

### 1. `generate_and_play_sentences`

This function generates random sentences using the `noun`, `verb`, and `adj_list.txt` files. It then converts these sentences into audio files and plays them. Each sentence is timestamped with the Python clock and saved into a nested dictionary.

**Parameters:**
- `num_sentences` (int): Number of sentences to generate and play.
- `patient_id` (str): Identifier for the EEG patient.
- `noun_list_path`, `adj_list_path`, `verb_list_path` (str): Paths to the text files containing lists of nouns, adjectives, and verbs.

**Returns:**
- `patient_id` (str): Identifier for the EEG patient.
- `administered_sentences_dict` (dict): Dictionary containing timestamped sentences.

### 2. `update_patient_dict`

This function updates the `patient_dict.json` with the sentences generated and administered by the `generate_and_play_sentences` function. It organizes the data by patient ID and date.

**Parameters:**
- `patient_id` (str): Identifier for the EEG patient.
- `administered_sentences_dict` (dict): Dictionary containing timestamped sentences.

**Returns:**
- None (Updates the `patient_dict.json`)

## Notes

- This package is currently a work in progress, with plans to develop a GUI.
- The functions can be used in Jupyter Notebook environments.
- Remember to modify the word lists as desired for different corpus of words.

## Contributors

- Anika Gupta
- Arielle Hancko
- Jacob Cavon
- Roni Weissman

## Powerpoint Presentations
https://docs.google.com/presentation/d/1Kp6XUgpTHJ_MS2kLk3vIcxjNE0yz_ODsBUjHLSKQaZU/edit?usp=sharing

