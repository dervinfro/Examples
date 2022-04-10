#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 22:58:12 2022

@author: derekfrost
"""

import smtplib
import time

#%% Variables

#################################################
### Port, Server, Email addresses and Message ###
#################################################

# All of the server, ports, emails need to be outside of the function
port = 465
smtp_server = "smtp.gmail.com"
sender_email = "dfrewards1@gmail.com"
rec_email = "devifr@gmail.com"
password = r"Certainty-Bloomers6-Unblock-Grunt-Magnetism"
current_time = time.asctime()
message = f"""\
Subject: Test - {current_time}

A test message: {current_time}  """

#%%
def email_api_status():
    ###################################################
    ### SSL Connection and Server Login & Sendemail ###
    ###################################################
    
    with smtplib.SMTP_SSL(smtp_server) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, rec_email, message)
        # server.set_debuglevel(1)
#%%

email_api_status()
    
