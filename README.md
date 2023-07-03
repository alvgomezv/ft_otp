# ft_otp

ft_otp is a Time-based One-time Password generator developed in Python. It provides functionality to save keys, generate one-time passwords, and display them using both the ft_otp and Pyotp libraries.

## Features

- Displays a graphical interface
- Generate an encrypted password from an existing hex key file, the file must contain a hexadecimal key of at least 64 characters
- Generate one-time passwords using the encrypted hex key file
- Display generated one time passwords with ft_otp and Pyotp to compare results
- Create a QR code for the generated key, valid for many OTP apps

## Prerequisites

Before running the program, ensure you have the following dependencies installed:

- Python
- PySimpleGUI
- pyotp
- cryptography
- qrcode

You can install the dependencies using the following command:

`pip install -r requirements.txt`

## Usage

Run the `ft_otp.py` script to launch the graphical interface. The interface provides two main sections:

### Save key from file

This section allows you to save a hex key from a file to another file encrypted called `ft_otp.key.

- Input the path to the hex key file to create an encrypted password.
- Click the **Save Key** button to save the key. The program will encrypt the key and save it in the `ft_otp.key` file.
- The result of the operation will be displayed below the button.

### Generate one-time password

This section enables you to generate one-time passwords using an OTP key file.

- Input the path to the OTP key file, issuer name, account name, and the password for key decryption.
- Click the **Create Token** button to generate a token.
- The result of the operation will be displayed below the button.
- The generated ft_otp token and Pyotp token will be displayed in the interface.
- A QR code for the generated key will be shown in the interface.

### Exit

You can exit the program by clicking the **Exit** button or closing the window.




