#!/usr/bin/env python
# -*- coding: utf-8 -*- 
################################################################################
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
File: conversation_server.py
"""
 
import sys
sys.path.append('/root/knowledge-driven-dialogue/generative_pt/')
import os
os.chdir('/root/knowledge-driven-dialogue/generative_pt/')
import socket
from _thread import start_new_thread
from tools.conversation_strategy import load
from tools.conversation_strategy import predict

 

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8601

print("starting conversation server ...")
print("binding socket ...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind socket to local host and port
try:
    s.bind((SERVER_IP, SERVER_PORT))
except socket.error as msg:
    print("Bind failed. Error Code : " + str(msg[0]) + " Message " + msg[1])
    exit()
#Start listening on socket
s.listen(10)
print("bind socket success !")

print("loading model...")
model = load()
print("load model success !")

print("start conversation server success !")

def main():

    for line in open(sys.argv[1]):
        param = line.strip()
        logstr += "\tparam:" + param 
        if param is not None:
            response = predict(model, param.strip())
            logstr += "\tresponse:" + response 
        print(logstr + "\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nExited from the program ealier!")
