import os
import time
import random
import pandas as pd
from gtts import gTTS
from psychopy import sound, core
import psychtoolbox as ptb
from playsound import playsound
#import winsound
#import pyecho


def administer_sentence(sentence_list):
    
    """
    Administers a sentence stimulus to a patient.

    Parameters:
    - sentence_list (list): A list of sentences to choose from and play.

    Returns:
    - sentence (str): The administered sentence.
    - timestamp (float): The timestamp when the sentence was administered.
    """
    
    # Initialize word to be played by gTTS
    sentence = random.choice(sentence_list)

    # Get timestamp of when word is played
    timestamp = time.time()
    
    # Initialize gTTS and play the sentence audio
    tts = gTTS(text=sentence, lang="en")
    tts.save("temp_sentence.mp3")
    #sentence_sound = sound.Sound("temp_sentence.mp3")
    now = ptb.GetSecs()
    #Replacing sound.Sound.play (which is using PsychoPy) with a python version of running sound player.
    #PsychoPy is the better option because it allows you to control frequency + timing, but it is no longer working
    #PsychoPy has been reported to have issues running, but if future teams can work on getting this up and running that would be great!
    #sound.Sound.play(sentence_sound, when=now)
    playsound("temp_sentence.mp3")

    # Delete intermediate mp3 file
    if os.path.exists("temp_sentence.mp3"):
        os.remove("temp_sentence.mp3")

    return sentence, timestamp

def administer_word(word_list):

    """
    Administers a word stimulus to a patient.

    Parameters:
    - word_list (list): A list of words to choose from and play.

    Returns:
    - word (str): The administered word.
    - timestamp (float): The timestamp when the word was administered.
    """
    
    # Initialize word to be played by gTTS
    word = random.choice(word_list)

    # Get timestamp of when word is played
    timestamp = time.time()
    
    # Initialize gTTS and play the sentence audio
    tts = gTTS(text=word, lang="en")
    tts.save("temp_word.mp3")
    #word_sound = sound.Sound("temp_word.mp3")
    now = ptb.GetSecs()
    #sound.Sound.play(word_sound, when=now)
    playsound("temp_word.mp3")

    # Delete intermediate mp3 file
    if os.path.exists("temp_word.mp3"):
        os.remove("temp_word.mp3")

    return word, timestamp

def administer_beep(frequency=1000, duration=0.5):

    """
    Administers a beep stimulus to a patient.

    Parameters:
    - frequency (int): The frequency of the beep sound. Default is 1000 Hz.
    - duration (float): The duration of the beep sound in seconds. Default is 0.5 seconds.

    Returns:
    - beep (str): The string "BEEP".
    - timestamp (float): The timestamp when the beep was administered.
    """
    
    # Get timestamp of when beep will play
    timestamp = time.time()
    
    # Initialize sound
    frequency = 1000
    duration = 0.5
    playsound("brain_waves_packages/sample_beep.mp3")
    #for a Windows machine, use:
    #winsound.Beep(frequency, duration)
    
    #commented out: the PsychoPy version of creating the beep sound. We shifted to using a Python version.
    #beep_sound = sound.Sound(value=frequency, secs=duration)
    #now = ptb.GetSecs()
    #sound.Sound.play(beep_sound, when=now)

    return "BEEP", timestamp

def get_random_stimulus_order():

    """
    Generates a random order of stimuli to be administered.

    Returns:
    - stimuli (list): A list of stimuli ("sentence", "word", "beep") in random order.
    """
    
    stimuli = ["sentence", "word", "beep"]
    random.shuffle(stimuli)
    return stimuli

def generate_and_play_stimuli(patient_id="patient0"):

    """
    Generates and plays auditory stimuli for a patient.

    Parameters:
    - patient_id (str): The ID of the patient. Default is "patient0".

    Outputs:
    - The function plays the selected stimuli for the patient.
    - The results are recorded and saved to 'patient_df.csv'.
    """

    sentence_list_path = os.path.join("corpus/rodika_sentences.txt")
    word_list_path = os.path.join("corpus/word_list.txt")

    with open(sentence_list_path, 'r') as file:
        sentence_list = [sentence.strip(', \n') for sentence in file]

    with open(word_list_path, "r") as word_file:
        word_list = [word.strip() for line in word_file for word in line.split(',')]

    current_date = time.strftime("%Y-%m-%d")

    if os.path.exists('patient_df.csv'):
        patient_df = pd.read_csv('patient_df.csv')
    else:
        patient_df = pd.DataFrame(columns=['patient_id', 'date', 'stimulus', 'timestamp', 'order'])

    administered_stimuli = []

    if ((patient_df['patient_id'] == patient_id) & (patient_df['date'] == current_date)).any():
        print("Patient has already been administered stimulus protocol today")
        return
    else:
        stimulus_order = get_random_stimulus_order()

        for stimulus in stimulus_order:
            if stimulus == "sentence":
                sentence, timestamp = administer_sentence(sentence_list)
                administered_stimuli.append({
                    'patient_id': patient_id,
                    'date': current_date,
                    'stimulus': sentence,
                    'timestamp': timestamp,
                    'order': ", ".join(stimulus_order)
                })
            elif stimulus == "word":
                word, timestamp = administer_word(word_list)
                administered_stimuli.append({
                    'patient_id': patient_id,
                    'date': current_date,
                    'stimulus': word,
                    'timestamp': timestamp,
                    'order': ", ".join(stimulus_order)
                })
            elif stimulus == "beep":
                beep, timestamp = administer_beep()
                administered_stimuli.append({
                    'patient_id': patient_id,
                    'date': current_date,
                    'stimulus': beep,
                    'timestamp': timestamp,
                    'order': ", ".join(stimulus_order)
                })

            # How long to wait in between each stimulus
            core.wait(5)

    administered_stimuli_df = pd.concat([patient_df, pd.DataFrame(administered_stimuli)], ignore_index=True)
    administered_stimuli_df.to_csv("patient_df.csv", index=False)
