import matplotlib.pyplot as plt
import csv
import math as m
import matplotlib.lines as mlines
import numpy as np

csv_file = open("buff_data.csv", mode='r')
csv_reader = csv.reader(csv_file, delimiter=',')

try:
	data = list(csv_reader)
	data= [[float(float(j)) for j in i] for i in data]
	#print(data)
	pos_y = 0
	pos_x = 0
	dist_x = 0
	dist_y =0
	aux_x = 0 
	aux_y = 0
	aux_dist_x = 0
	aux_dist_y = 0
	for i in range(len(data)):
		aux_y = pos_y
		aux_x = pos_x

		pos_y = data[i][3] # terceira coluna = posição em y
		pos_x = data[i][2] # segunda coluna = posição em x

		dist_x = data[i][4] +data[i][2] # distancia do obj = posição do carrinho + distancia sonar
		dist_y = data[i][5] +data[i][3]
		if (i-1==-1):
			pass
		else:
			aux_dist_x = data[i-1][4] + data[i-1][2]
			aux_dist_y = data[i-1][5] + data[i-1][3]
			# NAO SEI SE VOU USAR PQ LIGA TODOS OS PONTOS EM ORDEM "PRA Q ?" plt.plot([aux_dist_x, dist_x], [aux_dist_y, dist_y], color='black')#linha entre os pontos marcados como obj
			plt.plot([aux_x, pos_x], [aux_y, pos_y], color='red') #linha por onde o carrinho andou
		
		p1 = [aux_x,aux_y]
		p2 = [pos_x,pos_y]
		print("P1:{0} P2:{1}".format(p1,p2))


		plt.plot(pos_x, pos_y, color='blue', marker='o', linestyle=':', linewidth=2, markersize=3)#pontos onde o carrinho atualizou sua posição
		
		plt.plot(dist_x, dist_y, color='green', marker='o', linestyle=':', linewidth=2, markersize=1)#pontos onde foi encontrado um obj
	

	plt.show()
finally:
	csv_file.close()


