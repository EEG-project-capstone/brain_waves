import unittest
import stimulus_package 
import json

# Defining a global variable for how many tests to run
num_tests = 2

class test_generate_and_play_sentences(unittest.TestCase):

    # Testing that all sentences in the out put sentences are strings
    def test_generate_sentence(self):
        for x in range(num_tests):
            out_id, out_dict = stimulus_package.generate_and_play_sentences(x+1, x+1)
            for sent in out_dict.values():
                self.assertTrue(type(sent)==str)

    # Testing that the patient ID that is returned is the same as the one that is inputted    
    def test_correct_patientID(self):   
        for x in range(num_tests):
            out_id, out_sentences = stimulus_package.generate_and_play_sentences(x+1, x+1)
            self.assertTrue(x+1==out_id)

    # Testing that the number of sentences in the dictionary is equal to the number of sentences in the input
    def test_num_sentences(self):
        for x in range(num_tests):
            out_id, out_sentences = stimulus_package.generate_and_play_sentences(x+1, x+1)
            self.assertTrue(len(out_sentences)==x+1)

def test_sentence_dict_update():
    # Testing that the dictionary holding the sentences administered to different patients was updated when the test runs.
    num_sentences = 4
    patient_id = "patient123"
    patient_id, administered_sentences_dict = stimulus_package.generate_and_play_sentences(num_sentences, patient_id)
    for timestamp, sentence in administered_sentences_dict.items():
        assert sentence == administered_sentences_dict[timestamp]

class test_update_patient_dict(unittest.TestCase):

    # Testing that sentences are added the correct patient IDs
    def test_correct_patientID(self): 
        for x in range(num_tests):
            out_id, out_sentences = stimulus_package.generate_and_play_sentences(x+1, x+1)
            stimulus_package.update_patient_dict(out_id, out_sentences)
            dict_file = open('patient_dict.json') 
            patient_dict = json.load(dict_file)
            self.assertTrue(str(x+1) in patient_dict)
            dict_file.close()
    
    #test format of the date
    def test_update_patientID(self):
        for x in range(num_tests):
            out_id, out_current_date = stimulus_package.generate_and_play_sentences(x+1, x+1)
            for sent in out_current_date.values():
                self.assertTrue(type(sent)==str)

"""
class test_prompt_user_inputs(unittest.TestCase):
    
        
"""
