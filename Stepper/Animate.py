import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Reader import Reader_Class




def animate(i):
	reader.update_data()
	x = reader.distance
	y = reader.pitch

	plt.cla()
	plt.plot(x,y)

reader = Reader_Class()
#plot = Animate_Plot()

ani = FuncAnimation(plt.gcf(), animate, interval=0.001)
plt.tight_layout()
plt.show()
