import unittest
from unittest.mock import patch, MagicMock, ANY
import brain_waves_packages
from brain_waves_packages.stimulus_package3 import administer_sentence, administer_word, administer_beep
from brain_waves_packages.stimulus_package3 import get_random_stimulus_order, generate_and_play_stimuli

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

    @patch('os.remove')
    @patch('os.path.exists', return_value=True)
    def test_file_creation(self, mock_exists, mock_remove):

        sentence_list = ['test_sentence']
        sentence, _ = administer_sentence(sentence_list)

        mock_exists.assert_called_once_with('temp_sentence.mp3')
        mock_remove.assert_called_once_with('temp_sentence.mp3')

class TestAdministerWord(unittest.TestCase):

    @patch('random.choice')
    def test_random_sentence_selection(self, mock_choice):
        mock_choice.return_value = 'test_word'
        result, _ = administer_word(['test_word'])
        self.assertEqual(result, 'test_word')

    @patch('time.time', return_value=1717178400.0)
    def test_timestamp(self, mock_time):
        _, timestamp = administer_word(['test_word'])
        self.assertEqual(timestamp, 1717178400.0)

    @patch('os.remove')
    @patch('os.path.exists', return_value=True)
    def test_file_creation(self, mock_exists, mock_remove):

        sentence_list = ['test_word']
        sentence, _ = administer_word(sentence_list)

        mock_exists.assert_called_once_with('temp_word.mp3')
        mock_remove.assert_called_once_with('temp_word.mp3')

class TestAdministerBeep(unittest.TestCase):

    @patch('time.time', return_value=1717178400.0)
    def test_timestamp(self, mock_time):
        _, timestamp = administer_beep()
        self.assertEqual(timestamp, 1717178400.0)

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
