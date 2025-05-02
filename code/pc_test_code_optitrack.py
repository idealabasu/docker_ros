# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 16:32:58 2023

@author: yjian154
"""
#
# Created on Wed Jul 12 2023
#
# Copyright (c) Yuhao
#

import socket
import numpy as np
import idealab_tools.data_exchange.csv as csv
import sys
import os
import time
from NatNetClient import NatNetClient
#import winsound

ws=os.path.abspath(os.curdir)
folder_name = "result_data"
data_path = os.path.join(ws,folder_name)

if os.path.isdir(data_path):
    print('Data directory found.')
else:
    print('Data directory not found.')
    os.mkdir(data_path)
    print('Successfully created data directory')

beep_frequency = 2500  # Set Frequency To 2500 Hertz
beep_duration = 2000  # Set Duration To 1000 ms == 1 second

# This is a callback function that gets connected to the NatNet client. It is called once per rigid body per frame
def receive_rigid_body_frame( new_id, position, rotation ):
    global pos
    global rot
    pos = position
    rot = rotation

    print( "Received frame for rigid body", new_id," ",position," ",rotation )
    pass


optionsDict = {}
optionsDict["clientAddress"] = "192.168.1.7"
optionsDict["serverAddress"] = "192.168.1.5"
optionsDict["use_multicast"] = False

streaming_client = NatNetClient()
streaming_client.set_client_address(optionsDict["clientAddress"])
streaming_client.set_server_address(optionsDict["serverAddress"])
streaming_client.set_use_multicast(optionsDict["use_multicast"])

# # Configure the streaming client to call our rigid body handler on the emulator to send data out.
streaming_client.rigid_body_listener = receive_rigid_body_frame

# Start up the streaming client now that the callbacks are set up.
# This will run perpetually, and operate on a separate thread.
is_running = streaming_client.run()
if not is_running:
    print("ERROR: Could not start streaming client.")
    try:
        sys.exit(1)
    except SystemExit:
        print("...")
    finally:
        print("exiting")

time.sleep(1)
if streaming_client.connected() is False:
    print("ERROR: Could not connect properly.  Check that Motive streaming is on.")
    try:
        sys.exit(2)
    except SystemExit:
        print("...")
    finally:
        print("exiting")

#Initialize wifi connection with the robot
# bind all IP
#HOST = '192.168.0.173'
# Listen on Port 
#PORT = 8080 
#Size of receive buffer   
#BUFFER_SIZE = 200
# Create a TCP/IP socket
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the host and port
#s.bind((HOST, PORT))

msg_flag = []

#while msg_flag == []:
#    msg_flag = s.recvfrom(BUFFER_SIZE)
#sendingAddress = msg_flag[1]
#print('esp connected, address: {}'.format(sendingAddress))

freq_max = 45

#input("Press Enter to start test when motors are ready")

for freq in range(0,100):
    print('Step frequemcy={} Started'.format(freq))
  #  s.sendto("T{}\n".format(freq).encode(), sendingAddress)
   # s.sendto("T{}\n".format(freq).encode(), sendingAddress)
    optitrack_data = []
#    global pos
#    print(pos)
#    winsound.Beep(beep_frequency, 1000)
    # time.sleep(2)
    #t0 = time.time()
    #t = time.time()
#    while t - t0 <= 5:
    #print('statred collecting data current time: {}'.format(t-t0))
    #t = time.time()
 #       optitrack_data.append([t - t0, pos[0], pos[1], pos[2], rot[0], rot[1], rot[2]])      
        # time.sleep(0.0001)
 #   s.sendto("T0\n".encode(), sendingAddress)
    #Name = os.path.join(data_path, 'walking_test_optitrack_freq{}.csv'.format("{0:0=2d}".format(freq)))
    #csv.write(Name, optitrack_data)
    #print('Step frequemcy={} finished'.format("{0:0=2d}".format(freq)))
#    winsound.Beep(beep_frequency, beep_duration)

#    input("Put back the robot and Press Enter to proceed")

print("Test Finished")
#s.sendto("T0\n".encode(), sendingAddress)
