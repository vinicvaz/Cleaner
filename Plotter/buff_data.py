import time
import random
import csv
import math as m

time = 1 # atualização de 1 segundo

class buff_data():
	"""docstring for buff_data"""
	def __init__(self,):

		read_file = open('buff_temp.csv', 'r')
		write_file = open("buff_data.csv", 'w+')

		data = csv.reader(read_file, delimiter=',')
		data = list(data)
		data= [[float(float(j)) for j in i] for i in data]

		print(type(data[0][0]))
		read_file.close()
		"""#calculos para a primeira interação:
		####velocidade####
		V_i = data[0][0] * time
		V_iy = V_i * m.sin(m.radians(data[0][1]))
		V_ix = V_i * m.cos(m.radians(data[0][1]))
		###posicao######
		S_i = (data[0][0] * time * time)/2
		S_iy = S_i * m.sin(m.radians(data[0][1]))
		S_ix = S_i * m.cos(m.radians(data[0][1]))
		###Distancia sonar####
		if 2>data[0][2]>400:
			#OUT OF RANGE
			D_i = D_ix = D_iy = -1
		else:
			D_i = data[0][2]
			D_iy = data[0][2]*m.sin(m.radians(data[0][1]))
			D_ix = data[0][2]*m.cos(m.radians(data[0][1]))

		write_file.write("%.2f,%.2f,%.2f,%.2f,%.2f,%.2f\n"% (V_ix,V_iy,S_ix,S_iy,D_ix,D_iy))
		"""		
		V_i = 0
		S_i = 0
		D_i = 0
		for i in range(0,(len(data))):
			V_aux = V_i
			V_i = data[i][0] * time + V_i
			V_iy = V_i * m.sin(m.radians(data[i][1]))
			V_ix = V_i * m.cos(m.radians(data[i][1]))
			###posicao######
			S_i = (data[i][0] * time * time)/2 + S_i + V_aux * time
			S_iy = S_i * m.sin(m.radians(data[i][1]))
			S_ix = S_i * m.cos(m.radians(data[i][1]))
			###Distancia sonar####
			if 2>data[i][2]>400:
				#OUT OF RANGE
				D_i = D_ix = D_iy = -1
			else:
				D_i = data[i][2]
				D_iy = data[i][2]*m.sin(m.radians(data[i][1]))
				D_ix = data[i][2]*m.cos(m.radians(data[i][1]))

			write_file.write("%.2f,%.2f,%.2f,%.2f,%.2f,%.2f\n"% (V_ix,V_iy,S_ix,S_iy,D_ix,D_iy)) #data[i][2] data[i][3]

				
		
buff_data()



		
		