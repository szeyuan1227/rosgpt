#!/usr/bin/env python3
# This file is part of rosgpt package.
#
# Copyright (c) 2023 Anis Koubaa.
# All rights reserved.
#
# This work is licensed under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
# International Public License. See https://creativecommons.org/licenses/by-nc-sa/4.0/ for details.


import json
import requests

def send_text_command(text_command):
    """
    Sends a text command to the ROSGPT system and receives a response from the ChatGPT language model.
    
    Parameters:
        text_command (str): The natural language text command to be processed by the ROSGPT system.
        
    Returns:
        None
    """
    data = {'text_command': text_command}
    response = requests.post('http://localhost:5000/rosgpt', data=data)
    
    if response.status_code == 200:
        response_str = response.content.decode('utf-8')
        #print(response_str)
        try:
            response_dict = json.loads(response_str)
            #print(response_dict)
            print("\nResponse:", response_dict['text'])
            print("\nJSON:", json.loads(response_dict['json']))
        except json.JSONDecodeError:
            print('[json.JSONDecodeError] Invalid or empty JSON string received:', response_dict)
        except Exception as e:
            print('[Exception] An unexpected error occurred:', str(e)) 
    else:
        print("Error:", response.status_code)


if __name__ == '__main__':
    """
    This script allows the user to input a text command, which is sent to the ROSGPT system
    using the send_text_command() function. The response generated by ChatGPT is printed
    to the console.
    """
    while True:
        print('Enter a move command or a rotate command.')
        text_command = input("Enter a text command: ")
        send_text_command(text_command)
