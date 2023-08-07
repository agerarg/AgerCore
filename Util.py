import re
from Init import *
import threading
def remove_special_characters(input_string):
    cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
    return cleaned_string

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, email):
        return True
    else:
        return False
    
def send_message(client_socket, response):
    response+=CALL_MULTYLINE
    try:
        client_socket.sendall(response.encode())
    finally:
        pass

triggerEvery10Sec = []  
def triggerEvery10Seconds():
    threading.Timer(10, triggerEvery10Seconds).start()
    for fnc in triggerEvery10Sec:
        fnc()
    