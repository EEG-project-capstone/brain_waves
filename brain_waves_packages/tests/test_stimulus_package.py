import unittest
from unittest.mock import patch, MagicMock, ANY, mock_open, call
import random
import time
import os
from gtts import gTTS
from psychopy import sound
import psychtoolbox as ptb
from stimulus_package3 import administer_sentence, administer_word, administer_beep, get_random_stimulus_order, generate_and_play_stimuli

class TestAdministerSentence(unittest.TestCase):

    @patch('random.choice')
    def test_random_sentence_selection(self, mock_choice):
        mock_choice.return_value = 'test_sentence'
        result, _ = administer_sentence(['test_sentence'])
        self.assertEqual(result, 'test_sentence')

    @patch('time.time', return_value=1717178400.0)
    def test_timestamp(self, mock_time):
        _, timestamp = administer_sentence(['test_sentence'])
        self.assertEqual(timestamp, 1717178400.0)

    @patch('gtts.gTTS')
    @patch('psychopy.sound.Sound')
    @patch('os.remove')
    def test_gtts_and_file_creation(self, mock_remove, mock_Sound, mock_gTTS):
        mock_tts = MagicMock()
        mock_gTTS.return_value = mock_tts
        mock_Sound.return_value = MagicMock()

        sentence_list = ['test_sentence']
        sentence, _ = administer_sentence(sentence_list)

        mock_Sound.assert_called_once_with('temp_sentence.mp3')
        mock_remove.assert_called_once_with('temp_sentence.mp3')

    @patch('psychopy.sound.Sound.play')
    @patch('psychopy.sound.Sound')
    def test_sound_playback(self, mock_Sound, mock_play):
        mock_sound_instance = MagicMock()
        mock_Sound.return_value = mock_sound_instance

        administer_sentence(['test_sentence'])

        mock_Sound.assert_called_once_with('temp_sentence.mp3')
        mock_play.assert_called_once_with(mock_sound_instance, when=ANY)

    @patch('os.path.exists', return_value=True)
    @patch('os.remove')
    def test_file_deletion(self, mock_remove, mock_exists):
        administer_sentence(['test_sentence'])
        mock_exists.assert_called_once_with('temp_sentence.mp3')
        mock_remove.assert_called_once_with('temp_sentence.mp3')

class TestAdministerWord(unittest.TestCase):

    @patch('random.choice')
    def test_random_word_selection(self, mock_choice):
        mock_choice.return_value = 'test_word'
        result, _ = administer_word(['test_word'])
        self.assertEqual(result, 'test_word')

    @patch('time.time', return_value=1717178400.0)
    def test_timestamp(self, mock_time):
        _, timestamp = administer_word(['test_word'])
        self.assertEqual(timestamp, 1717178400.0)

    @patch('gtts.gTTS')
    @patch('psychopy.sound.Sound')
    @patch('os.remove')
    def test_gtts_and_file_creation(self, mock_remove, mock_Sound, mock_gTTS):
        mock_tts = MagicMock()
        mock_gTTS.return_value = mock_tts
        mock_Sound.return_value = MagicMock()

        word_list = ['test_word']
        word, _ = administer_word(word_list)

        mock_Sound.assert_called_once_with('temp_word.mp3')
        mock_remove.assert_called_once_with('temp_word.mp3')

    @patch('psychopy.sound.Sound.play')
    @patch('psychopy.sound.Sound')
    def test_sound_playback(self, mock_Sound, mock_play):
        mock_sound_instance = MagicMock()
        mock_Sound.return_value = mock_sound_instance

        administer_word(['test_word'])

        mock_Sound.assert_called_once_with('temp_word.mp3')
        mock_play.assert_called_once_with(mock_sound_instance, when=ANY)

    @patch('os.path.exists', return_value=True)
    @patch('os.remove')
    def test_file_deletion(self, mock_remove, mock_exists):
        administer_word(['test_word'])
        mock_exists.assert_called_once_with('temp_word.mp3')
        mock_remove.assert_called_once_with('temp_word.mp3')

class TestAdministerBeep(unittest.TestCase):

    @patch('time.time', return_value=1717178400.0)
    def test_timestamp(self, mock_time):
        _, timestamp = administer_beep()
        self.assertEqual(timestamp, 1717178400.0)

    @patch('psychopy.sound.Sound.play')
    @patch('psychopy.sound.Sound')
    def test_sound_initialization_and_playback(self, mock_Sound, mock_play):
        mock_sound_instance = MagicMock()
        mock_Sound.return_value = mock_sound_instance

        beep_text, timestamp = administer_beep(frequency=1000, duration=0.5)

        # Verify the Sound object was created with correct parameters
        mock_Sound.assert_called_once_with(value=1000, secs=0.5)
        # Verify the sound was played with the correct timing
        mock_play.assert_called_once_with(mock_sound_instance, when=ANY)
        # Verify the function return values

class TestGetRandomStimulusOrder(unittest.TestCase):

    @patch('random.shuffle')
    def test_shuffle_called(self, mock_shuffle):
        # Call the function
        result = get_random_stimulus_order()

        # Ensure random.shuffle was called once
        mock_shuffle.assert_called_once()

        # Check that result is a permutation of the original list
        self.assertCountEqual(result, ["sentence", "word", "beep"])

    def test_random_order(self):
        # Create a set to track different orders
        orders = set()
        
        # Run the function multiple times to check different orderings
        for _ in range(100):
            result = get_random_stimulus_order()
            orders.add(tuple(result))
        
        # There are 6 possible permutations of 3 items
        self.assertGreaterEqual(len(orders), 3)
        self.assertLessEqual(len(orders), 6)



if __name__ == '__main__':
    unittest.main()
