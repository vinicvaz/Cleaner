import socket
import serial 

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