import qrcode  # import the QR code library to generate code.
from datetime import datetime  # import datetime to create unique file names using timestamp

def generate_qr(data, fill_color='black', back_color='white'):  # this function generates a QR code image from given data.
    # parameters : data(str): the text or url to encode inside the QR.
    # fill_color (str) : color of the QR pattern.
    # back_color (str) : background color of QR.
    # return : 
    # filename(str) : name of the saved QR image file
    
    
    if not data.strip():             # check if the input is empty or just spaces                                 
        raise ValueError("input cannot be empty.")   # raise error if the user enters empty input.
