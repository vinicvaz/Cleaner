import socket
import time
import re



roll = 0.0
pitch = 0.0
yaw = 0.0

## Connection
host = "10.0.0.102"
port = 7000
dest = (host,port)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#regex = "(((-{1})?([0-9][.][0-9][0-9])\/{1}(-{1})?([0-9][.][0-9][0-9])\/{1}(-{1})?([0-9][.][0-9][0-9])){1})"

data = ""

def setup():
    size(1300,700,P3D)
    frameRate(90)
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
    textSize(90)
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
        data = data.rstrip('-')
        items = []
        items = data.split('/')
        #if len(data) <= 17 and len(items)==3:
        if re.match(r'(((-{1})?([0-9]{1,3}[.][0-9][0-9])\/{1}(-{1})?([0-9]{1,3}[.][0-9][0-9])\/{1}(-{1})?([0-9]{1,3}[.][0-9][0-9])){1})',data) and len(data)<=17 and len(items)==3:
            global roll 
            #if '/' not in items[0]:
            roll = float(items[0])
            global pitch 
            #if '/' not in items[1]:
            pitch= float(items[1])
            global yaw
            #if '/' not in items[2]: 
            yaw = float(items[2])
            
            print("Item[0]:", items[0])
        else:
            pass

        #print(items)
            
            
    
