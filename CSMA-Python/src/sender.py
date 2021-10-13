'''Sender Module for packet sending based on chosen CSMA technique'''

import sys
import time
import const
import random
import threading
from gen_packet import Packet
from datetime import datetime


class Sender:
    '''Sender Class to implement packet sending functionalities'''

    def __init__(self, name:int, file_name:str, sender_to_channel, channel_to_sender, collision_technique:int):
        self.start               = 0
        self.seq_no              = 0
        self.pkt_count           = 0
        self.collision_count     = 0
        self.busy                = False
        self.end_transmitting    = False
        self.recent_packet       = None
        self.name                = name
        self.file_name           = file_name
        self.sender_to_channel   = sender_to_channel
        self.channel_to_sender   = channel_to_sender
        self.collision_technique = collision_technique
        self.packet_type         = {'data' : 0, 'ack' : 1}
        self.dest                = self.select_receiver()
        self.timeout_event       = threading.Event()
        self.now                 = datetime.now()


    def select_receiver(self):
        '''Selects which receiver to send packet to'''
        return self.name


    def open_file(self, file_name):
        '''Opens file in read mode and returns file-pointer-object'''
        try:
            self.now = datetime.now()
            curr_datetime = self.now.strftime("%d/%m/%Y %H:%M:%S")
            file = open(file_name, 'r', encoding='utf-8')
        except FileNotFoundError as fnfe:
            print(curr_datetime + " EXCEPTION CAUGHT : " + str(fnfe))
            sys.exit("File with name {} is not found!".format(file_name))
        return file


    def send_data_with_one_persistent(self, packet):
        '''Sends packet with One-persistent CSMA technique'''
        while True:
            if self.busy == False:
                file = self.open_file("textfiles/collision.txt")
                collision = file.read()
                file.close()

                if collision == '1':
                    self.collision_count += 1
                    self.now = datetime.now()
                    curr_datetime = self.now.strftime("%d/%m/%Y %H:%M:%S")
                    with open('textfiles/report.txt', 'a+', encoding='utf-8') as rep_file:
                        rep_file.write(curr_datetime + " SENDER-{}    ||  COLLISION".format(self.name+1) + '\n')
                    time.sleep(const.collision_wait_time)
                else:
                    self.now = datetime.now()
                    curr_datetime = self.now.strftime("%d/%m/%Y %H:%M:%S")
                    with open('textfiles/report.txt', 'a+', encoding='utf-8') as rep_file:
                        rep_file.write(curr_datetime + " SENDER-{}    ||  PACKET {} SENT TO CHANNEL".format(self.name+1, self.pkt_count+1) + '\n')
                    file = open('textfiles/collision.txt', "w", encoding='utf-8')
                    file.write(str(1))
                    file.close()
                    time.sleep(const.vulnerable_time)
                    file = open('textfiles/collision.txt', "w",  encoding='utf-8')
                    file.write(str(0))
                    file.close()
                    self.sender_to_channel.send(packet) 
                    time.sleep(const.propagation_time)
                    break

            else:
                self.now = datetime.now()
                curr_datetime = self.now.strftime("%d/%m/%Y %H:%M:%S")
                with open('textfiles/report.txt', 'a+', encoding='utf-8') as rep_file:
                    rep_file.write(curr_datetime + " SENDER-{}    ||  FOUND CHANNEL BUSY".format(self.name+1) + '\n')
                time.sleep(0.5)
                continue


    def send_data_with_non_persistent(self, packet):
        '''Sends packet with Non-persistent CSMA technique'''
        while True:
            if self.busy == False:
                file = self.open_file("textfiles/collision.txt")
                collision = file.read()
                file.close()

                if collision == '1':
                    self.collision_count += 1
                    self.now = datetime.now()
                    curr_datetime = self.now.strftime("%d/%m/%Y %H:%M:%S")
                    with open('textfiles/report.txt', 'a+', encoding='utf-8') as rep_file:
                        rep_file.write(curr_datetime + " SENDER-{}    ||  COLLISION".format(self.name+1) + '\n')
                    time.sleep(const.collision_wait_time)
                else:
                    self.now = datetime.now()
                    curr_datetime = self.now.strftime("%d/%m/%Y %H:%M:%S")
                    with open('textfiles/report.txt', 'a+', encoding='utf-8') as rep_file:
                        rep_file.write(curr_datetime + " SENDER-{}    ||  PACKET {} SENT TO CHANNEL".format(self.name+1, self.pkt_count+1) + '\n')
                    file = open('textfiles/collision.txt', "w",  encoding='utf-8')
                    file.write(str(1))
                    file.close()
                    time.sleep(const.vulnerable_time)
                    file = open('textfiles/collision.txt', "w",  encoding='utf-8')
                    file.write(str(0))
                    file.close()
                    self.sender_to_channel.send(packet)
                    time.sleep(const.propagation_time)
                    break

            else:
                self.now = datetime.now()
                curr_datetime = self.now.strftime("%d/%m/%Y %H:%M:%S")
                with open('textfiles/report.txt', 'a+', encoding='utf-8') as rep_file:
                    rep_file.write(curr_datetime + " SENDER-{}    ||  FOUND CHANNEL BUSY".format(self.name+1) + '\n')
                time.sleep(const.non_persistant_waiting_time)
                continue


    def send_data_with_p_persistent(self, packet):
        '''Sends packet with P-persistent CSMA technique'''
        while True:
            if self.busy == False:
                prob = random.random()
                p = 1/(const.total_sender_number)

                if prob <= p:
                    file = self.open_file("textfiles/collision.txt")
                    collision = file.read()
                    file.close()

                    if collision == '1':
                        self.collision_count += 1
                        self.now = datetime.now()
                        curr_datetime = self.now.strftime("%d/%m/%Y %H:%M:%S")
                        with open('textfiles/report.txt', 'a+', encoding='utf-8') as rep_file:
                            rep_file.write(curr_datetime + " SENDER-{}    ||  COLLISION OCCURED".format(self.name+1) + '\n')
                        time.sleep(const.collision_wait_time)
                    else:
                        self.now = datetime.now()
                        curr_datetime = self.now.strftime("%d/%m/%Y %H:%M:%S")
                        with open('textfiles/report.txt', 'a+', encoding='utf-8') as rep_file:
                            rep_file.write(curr_datetime + " SENDER-{}    ||  PACKET {} SENT TO CHANNEL".format(self.name+1, self.pkt_count+1) + '\n')
                        file = open('textfiles/collision.txt', "w",  encoding='utf-8')
                        file.write(str(1))
                        file.close()
                        time.sleep(const.vulnerable_time)
                        file = open('textfiles/collision.txt', "w",  encoding='utf-8')
                        file.write(str(0))
                        file.close()
                        self.sender_to_channel.send(packet) 
                        time.sleep(const.propagation_time)
                        break

                else:
                    self.now = datetime.now()
                    curr_datetime = self.now.strftime("%d/%m/%Y %H:%M:%S")
                    with open('textfiles/report.txt', 'a+', encoding='utf-8') as rep_file:
                        rep_file.write(curr_datetime + " SENDER-{}    ||  WAITING".format(self.name+1) + '\n')
                    time.sleep(const.time_slot)

            else:
                self.now = datetime.now()
                curr_datetime = self.now.strftime("%d/%m/%Y %H:%M:%S")
                with open('textfiles/report.txt', 'a+', encoding='utf-8') as rep_file:
                    rep_file.write(curr_datetime + " SENDER-{}    ||  FOUND CHANNEL BUSY".format(self.name+1) + '\n')
                time.sleep(0.5)
                continue


    ############################################################################
    # This function is responsible for maintaining sender to channel packet flow
    ############################################################################
    def data_into_frames(self):
        '''Reads data from input file, generates packet, sends to channel based on the CSMA 
        technique chosen, also generates report (Delay, Collisions, Throughput) for each Sender'''
        self.now = datetime.now()
        curr_datetime = self.now.strftime("%d/%m/%Y %H:%M:%S")
        with open('textfiles/report.txt', 'a+', encoding='utf-8') as rep_file:
            rep_file.write(curr_datetime + " SENDER-{} starts sending data to RECEIVER{}".format(self.name+1, self.dest+1) + '\n')
        self.start = time.time()
        file = self.open_file(self.file_name)
        byte = file.read(const.default_datapacket_size)
        self.seq_no = 0
        while byte:
            packet = Packet(self.packet_type['data'], self.seq_no, byte, self.name, self.dest).make_pkt()
            self.recent_packet = packet
            if self.collision_technique == 1: self.send_data_with_one_persistent(packet)
            elif self.collision_technique == 2: self.send_data_with_non_persistent(packet)
            else: self.send_data_with_p_persistent(packet)
            self.pkt_count += 1
            byte = file.read(const.default_datapacket_size)
            if len(byte) == 0: break
            if len(byte) < const.default_datapacket_size:
                temp_length = len(byte)
                for _ in range(const.default_datapacket_size - temp_length): byte += '\0'

        self.end_transmitting = True
        file.close()
        self.now = datetime.now()
        curr_datetime = self.now.strftime("%d/%m/%Y %H:%M:%S")
        with open('textfiles/report.txt', 'a+', encoding='utf-8') as rep_file:
            rep_file.write("\n\n********************** {} SENDER-{} HAS SENT ALL ITS PACKETS **********************".format(curr_datetime, self.name+1) + '\n\n')

        with open('textfiles/analysis.txt', 'a+', encoding='utf-8') as rep_file:
            rep_file.write("\n\n********** {} SENDER-{} STATS **********".format(curr_datetime, self.name+1) + '\n' + \
                            "*\tTotal packets: {}".format(self.pkt_count) + '\n' + \
                            "*\tTotal Delay: {} secs".format(round(time.time() - self.start, 2)) + '\n' + \
                            "*\tTotal collisions: {}".format(self.collision_count) + '\n' + \
                            "*\tThroughput: {}".format(round(self.pkt_count/(self.pkt_count + self.collision_count), 3)) + '\n' + \
                            "********************************************************\n\n" + '\n')


    def sense_signal(self):
        '''Senses the channel and decides wheather it is currently BUSY or FREE'''
        while True:
            if self.channel_to_sender.recv() == '1': self.busy = True
            else: self.busy = False


    #####################################################################
    # This function operates on each Sender-Object (from Sender-List)
    #####################################################################
    def initiate_sender_process(self):
        '''Initializes and terminates the sending thread and receiving thread'''
        sending_thread = threading.Thread(name="sending_thread", target=self.data_into_frames)
        receiving_signal_thread = threading.Thread(name="receiving_signal_thread", target=self.sense_signal)

        sending_thread.start()
        receiving_signal_thread.start()

        sending_thread.join()
        receiving_signal_thread.join()
