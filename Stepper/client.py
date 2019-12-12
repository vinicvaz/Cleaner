import socket
import time
import re
import os


class Client_Class:

	def __init__(self):
		## Connection
		self.host = "10.0.0.102"
		self.port = 7000
		self.dest = (self.host,self.port)
		self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcp.connect(self.dest)

		self.data = ''

		### File Init ###
		self.path = '//home//vinicius//Temp_Client//temp_client.txt'
		header = 'speed/distance/y/x/z\n'
		self.file = open(self.path,'w+')  ## Open file to write (and overwrites)
		self.file.write(header) ## Write the header on file
		self.file.close() ## Closes file

	def client_socket(self):

		self.file = open(self.path, 'a+')

		while True:
			self.data = self.tcp.recv(1024)
			self.data = self.data.decode('unicode_escape')
			self.data = self.data.strip()

			if re.match(r'-?[0-9]{1,2}.?[0-9]{0,2}\/[0-9]{1,3}.{0,1}[0-9]{0,2}\/((-{1})?([0-9]{1,3}[.][0-9]{1,2})\/{1}(-{1})?([0-9]{1,3}[.][0-9]{1,2})\/{1}(-{1})?([0-9]{1,3}[.][0-9]{1,2}))', 
				self.data) and len(self.data)<=31:
				self.file.write(self.data)
				self.file.write('\n')
				print(self.data)





client = Client_Class()
client.client_socket()

client.tcp.close()


