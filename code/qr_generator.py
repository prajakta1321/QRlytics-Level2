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
    # create a qRcode object with configuration
    qr = qrcode.QRCode(
        version = None,    # automatically determines QR size based on input length.
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # error_correct_M allows ~15% of qr to be damaged but still readable
        box_size=10,        # the size of each small box in the qr grid.
        border = 4,)        # thickness of white border around qr(standard = 4)
    
    qr.add_data(data)       # add user_input data to qr object
    qr.make(fit=True)       # generate qr layout (fit=True adjusts size automatically)

    img = qr.make_image(fill_color = fill_color, back_color=back_color)   # convert qr object into an actual image

    # create unqiue filenames into date and time
    filename = f"qr_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    img.save(filename)  # save image file in current directory
    return filename     # return the filename so main.py can display it
