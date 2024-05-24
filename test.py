import unittest
from unittest.mock import patch, MagicMock
import streamlit as st

#testing the gui here:
# Import the main function to test
from main import start_stimulus

class TestStartStimulus(unittest.TestCase):

    @patch('main.st')
    @patch('main.generate_and_play_sentences')
    @patch('main.update_patient_dict')
    def test_start_stimulus_success(self, mock_update_patient_dict, mock_generate_and_play_sentences, mock_st):
        # Mocking the return value of generate_and_play_sentences
        mock_generate_and_play_sentences.return_value = (None, {"sentence1": "This is a test sentence."})

        # Mocking streamlit functions
        mock_st.empty.return_value = MagicMock()

        patient_id = "test_patient"
        num_sentences = 5

        start_stimulus(num_sentences, patient_id)

        # Assertions to check if streamlit functions were called correctly
        mock_st.error.assert_not_called()
        mock_st.success.assert_called_once_with("Stimulus protocol successfully administered.")
        mock_st.empty().write.assert_any_call("Administering Stimulus...")
        mock_st.empty().write.assert_any_call("Stimulus is running...")
        mock_st.empty().empty.assert_any_call()

        # Assertions to check if the mocked functions were called with the right parameters
        mock_generate_and_play_sentences.assert_called_once_with(num_sentences=num_sentences, patient_id=patient_id)
        mock_update_patient_dict.assert_called_once_with(patient_id, {"sentence1": "This is a test sentence."})

    @patch('main.st')
    @patch('main.generate_and_play_sentences')
    @patch('main.update_patient_dict')
    def test_start_stimulus_empty_patient_id(self, mock_update_patient_dict, mock_generate_and_play_sentences, mock_st):
        patient_id = ""
        num_sentences = 5

        start_stimulus(num_sentences, patient_id)

        # Assertions to check if streamlit error message is displayed
        mock_st.error.assert_called_once_with("Please enter a patient ID.")

        # Assertions to check if other functions are not called
        mock_generate_and_play_sentences.assert_not_called()
        mock_update_patient_dict.assert_not_called()
        mock_st.success.assert_not_called()

    @patch('main.st')
    @patch('main.generate_and_play_sentences')
    @patch('main.update_patient_dict')
    def test_start_stimulus_generate_and_play_sentences_failure(self, mock_update_patient_dict, mock_generate_and_play_sentences, mock_st):
        # Mocking the generate_and_play_sentences to raise an exception
        mock_generate_and_play_sentences.side_effect = Exception("An error occurred during sentence generation.")

        # Mocking streamlit functions
        mock_st.empty.return_value = MagicMock()

        patient_id = "test_patient"
        num_sentences = 5

        with self.assertRaises(Exception) as context:
            start_stimulus(num_sentences, patient_id)

        self.assertTrue("An error occurred during sentence generation." in str(context.exception))

        # Assertions to check if streamlit functions were called correctly
        mock_st.error.assert_not_called()
        mock_st.success.assert_not_called()

        # Assertions to check if the mocked functions were called with the right parameters
        mock_generate_and_play_sentences.assert_called_once_with(num_sentences=num_sentences, patient_id=patient_id)
        mock_update_patient_dict.assert_not_called()

if __name__ == '__main__':
    unittest.main()
