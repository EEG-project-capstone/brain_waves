import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
import stimulus_package3

num_tests = 2

class TestGenerateAndPlaySentences(unittest.TestCase):

    @patch('stimulus_package3.gTTS')
    @patch('stimulus_package3.sound.Sound')
    @patch('stimulus_package3.ptb.GetSecs', return_value=0)
    @patch('stimulus_package3.time.time', return_value=1622470427.0)
    def test_generate_sentence(self, mock_time, mock_getsecs, mock_sound, mock_gtts):
        for x in range(num_tests):
            out_id, out_dict = stimulus_package3.generate_and_play_sentences(x + 1, x + 1)
            for sent in out_dict.values():
                self.assertTrue(isinstance(sent, str))

    def test_correct_patientID(self):
        for x in range(num_tests):
            out_id, out_sentences = stimulus_package3.generate_and_play_sentences(x + 1, x + 1)
            self.assertEqual(x + 1, out_id)

    def test_num_sentences(self):
        for x in range(num_tests):
            out_id, out_sentences = stimulus_package3.generate_and_play_sentences(x + 1, x + 1)
            self.assertEqual(len(out_sentences), x + 1)

class TestSentenceDictUpdate(unittest.TestCase):

    @patch('stimulus_package3.gTTS')
    @patch('stimulus_package3.sound.Sound')
    @patch('stimulus_package3.ptb.GetSecs', return_value=0)
    @patch('stimulus_package3.time.time', return_value=1622470427.0)
    def test_sentence_dict_update(self, mock_time, mock_getsecs, mock_sound, mock_gtts):
        num_sentences = 4
        patient_id = "patient123"
        patient_id, administered_sentences_dict = stimulus_package3.generate_and_play_sentences(num_sentences, patient_id)
        for timestamp, sentence in administered_sentences_dict.items():
            self.assertEqual(sentence, administered_sentences_dict[timestamp])

class TestUpdatePatientDict(unittest.TestCase):

    @patch('stimulus_package3.open', new_callable=mock_open, read_data='{}')
    @patch('stimulus_package3.json.load')
    @patch('stimulus_package3.json.dump')
    @patch('stimulus_package3.gTTS')
    @patch('stimulus_package3.sound.Sound')
    @patch('stimulus_package3.ptb.GetSecs', return_value=0)
    @patch('stimulus_package3.time.time', return_value=1622470427.0)
    def test_correct_patientID(self, mock_time, mock_getsecs, mock_sound, mock_gtts, mock_json_dump, mock_json_load, mock_open):
        mock_json_load.return_value = {}
        for x in range(num_tests):
            out_id, out_sentences = stimulus_package3.generate_and_play_sentences(x + 1, x + 1)
            stimulus_package3.update_patient_dict(out_id, out_sentences)
            mock_open.assert_called_with('patient_dict.json')
            handle = mock_open()
            handle.write.assert_called_once()
            mock_json_dump.assert_called_once()

    @patch('stimulus_package3.open', new_callable=mock_open, read_data='{}')
    @patch('stimulus_package3.json.load')
    @patch('stimulus_package3.json.dump')
    @patch('stimulus_package3.gTTS')
    @patch('stimulus_package3.sound.Sound')
    @patch('stimulus_package3.ptb.GetSecs', return_value=0)
    @patch('stimulus_package3.time.time', return_value=1622470427.0)
    def test_update_patientID(self, mock_time, mock_getsecs, mock_sound, mock_gtts, mock_json_dump, mock_json_load, mock_open):
        mock_json_load.return_value = {}
        for x in range(num_tests):
            out_id, out_current_date = stimulus_package3.generate_and_play_sentences(x + 1, x + 1)
            for sent in out_current_date.values():
                self.assertTrue(isinstance(sent, str))

if __name__ == '__main__':
    unittest.main()

