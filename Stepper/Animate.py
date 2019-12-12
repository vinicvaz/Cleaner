import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Reader import Reader_Class
from Tracking import Tracking_Class
import threading

class Plot_Class:

	def __init__(self):

		#### Start Tracking Class and run as Background ###
		self.tracking = Tracking_Class()
		print("Iniciando Thread")
		self.thread_tracking = threading.Thread(target = self.tracking.tracking)
		self.thread_tracking.daemon = True
		self.thread_tracking.start()

		print("Passei Da Thread")

		self.ani = FuncAnimation(plt.gcf(), self.animate, interval=0.0001)

	def animate(self,i):
		x = self.tracking.pos_dict['x']
		y = self.tracking.pos_dict['y']
		plt.cla()
		plt.plot(x,y) 

	




plot = Plot_Class()

plt.tight_layout()
plt.show()
