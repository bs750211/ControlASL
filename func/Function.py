def screenshot():
    import autopy
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Temp/99.png')

def deletefile():
    import os
    import time
    time.sleep(10)
    os.remove("C:/Temp/99.png")

#def lineNotify(message):
#    payload = {'message':message}
#    return _lineNotify(payload)

def notifyFile(filename, level, speed):
    import time
    timeis = time.localtime()
    a = "ระดับน้ำ " + str(level) + " เมตร ความเร็ว " + str(speed) + ' cm/s'
    file = {'imageFile':open(filename,'rb')}
    payload = {'message': a}
    return _lineNotify(payload,file)

#def notifyPicture(url):
#    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
#    return _lineNotify(payload)

#def notifySticker(stickerID,stickerPackageID):
#    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
#    return _lineNotify(payload)

def _lineNotify(payload, file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'W8QLoGLoqytOkmNvHSF5H9XC7Gd6yTwawooWPbHCWCQ'  # For กลุ่ม ทดสอบระบบ
    #token = 'x4RaX9Oc3kxsQbjnBilrSovIz5hOsGl4FD6MIFMemvQ'  # For กลุ่ม CCTV ผอ.
    headers = {'Authorization': 'Bearer ' + token}
    return requests.post(url, headers=headers, data=payload, files=file)

def readSensor():
    import socket
    server_ip = '192.168.20.192'
    port = 4003
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((server_ip, port))
    dstrng = ""
    a = 0
    while a < 14:
        data_server = server.recv(1024).decode('utf-8')
        dstrng += data_server
        a += 1
        try:
            dstrng = dstrng.rstrip()
            dstrng = dstrng.strip()
        except:
            print("This string does not comply with the UTF-8 standard")
    s = dstrng.split()
    return s[5], s[7]

#for simulation sensor
def readSensor1():
    return 5.000, 140.0