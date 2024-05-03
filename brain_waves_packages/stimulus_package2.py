import os
import time
import json
import random
import pandas as pd
from gtts import gTTS
from psychopy import sound, core
import psychtoolbox as ptb


def generate_and_play_sentences(num_sentences=4, patient_id="patient0"):
    """
    Generates random sentences in the form NOUN is ADJECTIVE and VERB by 
    randomly selecting words from the noun, adjective, and verb word lists.
    Each generated sentence is then turned into an audio and played out 
    loud. There is a 5 second pause in between audio plays of each sentence.

    Parameters:
    - patient_id (str): patient id number, or eeg id number, to identify 
    who/what eeg the stimulus is being administered to
    - num_sentences (int): number of sentences you want to generate and play
    - noun, adj, and verb words: lists of words that the function takes to
    randomly generate sentences. By default they are set to the _list.txt
    word files in the root directory.

    Returns:
    - patient_id (str)
    - administered_sentences_df: a pandas DataFrame of sentences that 
    were generated and audio played, where each row contains the patient_id,
    timestamp, and sentence played.
    """
    #current_directory = os.path.dirname(os.path.abspath(__file__))

    noun_list_path = os.path.join("word_lists/noun_list.txt")
    adj_list_path = os.path.join("word_lists/adj_list.txt")
    verb_list_path = os.path.join("word_lists/verb_list.txt")

    # Define lists of words (modify these with your desired words, could even modify this function to take in lists
    # of words as arguments)

    with open(noun_list_path, "r") as noun_file:
        noun_list = [word.strip()
                     for line in noun_file for word in line.split(',')]

    with open(adj_list_path, "r") as adj_file:
        adj_list = [word.strip()
                    for line in adj_file for word in line.split(',')]

    with open(verb_list_path, "r") as verb_file:
        verb_list = [word.strip()
                     for line in verb_file for word in line.split(',')]

    # Retrieve current date
    current_date = time.strftime("%Y-%m-%d")

    if os.path.exists('patient_df.csv'):
        # Open the patient DataFrame
        patient_df = pd.read_csv('patient_df.csv')
    else:
        # Create an empty DataFrame if patient_df.csv doesn't exist
        patient_df = pd.DataFrame(
            columns=['patient_id', 'timestamp', 'sentence', 'date'])

    # Initialize a list to store administered sentences
    administered_sentences = []

    # Check to see if patient has already been given stimulus today
    if (patient_df['patient_id'] == patient_id).any() and (patient_df['date'] == current_date).any():
        print("Patient has already been administered stimulus protocol today")

    else:
        sentence_count = 0

        while sentence_count < num_sentences:
            # Generate random sentence
            noun = random.choice(noun_list)
            adj = random.choice(adj_list)
            verb = random.choice(verb_list)
            sentence = f"{noun} is {adj} and {verb}"

            # Capture sentence timestamp
            current_timestamp = time.time()

            # Append the administered sentence to the list
            administered_sentences.append({'patient_id': patient_id,
                                           'timestamp': current_timestamp,
                                           'sentence': sentence,
                                            'date': current_date})

            # initialize the google text to speech object
            tts = gTTS(text=sentence, lang="en")
            tts.save("temp.mp3")

            # Play audio
            sentence_sound = sound.Sound("temp.mp3")
            now = ptb.GetSecs()
            sound.Sound.play(sentence_sound, when=now)
            print(sentence)

            # Wait for 5 seconds before looping again
            core.wait(5)

            # Increment the sentence count
            sentence_count += 1

            # delete the intermediate mp3 file
            os.remove("temp.mp3")

    # Concatenate the list of administered sentences with the patient DataFrame
    administered_sentences_df = pd.concat([patient_df,
                                           pd.DataFrame(administered_sentences, columns=['patient_id', 'timestamp', 'sentence', 'date'])],
                                           ignore_index=True)

    # Overwrite old df with the new df
    administered_sentences_df.to_csv("patient_df.csv", index=False)