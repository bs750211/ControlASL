def screenshot():
    import autopy
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Temp/99.png')

def deletefile():
    import os
    import time
    time.sleep(10)
    os.remove("C:/Temp/99.png")

# def lineNotify(message):
#    payload = {'message':message}
#    return _lineNotify(payload)

def notifyFile(filename):
    import time
    timeis = time.localtime()
    a = 'ระดับน้ำเวลา ' + time.strftime('%H:%M:%S', timeis)
    file = {'imageFile': open(filename, 'rb')}
    payload = {'message': a}
    return _lineNotify(payload, file)

# def notifyPicture(url):
#    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
#    return _lineNotify(payload)

# def notifySticker(stickerID,stickerPackageID):
#    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
#    return _lineNotify(payload)

def _lineNotify(payload, file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'grkyGCeCVgTduZHOipESEed6AKiDeceKqdjxS1BcCHa'  # For กลุ่ม จนท. คอม
    #token = 'x4RaX9Oc3kxsQbjnBilrSovIz5hOsGl4FD6MIFMemvQ'  # For กลุ่ม CCTV ผอ.
    headers = {'Authorization': 'Bearer ' + token}
    return requests.post(url, headers=headers, data=payload, files=file)

screenshot()
notifyFile('C:/Temp/99.png')
deletefile()