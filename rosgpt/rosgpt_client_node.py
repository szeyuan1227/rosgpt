#!/usr/bin/env python3
# This file is part of rosgpt package.
#
# Copyright (c) 2023 Anis Koubaa.
# All rights reserved.
#
# This work is licensed under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
# International Public License. See https://creativecommons.org/licenses/by-nc-sa/4.0/ for details.

import json
import rclpy
from rclpy.node import Node
import requests
import speech_recognition as sr


class ROSGPTClient(Node):
    def __init__(self):
        super().__init__('rosgpt_client')
        self.declare_parameter('server_url', 'http://localhost:5000/rosgpt')
        self.server_url = self.get_parameter('server_url').value

        self.get_logger().info('ROSGPT client node started')

        self.send_text_command()
        # self.get_voice_command()

    # def get_voice_command():
    #     """
    #     Prompts the user for a voice command and converts it to text using SpeechRecognition.
    #     """
    #     recognizer = sr.Recognizer()
    #     with sr.Microphone() as source:
    #         print("Speak your command:")
    #         audio = recognizer.listen(source)
    #     try:
    #         text_command = recognizer.recognize_google(audio)
    #         print("You said: " + text_command)
    #         return text_command
    #     except sr.UnknownValueError:
    #         print("Sorry, I could not understand audio")
    #     except sr.RequestError as e:
    #         print("Could not request results from Google Speech Recognition service; {0}".format(e))
    #     return None

    #     # Example usage within send_text_command:
    #     while rclpy.ok():
    #         text_command = get_voice_command()
    #         data = text_command
    #         response = requests.post(self.server_url, data=data)
    #         if response.status_code == 200:
    #             try:
    #                 response_str = response.content.decode('utf-8')
    #                 response_dict = json.loads(response_str)

    #                 self.get_logger().info('Response: {}'.format(response_dict['text']))
    #                 self.get_logger().info('JSON: {}'.format(json.loads(response_dict['json'])))
    #             except Exception as e:
    #                 print('[Exception] An unexpected error occurred:', str(e)) 
    #         else:
    #             self.get_logger().error('Error: {}'.format(response.status_code))
            


    def send_text_command(self):
        """
        Sends a text command to the ROSGPT system and receives a response from the ChatGPT language model.
        """
        while rclpy.ok():
            print('Enter a move command or a rotate command.')
            text_command = input("Enter a text command: ")
            data = {'text_command': text_command}

            response = requests.post(self.server_url, data=data)

            if response.status_code == 200:
                try:
                    response_str = response.content.decode('utf-8')
                    response_dict = json.loads(response_str)

                    self.get_logger().info('Response: {}'.format(response_dict['text']))
                    self.get_logger().info('JSON: {}'.format(json.loads(response_dict['json'])))
                except Exception as e:
                    print('[Exception] An unexpected error occurred:', str(e)) 
            else:
                self.get_logger().error('Error: {}'.format(response.status_code))


def main(args=None):
    rclpy.init(args=args)

    rosgpt_client = ROSGPTClient()

    rclpy.spin(rosgpt_client)

    rosgpt_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
