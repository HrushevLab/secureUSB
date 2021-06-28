import win32com.client
import os
import time
import shutil
import hashlib
from datetime import datetime


def checkUSB():
    wmi = win32com.client.GetObject ("winmgmts:")
    for usb in wmi.InstancesOf ("Win32_USBHub"):
        result = usb.DeviceID.find('VID_ABCD&PID_1234')
        if result != -1:
            return True
            break

def offPC():
    #saveFile()
    os.system('shutdown /s /t 20 /c "Токен был извлечен!!! У вас есть 20 секунд, чтобы вставить его обратно"')

def shutdownCancel():
    os.system('shutdown /a')

def checkUSBPass():
    if os.path.exists(r'F:\password'):
        passwordUnHashFile = open(r'F:\password', 'r')
        password = passwordUnHashFile.read()
        password = password.encode()
        hashPass =hashlib.sha512(password)
        hexDig = hashPass.hexdigest()
        if '3af146b9bf2a4bdba17d3a1c1726374a4fd27ca4e8a0a898fab1e6d8a559963b36bb2ff9dd23b288ab13c91447307a8fb84b7e2d0c7fcdf85d1a195aba4f5292' != hexDig:
            return False
        else:
            return True

def logger(info):
    infoSTR = "["+datetime.now().strftime('%d-%m-%Y %H:%M:%S')+"]: " + info + '\n'
    logFile = open(r'C:\log.txt','a+')
    logFile.write(infoSTR)
    logFile.close()


shutdown = False
while True:
    checkUSBPass()
    if checkUSB() == True and checkUSBPass() == True:
        if shutdown == True:
            shutdownCancel()
            shutdown = False
            logger('Была произведена отмена выключение')
    else:
        if shutdown == False or checkUSBPass() == False:
            shutdown = True
            offPC()
            logger('Было инициализировано отключение системы')
    time.sleep(1)

