# Automated Verbal Stimulus Package

## Overview

This Verbal Stimulus Package is designed to generate random sentences and administer them as auditory stimuli, particularly for EEG patients. It consists of two Python functions that facilitate this process.

## Usage guide

1. Set up a conda environment with the `environment.yml` file. Required packages are `gtts`, `psychopy`, and `psychtoolbox`.
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
