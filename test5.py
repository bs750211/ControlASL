from func.Function import *
import time

h = [0, 1, 2, 3, 4, 5]
m = [0, 1]
#Config hour Alert
h[0] = "16"

#Config minute Alert
m[0] = "03"
a = 0
#hour read Sensor
#h[3] = h[0] - 1
#h[4] = h[1] - 1
#h[5] = h[2] - 1

while a < 1:
    
    time.sleep(10)
    timeis = time.localtime()
    print("loop while h=" + time.strftime('%H', timeis) + " m=" + time.strftime('%M', timeis))

    #Before Time read Sonser
    #if hour == h[3] and minute == m[0]:
        #readSensor()
        #w_level, w_speed = readSensor():
    #if hour == h[4] and minute == m[0]:
        #readSensor()
        #w_level, w_speed = readSensor():
    #if hour == h[5] and minute == m[0]:
        #readSensor()
        #w_level, w_speed = readSensor():

    if h[0] == time.strftime('%H', timeis) and m[0] == time.strftime('%M', timeis):
        print("in condition")
        w_level = 3.722
        w_speed = 144.9
        screenshot()
        notifyFile('C:/Temp/99.png', w_level, w_speed)
        deletefile()
        time.sleep(60)
        a += 1
        print("success")

        