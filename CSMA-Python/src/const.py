'''module for assiging values to variables that remain constant throughout the flow during execution'''

import random


total_sender_number = 9
total_receiver_number = 9
default_datapacket_size = 46


####################################
# sender constants
####################################
time_slot = 0.25
propagation_time = 1            # sender remains busy this time
vulnerable_time = 0.1           # data length / bandwidth
collision_wait_time = 0.1
non_persistant_waiting_time = random.randint(1, 4)


####################################
# receiver constants
####################################
input_file_path = "./textfiles/input/"
outfile_path = "./textfiles/output/"


####################################
# channel constants
####################################
channel_propagation_time = 0.8  # channel remains busy this time
