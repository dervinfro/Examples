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


account_sid = 'enter_account_id'
auth_token = 'enter_auth_id'

client = Client(account_sid, auth_token)

    #%%

client.messages.create(from_='+1<from_number>',
                       to='+1<to_number>',
                       body='You just sent an SMS from Python using Twilio!')
#%%
