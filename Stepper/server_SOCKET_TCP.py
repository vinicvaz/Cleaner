import socket
import serial 
import threading


class Server_Socket:

	def __init__(self):
		self.ser = serial.Serial('/dev/ttyUSB0',19200)
		self.host = '' 
		self.port = 7000 
		self.addr = (self.host, self.port) 

		self.serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
		self.serv_socket.bind(self.addr)

		print ('Waiting for conection')
		self.serv_socket.listen(1)
		self.con, self.address = self.serv_socket.accept() 

	def handler(self):
		#print ('aguardando conexao')
		#self.serv_socket.listen(1)
		#self.con, self.addr = self.serv_socket.accept()
		print('Sending Gyro/Accel Data')
		while True:

			#print(self.ser.readline().decode('unicode_escape'))
			self.con.send(self.ser.readline())

		self.serv_socket.close()

