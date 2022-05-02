#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 23:50:15 2022

@author: derekfrost
"""

# https://www.twilio.com/blog/2016/10/how-to-send-an-sms-with-python-using-twilio.html

import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
import os
from twilio.rest import Client


account_sid = 'AC461e0746b12ba3a1aa62b5642c4886c7'
auth_token = 'b3b10e414b150afc486ca7c797311f29'

client = Client(account_sid, auth_token)

    #%%

client.messages.create(from_='+19593011059',
                       to='+17063154974',
                       body='You just sent an SMS from Python using Twilio!')
#%%
