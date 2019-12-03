import socket
import time



roll = 0.0
pitch = 0.0
yaw = 0.0

## Connection
host = "10.0.0.112"
port = 7000
dest = (host,port)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

data = ""

def setup():
    size(1300,700,P3D)
    frameRate(60)
    tcp.connect(dest)
    

def draw():
    translate(width/2, height/2, 0)
    background(0)
    textSize(22)
    text("Roll: {}".format(int(roll)) + "     Pitch: {}".format(int(pitch))+ "     Yaw: {}".format(int(yaw)), -100,265)
    
    ## ROTATE OBJECT
    global pitch
    global roll
    global yaw
    
    rotateX(-radians(pitch))
    rotateZ(-radians(roll))
    rotateY(radians(yaw))
    
    #print(yaw)
    
    ## 3D OBJECT
    textSize(30)
    fill(0,76,153)
    box(386,40,200)
    textSize(25)
    fill(255,255,255)
    text("",-183,10,101)
    
    reader()
    
    #print("to no draw")
    
def reader():
    
    #while True:
    data = tcp.recv(1024)
    #print(data.decode('unicode_escape'))
    if data != None:
        
        data = data.strip()
        items = []
        items = data.split('/')
        if len(data) <= 17 and len(items)==3:
        
            global roll 
            roll = float(items[0])
            global pitch 
            pitch= float(items[1])
            global yaw 
            yaw = float(items[2])
            
            #print("Yaw:", yaw)
        else:
            pass
        
        #print(items)
            
            
    
