import pandas as pd
class Reader_Class:

	def __init__(self):

		self.path = '//home//vinicius//Temp_Client//temp_client.txt'  ## Temp File Path
		self.data = pd.read_csv(self.path,sep='/') ## Read CSV 
		self.speed = self.data['speed'] ## Get Speed column from file
		self.distance = self.data['distance'] ## Get Distance Column from file
		self.pitch = self.data['x'] ## Get Pitch value from file
		self.roll = self.data['y'] ## Get Roll value from file
		self.yaw = self.data['z'] ## Get Yaw value from file


	def update_data(self):
		self.data = pd.read_csv(self.path,sep='/')
		self.speed = self.data['speed']
		self.distance = self.data['distance']
		self.pitch = self.data['x']
		self.roll = self.data['y']
		self.yaw = self.data['z']