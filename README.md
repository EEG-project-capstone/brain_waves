# EEG_ML_2024
Peter Schwab Capstone Project CHEM E 546: Coma Outcomes

# User stories


# Use-cases:
###Inputs


###Outputs


# Design components
###(1) Stimulus protocol
This includes 3 types of stimuli presented to patients in a random order to control for biases, as well as for comparison betwene stimuli to determine if they correlate with different recoveries. Two stimuli are verbal, including a stream or words in recorded spoken commands. The remaining stimulus is a tactile test for reactivity. Primary questions that this protocol may answer is whether these paradigms are measuring different parts of patient recovery.

###(2) Analysis pipeline software
The stimulus protocol will contain a method for providing a consistent signal that the EEG machine can recognize; thus, all timing can be synched between the EEG signal to the laptop stimulus. The analysis pipeline identifies the start and end of the stimulus for determining the impact of each stimulus on the patient.
