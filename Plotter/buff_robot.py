'''FUNÇÃO : LER E ARMAZENAR OS DADOS DO ACELETROMETRO GIROSCOPIO E SONAR EM UM ARQUIVO
	OS TRÊS DADOS SERÃO PROCESSADOS POR UMA CLASSE QUE CRIARÇÃO UM NOVO ARQUIVO
'''
import random
import time


class buff_robot():
	"""docstring for buff_robot"""
	def __init__(self, accelerometer, gyroscope,sonar):
		self.acce = accelerometer
		self.angle = gyroscope
		self.dist = sonar
	
		file = open("buff_temp.csv", 'w')

		try:
			"""DADOS ALEATORIO SIMULANDO OS SENSORES, SUBSTITUIR POR DADOS VERIDICOS DEPOIS / TIRAR O FOR"""
			for _ in range(36):
				self.acce = self.acce + random.randrange(0,5,1)
				self.angle = self.angle +random.randrange(-5,5,1)
				self.dist = random.randrange(15,25,1)
				file.write("%.2f,%.2f,%.2f\n"% (self.acce,self.angle,self.dist)) ### [ACELERAÇÃO , ANGULO, DISTANCIA SONAR(-1 == ERRO)]
		finally:
			file.close()

	def read_csv():
		file = open('buff_temp.csv', 'r')
		try:
			print(file.read())
		finally:
			file.close()

buff_robot(0,0,0)