from func.Function import *
import time

h = [0, 1, 2, 3, 4, 5, 6, 7]
h1 = [0, 1, 2, 3, 4, 5, 6, 7]
m = [0, 1]
#Config hour Alert
h[0] = 0
h[1] = 3
h[2] = 6
h[3] = 9
h[4] = 12
h[5] = 15
h[6] = 18
h[7] = 21

#Config minute Alert
m[0] = 50

#hour read Sensor
for i in range(8):
    if h[i] == 0:
        h1[i] = "23"
        h[i] = "00"
    elif h[i] > 0 and h[i] <= 9:
        h1[i] = h[i] - 1
        h1[i] = str(h1[i])
        h1[i] = h1[i].rjust(2, '0')
        h[i] = str(h[i])
        h[i] = h[i].rjust(2, '0')
    else:
        h1[i] = h[i] - 1
        h1[i] = str(h1[i])
        h[i] = str(h[i])
    
a = 0
while a < 1:
    time.sleep(30)
    timeis = time.localtime()
    
    #Before Time read Sonser
    if h1[0] or h1[1] or h1[2] or h1[3] or h1[4] or h1[5] or h1[6] or h1[7] == time.strftime('%H', timeis) and m[0] == time.strftime('%M', timeis):
        print("in condition read Sonser")
        print("Wait read Sonser")
        readSensor1()      #Function for Simulation
        #readSensor()
        w_level, w_speed = readSensor()
        print("read Sonser Success")

    if h[0] or h[1] or h[2] == time.strftime('%H', timeis) and m[0] == time.strftime('%M', timeis):
        print("in condition")
        w_level = 3.722
        w_speed = 144.9
        screenshot()
        notifyFile('C:/Temp/99.png', w_level, w_speed)
        deletefile()
        time.sleep(60)
        a += 1
        print("success")

        