# Stimulus Administration Package

## Overview

The Stimulus Administration Package provides a straightforward and intuitive interface for administering and recording auditory stimuli to patients, designed to be accessible to users without coding expertise. With intuitive functionalities for stimulus administration, patient record management, and note-taking, this software simplifies the process for researchers and clinicians alike. Users can seamlessly administer auditory stimuli to patients through a web-based interface, ensuring efficient data recording and management for research and clinical purposes.

## Usage guide

1. Set up a conda environment with the `environment.yml` file. Required packages are `gtts`, `psychopy`, `psychtoolbox`, and `playsound`.
     - PsychoPy no longer used due to erroring (now using `playsound`), would be great for future teams to troubleshoot this as it would allow for more specific control over stimulus.
2. Edit the word and/or sentence lists in the text files located in the `brain_waves_packages/corpus/` directory. Copy-Paste in your words and/or sentences into the appropriate .txt file(s). Alternatively, you may use the provided default words and sentence lists.
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

# Future Work Ideas
- Implement an archive function to remove patient data that we don't need to access anymore
- Tactile stimulus (hand squeeze, etc.)
- Methods of editing frequency at which words and sentences are played (might require finding an alternative to PsychoPy)
- Incorporating GUI tunable method to change hyperparameters (delays, hertz, etc.)

### Archive Entries [IN DEVELOPMENT]:
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

## Contributors

- Anika Gupta (Winter 2024)
- Arielle Hancko (Winter 2024)
- Jacob Cavon (Winter 2024, Spring 2024)
- Roni Weissman (Winter 2024, Spring 2024)
- Annika Philomin (Spring 2024)
- Khanh Ha (Spring 2024)

## Powerpoint Presentations
Winter 2024: https://docs.google.com/presentation/d/1Kp6XUgpTHJ_MS2kLk3vIcxjNE0yz_ODsBUjHLSKQaZU/edit?usp=sharing
Spring 2024: https://docs.google.com/presentation/d/1FUqLEs0Pi69MavDdpUPYJBafI9lskivDAvJT3tufLfA/edit?usp=sharing

## Gantt Chart Progress Report
Spring 2024: https://docs.google.com/spreadsheets/d/1dB0wKZc62g64NrvtKUnsOXBvMH8jNoDxWFfDWA1Aob4/edit?usp=sharing
