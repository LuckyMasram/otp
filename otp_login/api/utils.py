import random

def send_otp(mobile_number):
    if mobile_number:
        key = random.randint(100000,999999)
        return key
    else:
        return False
