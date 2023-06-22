import os, sys

if ".".join(sys.version.split(" ")[0].split(".")[:-1]) != "3.11":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nBạn cần chạy trên phiên bản Python3.11 vì Ngọc lỏ enc file code toàn Python3.11 thôi:v\n Dùng Python khác 3.11 chạy không được đâu!\n")
    input('Press Enter to Exit! ')
    sys.exit()

import socket
import time
import threading
import pystyle
import requests
import googletrans
import bs4

def network():
    try :
        socket.create_connection(("1.1.1.1",53 ))
        return True 
    except OSError :
        pass
    return False

try:
    code=requests.post('https://sever.ngocbansub.com/python/goptooldb.php',headers={'user-agent':'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36'} ,data={'matkhau':'bongocvidaiii'}).text 
except:
    if not network():
        print('Hãy Kiểm Tra Kết Nối Mạng !!! ')
    else :
        print('Sever Gặp Lỗi Hãy Liên Hệ Admin !!! ')
    exit()
ip = requests.get("https://ifconfig.me", {'user-agent' : 'curl/9.9.9'}, verify=False).text
ma_key = str(__import__('requests').post('https://sever.ngocbansub.com/api/key.php', {'user-agent': 'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36', 'pass':'bongocvidaii'} ,verify=False).text.split(',')[1].split(':')[1].replace("\"",""))
os.system('cls' if os.name == 'nt' else 'clear')
print('\nPython v' + sys.version.split(" ")[0])
print('IP: ' + ip)
print("Key của bạn là: " + ma_key)
input('Press Enter to continue! ')
exec(code, globals())