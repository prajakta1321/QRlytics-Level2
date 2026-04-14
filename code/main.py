from qr_generator import generate_qr               # Import generate_qr function from qr_generator file
from utils import is_valid_url                     # Import URL validation function (used later if needed)

def main():                                        # main function that runs the CLI interface, handles user interaction and calls qr generator
    print("\n Welcome to SmartQR - CLI Version \n")

    data = input("Enter text or URL to generate QR: ").strip()
                                                   # .strip() removes unnecessary spaces from beginning and end
    if not data:                                   # if the user enters nothing
        print("Error: Input cannot be empty.")
        return                                     # stop the execution

