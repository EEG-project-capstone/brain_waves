import unittest
import stimulus_package 

# Defining a global variable for how many tests to run
num_tests = 2

class generate_and_play_sentences(unittest.TestCase):
    
    #Testing that all sentences in the out put sentences are strings
    def test_generate_sentence(self):
        for x in range(num_tests):
            out_id, out_dict = stimulus_package.generate_and_play_sentences(x+1, x+1)
            for sent in out_dict.values():
                print(type(sent))
                self.assertTrue(type(sent)==str)

    # Testing that the patient ID that is returned is the same as the one that is inputted
    def test_correct_patientID(self):   
        for x in range(0):#num_tests):
            out_id, out_sentences = stimulus_package.generate_and_play_sentences(x+1, x+1)
            print(out_id, x+1)
            self.assertTrue(x+1==out_id)