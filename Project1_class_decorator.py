"""
Project: encoded the message with shifting position of alpha 2 step farwared
ex: "jgnnq" --> hello"""

import logging
from os import path

file_path = path.abspath(__file__)
file_folder_path = path.dirname(file_path)
log_file_path = path.join(file_folder_path, "log_file.log")
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(level)s - %(message)s",
)


class encoded_message:
    def __init__(self, data):
        self.data = data
        logging.info("Start the Program")


@encoded_message
def decoded_message(data):
    pass


var = "asf"
temp = list(var)
print(decode("hello"))
# print(chr(ord(var[0]) + 2))
