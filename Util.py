import re
from Init import *
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
    client_socket.sendall(response.encode())
    
