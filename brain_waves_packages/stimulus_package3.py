import os
import time
import random
import pandas as pd
from gtts import gTTS
from psychopy import sound, core
import psychtoolbox as ptb

def administer_sentence(sentence_list):

    # Initialize word to be played by gTTS
    sentence = random.choice(sentence_list)

    # Get timestamp of when word is played
    timestamp = time.time()
    
    # Initialize gTTS and play the sentence audio
    tts = gTTS(text=sentence, lang="en")
    tts.save("temp_sentence.mp3")
    sentence_sound = sound.Sound("temp_sentence.mp3")
    now = ptb.GetSecs()
    sound.Sound.play(sentence_sound, when=now)

    # Delete intermediate mp3 file
    if os.path.exists("temp_sentence.mp3"):
        os.remove("temp_sentence.mp3")

    return sentence, timestamp

def administer_word(word_list):

    # Initialize word to be played by gTTS
    word = random.choice(word_list)

    # Get timestamp of when word is played
    timestamp = time.time()
    
    # Initialize gTTS and play the sentence audio
    tts = gTTS(text=word, lang="en")
    tts.save("temp_word.mp3")
    word_sound = sound.Sound("temp_word.mp3")
    now = ptb.GetSecs()
    sound.Sound.play(word_sound, when=now)

    # Delete intermediate mp3 file
    if os.path.exists("temp_word.mp3"):
        os.remove("temp_word.mp3")

    return word, timestamp

def administer_beep(frequency=1000, duration=0.5):

    # Get timestamp of when beep will play
    timestamp = time.time()
    
    # Initialize sound
    beep_sound = sound.Sound(value=frequency, secs=duration)
    now = ptb.GetSecs()
    sound.Sound.play(beep_sound, when=now)

    return "BEEP", timestamp

def get_random_stimulus_order():
    stimuli = ["sentence", "word", "beep"]
    random.shuffle(stimuli)
    return stimuli

def generate_and_play_stimuli(patient_id="patient0"):

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