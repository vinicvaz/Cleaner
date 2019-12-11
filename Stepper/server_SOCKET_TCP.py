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

		print ('aguardando conexao')
		self.serv_socket.listen(1)
		self.con, self.address = self.serv_socket.accept() 

	def handler(self):
		#print ('aguardando conexao')
		#self.serv_socket.listen(1)
		#self.con, self.addr = self.serv_socket.accept()
		print('enviando os dados :')
		while True:

			#print(self.ser.readline().decode('unicode_escape'))
			self.con.send(self.ser.readline())

		self.serv_socket.close()


'''
def server_socket():
	ser = serial.Serial('/dev/ttyUSB0',19200)

	host = '' 
	port = 7000 
	addr = (host, port) 

	serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
	serv_socket.bind(addr) 

	print ('aguardando conexao')
	serv_socket.listen(1)
	con, addr = serv_socket.accept()
	print('enviando os dados :')
	while True:
		print(ser.readline().decode('unicode_escape'))
		con.send(ser.readline())

	serv_socket.close()
'''