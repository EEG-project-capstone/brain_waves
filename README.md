# EEG_ML_2024
Peter Schwab Capstone Project CHEM E 546: Coma Outcomes

# User stories
The user is a medical doctor in a hospital. They have a patient in a comatose state and would like to determine the patient's level of consciousness/prognosis to make the best healthcare decisions for this patient. They know that there is a wide range of outcomes for coma patients, ranging from full recovery with no long term effects to serious disabilities or failure to regain consciousness. The doctor needs a systematic approach to discern the severity of the patient's case based on EEG responses to uniform, randomized auditory or tactile perturbations. They will use the software to input patient EEG data and will recieve a numerical probability score of likelihood outof 100 that the patient will regain consciousness.

# Use-cases
The user (a clinical research technician) wants to administer a defined stimulation protocol on a newly admitted comatose patient who has recently experienced a myocardial infarction. The patient has been connected to an EEG. The user runs the stimulus software developed by our group, which outputs complete sentences, as well as commands. The software syncs the outputs to the recorded EEG data for downstream processing and determination of potential patient prognosis. 

The user (a clinical research technician) wants to administer a defined stimulation protocol on a comatose patient. However, they do not know that the protocol has already been run that day on this patient. When they input the patient ID, the program returns an error explaining that the patient has already had this test administered on that day, thus preventing a protocol run which could return data not representative of the patient’s true cognitive state due to not returning to baseline.

# Design components
## (1) Stimulus protocol
This includes 3 types of stimuli presented to patients in a random order to control for biases, as well as for comparison between stimuli to determine if they correlate with different recoveries. Two stimuli are verbal, including a stream or words in recorded spoken commands. The remaining stimulus is a tactile test for reactivity. Primary questions that this protocol may answer is whether these paradigms are measuring different parts of patient recovery. *we are thinking we will not continue with the tactile stimuli since it is difficult to automate and would require more assistance from technicians which adds a layer of complexity

### Inputs (with type information)
Inputs include identifier information (strings) that will be used to connect EEG recordings with details of type/duration of stimuli provided and eventually connect patient outcome to EEG data

### Outputs
Randomly generated audio files that are played from computer
Storing of audio file words in a dictionary to retrieve upon request

### How it uses other components

### Side effects

## (2) Analysis pipeline software
The stimulus protocol will contain a method for providing a consistent signal that the EEG machine can recognize; thus, all timing can be synched between the EEG signal to the laptop stimulus. The analysis pipeline identifies the start and end of the stimulus for determining the impact of each stimulus on the patient.
