### User Story
In the realm of comatose patient research, a user-friendly GUI software is essential for administering audio stimuli efficiently across various settings. Physician researchers require a tool that enables easy patient selection, date specification for administration, and playback of diverse auditory stimuli, such as sentences, words, and beeps. Additionally, the software should facilitate the quick addition of detailed notes to patient records to support comprehensive data analysis. With this solution, physician researchers can conduct auditory processing studies effectively and gain valuable insights into comatose patient responsiveness.

### Use Cases

### Graphical User Interface (GUI)

**Description:** Users can perform various actions through a GUI web interface, including administering stimuli, searching and querying patient entries, and adding notes to patient entries.  
**Actor:** Administrator/User  
**Trigger:** User interacts with the GUI to perform desired actions.

**Basic Flow:**
1. **Administer Stimuli:**
    - User enters the patient ID.
    - User clicks the "Start Stimulus" button.
    - System checks if the patient has already been administered the stimulus protocol for the current date.
    - If not, the system generates and plays a series of stimuli in random order.
    - System records the administered stimuli and their timestamps.
    - The results are saved in a CSV file.

2. **Search/Query:**
    - User selects a patient ID from a dropdown list of patients who have already been administered stimuli.
    - User selects a date to see what stimuli were administered.
    - The system retrieves and displays entries matching the selected criteria, including the stimuli and their order.

3. **Add Notes:**
    - User selects a patient ID and date.
    - User enters the note content.
    - User clicks the "Add Note" button.
    - The note is added to the selected patient entry in the `patient_notes.csv` file.

4. **Find Notes:**
    - User selects a patient ID and date from dropdown lists.
    - The system retrieves and displays notes for the selected patient and date.

**Alternate Flow:** None  
**Post-conditions:** 
- Administered stimuli and timestamps are recorded for the patient.
- The system displays entries matching the selected patient ID and date.
- Notes are appended to the patient's entry.
- The system displays notes matching the selected patient ID and date.

**Components:**

**Component Name:** `gui_stimulus.py`  
**Input:**
- User-entered `patient_id` for administering stimuli.
- User-selected `patient_id` and date for searching/querying and finding notes.
- Note content and date for adding notes.

**Output:** 
- Display of entries matching the selected patient ID and date.
- Recording of administered stimuli and timestamps.
- Addition of notes to patient entries.
- Display of notes matching the selected patient ID and date.


### Backend Functions

#### Administer Stimuli

**Description:** Users can administer different types of stimuli (sentence, word, beep) to patients and record the results.  
**Actor:** Administrator/User  
**Trigger:** User decides to administer stimuli to a patient via the GUI.

**Basic Flow:**
1. User enters the patient ID.
2. User clicks the "Start Stimulus" button.
3. System checks if the patient has already been administered the stimulus protocol for the current date.
4. If not, the system generates and plays a series of stimuli in random order using the `generate_and_play_stimuli` function from `stimulus_package3.py`.
5. The system records the administered stimuli and their timestamps.
6. The results are saved in the `patient_df.csv` file.

**Alternate Flow:** None  
**Post-conditions:** 
- Administered stimuli and timestamps are recorded for the patient.
- The results are saved to `patient_df.csv`.

**Components:**

**Component Name:** `administer_sentence`  
**Input:**
- `sentence_list` (list): A list of sentences to choose from and play.
**Output:** 
- `sentence` (str): The administered sentence.
- `timestamp` (float): The timestamp when the sentence was administered.

**Component Name:** `administer_word`  
**Input:**
- `word_list` (list): A list of words to choose from and play.
**Output:** 
- `word` (str): The administered word.
- `timestamp` (float): The timestamp when the word was administered.

**Component Name:** `administer_beep`  
**Input:**
- `frequency` (int): The frequency of the beep sound. Default is 1000 Hz.
- `duration` (float): The duration of the beep sound in seconds. Default is 0.5 seconds.
**Output:** 
- `beep` (str): The string "BEEP".
- `timestamp` (float): The timestamp when the beep was administered.

**Component Name:** `get_random_stimulus_order`  
**Input:** None  
**Output:** 
- Updates patient_df.csv with string of order stimuli were administered, date, patient_id, timestamps of stimuli, and strings of administered stimuli


**Component Name:** `generate_and_play_stimuli`  
**Input:**
- `patient_id` (str): The ID of the patient. Default is "patient0".
**Output:**
- The function plays the stimuli in a random order for the patient.
- The results are recorded and saved to `patient_df.csv`.


#### 3. Record Stimulus Package Notes

**Description:** Users can record notes related to the stimulus package administered to patients.  
**Actor:** Administrator/User  
**Trigger:** User decides to record a note for the administered stimuli.  

**Basic Flow:**
1. User selects the patient entry for which to add a note.
2. User enters the note content and the date of the note.
3. User triggers the stimulus_package_notes function.
4. The note is added to the selected patient entry.

**Alternate Flow:** None  
**Post-conditions:** The note is appended to the patient's entry related to the stimulus package.

**Components:**

**Component Name:** `stimulus_package_notes`  
**Input:**
- `patient_notes_path` (str): Path to the patient_notes.csv file.
- `patient_id` (str): Identifier for the patient.
- `note` (str): Note to be added.
- `date` (str): Date of the note.

**Output:**
- `patient_notes.csv` is updated with the note.