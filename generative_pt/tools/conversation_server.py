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



def main():
    print("loading model...")
    model = load()
    print("load model success !")

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
