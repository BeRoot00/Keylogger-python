# Keylogger

This is a simple keylogger written in Python that captures keyboard inputs and sends them via email. It uses the `pynput.keyboard` library for key event handling and the `smtplib` library for email sending.

## Features

- Captures keyboard inputs and logs them
- Configurable time interval for sending emails
- Handles special keys and spaces
- Sends the captured logs via email

## Installation

1. Clone the repository or download the source code.

2. Install the required dependencies using pip3: pynput threading smtplib

## Give your mail adresse

Provide your email address and password in the app.py file to retrieve the information collected in your mailbox.

## Run the app
```bash
        python3 app.py
```
You will need to "Allow less secure app" on your email address account
## Usage

The keylogger will automatically start capturing keyboard inputs and sending logs via email. The logs are sent periodically at a configurable time interval.

## Disclaimer

**Please note that this keylogger is intended for educational and informational purposes only. The use of this software to capture keyboard inputs and access personal information without proper authorization is strictly prohibited.**

By using this keylogger, you acknowledge and agree that:

- You will only use this software on your own devices or with explicit permission from the device owner.
- You understand that capturing and accessing sensitive information without proper authorization is a violation of privacy laws and regulations.
- You assume all responsibility and liability for any actions taken using this software.
- The author and contributors of this software are not responsible for any misuse or damage caused by the use of this software.
- You will use this software in compliance with applicable laws and regulations governing your jurisdiction.

Please use this keylogger responsibly, respecting the privacy and legal rights of others.

