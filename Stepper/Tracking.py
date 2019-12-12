import time
from Reader import Reader_Class
import math as m


class Tracking_Class:

	def __init__(self):


		#### Start Reader Class ####
		self.reader = Reader_Class() 
		self.time = 0.007
		##### Init Speed on axis ###
		#self.speed_dict = {'x':[],'y':[]}

		#calc_x = self.reader.speed[0] * m.cos(m.radians(self.reader.yaw[0]))
		#calc_y = self.reader.speed[0] * m.sin(m.radians(self.reader.yaw[0]))

		self.pos_dict = {'x':[],'y':[]}
		self.pos_dict['x'].append(0)
		self.pos_dict['y'].append(0)

	def tracking(self):

		i= 1
		while True:
			if i<len(self.reader.data.index):

				calc_x = self.reader.speed[i] * m.cos(m.radians(self.reader.yaw[i]))
				calc_y = self.reader.speed[i] * m.sin(m.radians(self.reader.yaw[i]))

				pos_x = self.pos_dict['x'][i-1] + calc_x * self.time
				pos_y = self.pos_dict['y'][i-1] + calc_y * self.time
				#print("pos_x", pos_x)
				#print('i',i)
				self.pos_dict['x'].append(pos_x)
				self.pos_dict['y'].append(pos_y)
				print("Posicao X:",self.pos_dict['x'])
				print("Posicao Y:",self.pos_dict['y'])
				
				i+=1
			else:
				print("VOLTEI A LER")
				self.reader.update_data()

#tracker = Tracking_Class()
#tracker.tracking()	    

