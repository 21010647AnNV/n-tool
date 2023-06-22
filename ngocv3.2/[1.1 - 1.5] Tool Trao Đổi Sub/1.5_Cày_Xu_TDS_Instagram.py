def banner():
    print("   ███╗   ██╗   ████████╗ ██████╗  ██████╗ ██╗     \n   ████╗  ██║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     \n   ██╔██╗ ██║█████╗██║   ██║   ██║██║   ██║██║     \n   ██║╚██╗██║╚════╝██║   ██║   ██║██║   ██║██║     \n   ██║ ╚████║      ██║   ╚██████╔╝╚██████╔╝███████╗\n   ╚═╝  ╚═══╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝")
    print('        \x1b[1;37mCopyright © N-Tool 2022 | Version 3.2\n\x1b[1;31m────────────────────────────────────────────────────────\n\x1b[1;37m~\x1b[1;31m[\x1b[1;32m●\x1b[1;31m]\x1b[1;37m ➩\x1b[1;35m Admin: \x1b[1;36mNguyễn Chính Ngọc  \n\x1b[1;37m~\x1b[1;31m[\x1b[1;32m●\x1b[1;31m]\x1b[1;37m ➩\x1b[1;36m Zalo: \x1b[1;31m0369889638\n\x1b[1;37m~\x1b[1;31m[\x1b[1;32m●\x1b[1;31m]\x1b[1;37m ➩\x1b[1;32m Box Zalo: \x1b[1;37mhttps://zalo.me/g/cklqap965\n\x1b[1;37m~\x1b[1;31m[\x1b[1;32m●\x1b[1;31m]\x1b[1;37m ➩\x1b[1;33m YouTube: \x1b[1;37mhttps://youtube.com/@ngoctool\n\x1b[1;37m~\x1b[1;31m[\x1b[1;32m●\x1b[1;31m]\x1b[1;37m ➩ ')
den = '\x1b[1;90m'
luc = '\x1b[1;32m'
trang = '\x1b[1;37m'
red = '\x1b[1;31m'
vang = '\x1b[1;33m'
tim = '\x1b[1;35m'
lamd = '\x1b[1;34m'
lam = '\x1b[1;36m'
purple = '\\e[35m'
hong = '\x1b[1;95m'
thanh_xau = trang + '~' + red + '[' + vang + '⟨⟩' + red + '] ' + trang + '➩ ' + luc
thanh_dep = trang + '~' + red + '[' + vang + '✓' + red + '] ' + trang + '➩ ' + luc

import requests ,os ,sys ,re ,json 
from time import sleep 
from datetime import datetime 
import time 
from random import randint 
from sys import platform 
O00O0O0OOOO00OO00 =0 
O000OOO0O0OOO00OO =[]
def OOO00OO0000OOO00O (O0O00O00OOOO0OOO0 ):
	for OOOO0OOOO0000OOOO in range (O0O00O00OOOO0OOO0 ,-1 ,-1 ):
		print (f'{trang}Đang hoạt động chống block sẽ chạy lại sau {OOOO0OOOO0000OOOO} giây  ',end ='\r');sleep (1 );print (f'                                                        ',end ='\r')
def O0O0OO0OOO0OO00O0 (OOOO00OOO00OO0OOO ,O0O0O000O0O0OO0O0 ):
	OOOOOOOO00O00000O =randint (OOOO00OOO00OO0OOO ,O0O0O000O0O0OO0O0 )
	try :
		for O00OOOO0O00OO0O0O in range (OOOOOOOO00O00000O ,-1 ,-1 ):
			print (f'{vang}[{trang}NGOCTOOL{vang}][{trang}'+str (O00OOOO0O00OO0O0O )+vang +']           ',end ='\r')
			sleep (1 )
	except :
		sleep (OOOOOOOO00O00000O )
		print (OOOOOOOO00O00000O ,end ='\r')
def OO000000O000OOO00 (OO0000000O0OOO000 ,OO000O0O000OO0OOO ,OOOO00OO0O00O0OO0 ,O0OO000O0O0O0000O ,O0OO0O000OO000OO0 ):
	OOOOO00000OO00O0O =OO000O0O000OO0OOO .split ('_')[0 ]if '_'in OO000O0O000OO0OOO else OO000O0O000OO0OOO 
	O0O00OOO0O0O000OO =datetime .now ().strftime ("%H:%M:%S")
	print (f'{vang}[{trang}{OO0000000O0OOO000}{vang}] {red}| {lam}{O0O00OOO0O0O000OO} {red}| {vang}{OOOO00OO0O00O0OO0} {red}| {trang}{OOOOO00000OO00O0O} {red}| {luc}{O0OO000O0O0O0000O} {red}| {vang}{O0OO0O000OO000OO0} {red}|')
def O0OOO00OO0OOO0OO0 (OO0O000OOO0OO00OO ,OO0O0000OO0OO0OO0 ):
	O00O000O0O00OO0O0 =datetime .now ().strftime ("%H:%M:%S")
	O00000OOOO00OO00O =OO0O000OOO0OO00OO .split ('_')[0 ]if '_'in OO0O000OOO0OO00OO else OO0O000OOO0OO00OO 
	print (f'{vang}[{red}X{vang}] {red}| {lam}{O00O000O0O00OO0O0} {red}| {vang}{OO0O0000OO0OO0OO0} {red}| {trang}{O00000OOOO00OO00O} {red}| ERROR',end ='\r');sleep (2 );print (f'                                                   ',end ='\r')
def O000O0O00OOOO00O0 ():
	O0OO0O0O00O0O0OOO =0 
	while True :
		O0OO0O0O00O0O0OOO +=1 
		OO000O00O00OOO00O =input (f'{thanh_xau}{luc}Nhập Cookie Instagram Thứ {O0OO0O0O00O0O0OOO}:{vang} ')
		if OO000O00O00OOO00O ==''and O0OO0O0O00O0O0OOO >1 :
			break 
		O00OO0O0O0000O0O0 =OO0O000O0O000OOOO (OO000O00O00OOO00O )
		OOO00000O00OO000O =O00OO0O0O0000O0O0 .name ()
		if OOO00000O00OO000O !=False :
			OOO0OO00OOOO00O00 =OOO00000O00OO000O [0 ]
			print (f'{luc}User Instagram:{vang} {OOO0OO00OOOO00O00}')
			O000OOO0O0OOO00OO .append (OO000O00O00OOO00O )
			OOO0O00OO0OOOOOO0 (14 )
		else :
			print (f'{red}Cookie Instagram Die ! Vui Lòng Nhập Lại !!!')
			OOO0O00OO0OOOOOO0 (14 )
			O0OO0O0O00O0O0OOO -=1 
	return O000OOO0O0OOO00OO 
class OO0O000O0O000OOOO (object ):
	def __init__ (O00O0OOO00O00O0O0 ,O000OOOOOO000OO00 ):
		O00O0OOO00O00O0O0 .cookie =O000OOOOOO000OO00 
	def name (OOOO00O0O00O00O00 ):
		try :
			OO0O0O0000000O0OO ={'Host':'www.instagram.com','cache-control':'max-age=0','viewport-width':'980','sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 11; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site':'same-origin','sec-fetch-mode':'navigate','sec-fetch-user':'?1','sec-fetch-dest':'document','accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie':OOOO00O0O00O00O00 .cookie }
			O00OOO0O00OO0OOOO =requests .get ('https://www.instagram.com/',headers =OO0O0O0000000O0OO ).text 
			O00O000O000OOO0O0 =O00OOO0O00OO0OOOO .split ('username')[1 ].split ('\\"')[2 ]
			O00O000OO0OOOO0O0 =OOOO00O0O00O00O00 .cookie .split ('ds_user_id=')[1 ].split (';')[0 ]
			OOOO00O0O00O00O00 .headers ={"x-ig-app-id":"1217981644879628","x-asbd-id":"198387","x-instagram-ajax":"c161aac700f","accept":"*/*","content-length":"0","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03S) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19","x-csrftoken":OOOO00O0O00O00O00 .cookie .split ('csrftoken=')[1 ].split (';')[0 ],"x-requested-with":"XMLHttpRequest","cookie":OOOO00O0O00O00O00 .cookie }
			return O00O000O000OOO0O0 ,O00O000OO0OOOO0O0 
		except :
			return False 
	def like (O000OO00000OOO0OO ,O00000OO000O0OO0O ):
		try :
			OOOOOOOO00000OO0O =requests .post (f'https://www.instagram.com/web/likes/{O00000OO000O0OO0O}/like/',headers =O000OO00000OOO0OO .headers ).text 
			if '{"status":"ok"}'in OOOOOOOO00000OO0O :
				return True 
			else :
				return False 
		except :
			return False 
	def follow (OO0O0OO0O0O0000OO ,O00000OO0OO00OO0O ):
		try :
			O0O00O00000O00OO0 =requests .post ("https://i.instagram.com/web/friendships/"+O00000OO0OO00OO0O +"/follow/",headers =OO0O0OO0O0O0000OO .headers ).text 
			if '{"result":"following","status":"ok"}'in O0O00O00000O00OO0 or '{"result":"requested","status":"ok"}'in O0O00O00000O00OO0 :
				return True 
			else :
				return False 
		except :
			return False 
	def cmt (O0O0O00000O00000O ,OO00OOOOOO00O0O0O ,O0O000OOO00OO0O00 ):
		try :
			OO00O0O0OO0O00O0O =requests .post (f'https://i.instagram.com/api/v1/web/comments/{O0O000OOO00OO0O00}/add/',headers =O0O0O00000O00000O .headers ,data ={'comment_text':OO00OOOOOO00O0O0O }).text 
			if '"status":"ok"'in OO00O0O0OO0O00O0O :
				return True 
			else :
				return False 
		except :
			return False 
class O0OOO0OOOO0OO0000 (object ):
	def __init__ (O0O0O0OO0O0OOOOO0 ,OOOO00000OO0O0O00 ):
		O0O0O0OO0O0OOOOO0 .token =OOOO00000OO0O0O00 
	def main (O00OOO0O0O0OO00OO ):
		try :
			OOOOOOO0O0000O0OO =requests .get ('https://traodoisub.com/api/?fields=profile&access_token='+O00OOO0O0O0OO00OO .token ).json ()
			return OOOOOOO0O0000O0OO ['data']
		except :
			return False 
	def run (O000OOO000O000O0O ,OO00O00OOOO00OO0O ):
		try :
			OO0OOO00OO0OO0000 =requests .get (f'https://traodoisub.com/api/?fields=instagram_run&id={OO00O00OOOO00OO0O}&access_token={O000OOO000O000O0O.token}').json ()
			OO0OOO00OO0OO0000 ['data']['id']
			return True 
		except :
			return False 
	def get_nv (OOOOO00O000O0OOO0 ,OOO0O00O00O000OO0 ):
		try :
			OO0OO00O0OO0O0000 =requests .get (f'https://traodoisub.com/api/?fields={OOO0O00O00O000OO0}&access_token={OOOOO00O000O0OOO0.token}')
			return OO0OO00O0OO0O0000 
		except :
			return False 
	def nhan_xu (OO00O000O00000000 ,O000OO0O000OO0OOO ,OO000000O00O0OO0O ):
		try :
			O00000O00O00O00OO =requests .get (f'https://traodoisub.com/api/coin/?type={O000OO0O000OO0OOO}&id={OO000000O00O0OO0O}&access_token={OO00O000O00000000.token}').json ()
			O00O0OOOO000OO0OO =O00000O00O00O00OO ['data']['msg']
			OO0O000O0OOOO0000 =O00000O00O00O00OO ['data']['pending']
			return O00O0OOOO000OO0OO ,OO0O000O0OOOO0000 
		except :
			return False 
def OOO0O00OO0OOOOOO0 (OO000O0O0OOOOO0OO ):
	O00OOO0000OO0OOOO =f"{red}────"*OO000O0O0OOOOO0OO 
	for O00000O0O00000OOO in range (len (O00OOO0000OO0OOOO )):
		sys .stdout .write (O00OOO0000OO0OOOO [O00000O0O00000OOO ])
		sys .stdout .flush ()
	print ()
def OOO0O000000O00O00 ():
	OOOO0OO00OO00OO0O =0 
	OO0000OO0O0OO0OOO =0 
	banner ()
	while True :
		if os .path .exists ('configtds.txt'):
			with open ('configtds.txt','r')as O00O0OOO0OOO0OOOO :
				O00OOOO00O00O00O0 =O00O0OOO0OOO0OOOO .read ()
			OO0O0OO0O00000O00 =O0OOO0OOOO0OO0000 (O00OOOO00O00O00O0 )
			O000000O0OOOOO00O =OO0O0OO0O00000O00 .main ()
			try :
				print (f'{thanh_xau}{luc}Nhập {vang}[{trang}1{vang}] {luc}Giữ Lại Tài Khoản{vang} '+O000000O0OOOOO00O ['user'])
				print (f'{thanh_xau}{luc}Nhập {vang}[{trang}2{vang}] {luc}Nhập Access_Token TDS Mới')
				O0OO0OOOOO0O0O0OO =input (f'{thanh_xau}{luc}Nhập {trang}===>: {vang}')
				if O0OO0OOOOO0O0O0OO =='2':
					os .remove ('configtds.txt')
				elif O0OO0OOOOO0O0O0OO =='1':
					pass 
				else :
					print (red +'Lựa chọn không xác định !!!');OOO0O00OO0OOOOOO0 (14 )
					continue 
			except :
				os .remove ('configtds.txt')
		if not os .path .exists ('configtds.txt'):
			O00OOOO00O00O00O0 =input (f'{thanh_xau}{luc}Nhập Access_Token TDS:{vang} ')
			with open ('configtds.txt','w')as O00O0OOO0OOO0OOOO :
				O00O0OOO0OOO0OOOO .write (O00OOOO00O00O00O0 )
		with open ('configtds.txt','r')as O00O0OOO0OOO0OOOO :
			O00OOOO00O00O00O0 =O00O0OOO0OOO0OOOO .read ()
		OO0O0OO0O00000O00 =O0OOO0OOOO0OO0000 (O00OOOO00O00O00O0 )
		O000000O0OOOOO00O =OO0O0OO0O00000O00 .main ()
		try :
			O0OOO00O0000000OO =O000000O0OOOOO00O ['xu']
			O0OO0O00000OOOO0O =O000000O0OOOOO00O ['xudie']
			O0O000O0O00OOOOOO =O000000O0OOOOO00O ['user']
			print (lam +' Đăng Nhập Thành Công ')
			break 
		except :
			print (red +'Access Token Không Hợp Lệ! Xin Thử Lại ')
			os .remove ('configtds.txt')
			continue 
	OOO0O00OO0OOOOOO0 (14 )
	while True :
		if os .path .exists ('N-Tool_CookieIG.txt'):
			print (f'{thanh_xau}{luc}Nhập {vang}[{trang}1{vang}] {luc}Sử Dụng Cookie Instagram Đã Lưu ')
			print (f'{thanh_xau}{luc}Nhập {vang}[{trang}2{vang}] {luc}Nhập Cookie Instagram Mới')
			O0OO0OOOOO0O0O0OO =input (f'{thanh_xau}{luc}Vui Lòng Nhập: {vang}')
			if O0OO0OOOOO0O0O0OO =='1':
				print (f' {lam}Đang Lấy Dữ Liệu Đã Lưu');sleep (1 )
				with open ('N-Tool_CookieIG.txt','r')as O00O0OOO0OOO0OOOO :
					O0OO0O00O0000000O =json .loads (O00O0OOO0OOO0OOOO .read ())
					break 
			elif O0OO0OOOOO0O0O0OO =='2':
				os .remove ('N-Tool_CookieIG.txt');OOO0O00OO0OOOOOO0 (14 )
			else :
				print (red +'Lựa Chọn Không Xác Định.');OOO0O00OO0OOOOOO0 (14 );continue 
		if not os .path .exists ('N-Tool_CookieIG.txt'):
			O0OO0O00O0000000O =O000O0O00OOOO00O0 ()
			with open ('N-Tool_CookieIG.txt','w')as O00O0OOO0OOO0OOOO :
				json .dump (O0OO0O00O0000000O ,O00O0OOO0OOO0OOOO )
			break 
	banner ()
	print (f'{thanh_xau}{luc}Tên Tài Khoản{vang}:',O0O000O0O00OOOOOO )
	print (f'{thanh_xau}{luc}Xu Hiện Tại:{vang}',O0OOO00O0000000OO )
	print (f'{thanh_xau}{luc}Xu Bị Trừ:{vang}',O0OO0O00000OOOO0O )
	OOO0O00OO0OOOOOO0 (14 )
	print (f'{thanh_xau}{luc}Nhập {vang}[{trang}1{vang}] {luc}Để Chạy Nhiệm Vụ Like')
	print (f'{thanh_xau}{luc}Nhập {vang}[{trang}2{vang}] {luc}Để Chạy Nhiệm Vụ Follow')
	print (f'{thanh_xau}{luc}Nhập {vang}[{trang}3{vang}] {luc}Để Chạy Nhiệm Vụ Comment')
	print (f'{thanh_xau}{lam}Có Thể Chọn Nhiều Nhiệm Vụ (Ví Dụ 1+2+3)')
	O00O00000OO000O00 =input (f'{thanh_xau}{luc}Nhập Số Để Chạy Nhiệm Vụ: {vang}')
	OOO0O00OO0OOOOOO0 (14 )
	O0O00O0OO00000OOO =int (input (f'{thanh_xau}{luc}Nhập Delay Min: {vang}'))
	O0O0000OOOOO0O00O =int (input (f'{thanh_xau}{luc}Nhập Delay Max: {vang}'))
	print (f'{thanh_xau}{luc}Sau ____ Nhiệm Vụ Thì Kích Hoạt Chống Block.',end ='\r')
	O0OOO0O0OOO00O0O0 =int (input (f'{thanh_xau}{luc}Sau{vang} '))
	print (f'{thanh_xau}{luc}Sau {vang}{O0OOO0O0OOO00O0O0}{luc} Nhiệm Vụ Nghỉ Ngơi ____ Giây       ',end ='\r')
	OOO000OO0OOOO0O0O =int (input (f'{thanh_xau}{luc}Sau {vang}{O0OOO0O0OOO00O0O0} {luc}Nhiệm Vụ Nghỉ Ngơi{vang} '))
	O0O0OO0O0O0OO0OOO =int (input (f'{thanh_xau}{luc}Sau Bao Nhiêu Nhiệm Vụ Thì Đổi Nick:{vang} '))
	while True :
		if len (O0OO0O00O0000000O )==0 :
			print (f'{red}Đã Xoá Tất Cả Cookie, Vui Lòng Nhập Lại  ')
			O0OO0O00O0000000O =O000O0O00OOOO00O0 ()
			with open ('N-Tool_CookieIG.txt','w')as O00O0OOO0OOO0OOOO :
				json .dump (O0OO0O00O0000000O ,O00O0OOO0OOO0OOOO )
		for OOOOOOOO0O0OOOO0O in O0OO0O00O0000000O :
			OO0OO0O000OO0O00O ,OOOO00O00O00O0OOO ,O0OOO00O0OOO0O0OO =0 ,0 ,0 
			OOOO0OO00O000OO00 =OO0O000O0O000OOOO (OOOOOOOO0O0OOOO0O )
			O00000O00O00O0000 =OOOO0OO00O000OO00 .name ()
			if O00000O00O00O0000 !=False :
				O0O000O0O00OOOOOO =O00000O00O00O0000 [0 ]
				OOO00O000O0OOO000 =O00000O00O00O0000 [1 ]
			else :
				OOO00O000O0OOO000 =OOOOOOOO0O0OOOO0O .split ('ds_user_id=')[1 ].split (';')[0 ]
				print (f'{red}Cookie Tài Khoản {OOO00O000O0OOO000} Die',end ='\r');sleep (3 );print (f'                                     ',end ='\r')
				O0OO0O00O0000000O .remove (OOOOOOOO0O0OOOO0O )
				continue 
			O0O0000OOO0OOOO00 =OO0O0OO0O00000O00 .run (OOO00O000O0OOO000 )
			if O0O0000OOO0OOOO00 ==True :
				OOO0O00OO0OOOOOO0 (14 )
				print (f'{luc}Đang Cấu Hình ID: {vang}{OOO00O000O0OOO000} {red}| {luc}User: {vang}{O0O000O0O00OOOOOO} {red}|')
				OOO0O00OO0OOOOOO0 (14 )
			else :
				print (f'{red}Cấu Hình Thất Bại ID: {OOO00O000O0OOO000} | User: {O0O000O0O00OOOOOO} {red}| ',end ='\r')
				continue 
			OOOO0OO00OO00OO0O =0 
			while True :
				O0OOOOO00OO00OOOO =1 if '1'in O00O00000OO000O00 else 0 
				OOO0O0OO00O0000O0 =1 if '2'in O00O00000OO000O00 else 0 
				O0O00O0O00OOO000O =1 if '3'in O00O00000OO000O00 else 0 
				if O0OOOOO00OO00OOOO ==1 :
					OOOOO000OOOO0OO0O =OO0O0OO0O00000O00 .get_nv ('instagram_like')
					if OOOOO000OOOO0OO0O ==False :
						print (f'{red}Không Get Được Nhiệm Vụ Like              ',end ='\r');sleep (2 );print (f'                                                        ',end ='\r')
						O0OOOOO00OO00OOOO =0 
					elif 'error'in OOOOO000OOOO0OO0O .text :
						if OOOOO000OOOO0OO0O .json ()['error']=='Thao tác quá nhanh vui lòng chậm lại':
							OO00000O000OO0OOO =OOOOO000OOOO0OO0O .json ()['countdown']
							print (f'{red}Đang Get Nhiệm Vụ Like, COUNTDOWN: {str(round(OO00000O000OO0OOO, 3))}              ',end ='\r');sleep (2 );print (f'                                                       ',end ='\r')
						else :
							print (OOOOO000OOOO0OO0O .json ()['error'],end ='\r')
						O0OOOOO00OO00OOOO =0 
					else :
						try :
							OOOOO000OOOO0OO0O =OOOOO000OOOO0OO0O .json ()['data']
						except :
							print (f'{red}Không Get Được Nhiệm Vụ Like              ',end ='\r');sleep (2 );print (f'                                                        ',end ='\r')
							O0OOOOO00OO00OOOO =0 ;OOOOO000OOOO0OO0O =[]
						if len (OOOOO000OOOO0OO0O )==0 :
							print (f'{red}Hết Nhiệm Vụ Like                             ',end ='\r');sleep (2 );print (f'                                                        ',end ='\r')
							O0OOOOO00OO00OOOO =0 
						else :
							print (f'{luc}Tìm Thấy {vang}{len(OOOOO000OOOO0OO0O)}{luc} Nhiệm Vụ Like                       ',end ='\r');sleep (2 );print (f'                                                        ',end ='\r')
							for O00OOOOOO00OOO00O in OOOOO000OOOO0OO0O :
								OOO00O000O0OOO000 =O00OOOOOO00OOO00O ['id']
								OOO0OO00OO00OOO00 =O00OOOOOO00OOO00O ['link']
								OOOOOOO0OO0000O00 =OOO00O000O0OOO000 .split ('_')[0 ]if '_'in OOO00O000O0OOO000 else OOO00O000O0OOO000 
								O000O0000O000O000 =OOOO0OO00O000OO00 .like (OOOOOOO0OO0000O00 )
								if O000O0000O000O000 ==False :
									O0OOO00OO0OOO0OO0 (OOO00O000O0OOO000 ,'LIKE')
									OO0OO0O000OO0O00O +=1 
									O0O0O0O0OO0OOOO0O =OO0O0OO0O00000O00 .nhan_xu ('INS_LIKE_CACHE',OOO00O000O0OOO000 )
								else :
									O0O0O0O0OO0OOOO0O =OO0O0OO0O00000O00 .nhan_xu ('INS_LIKE_CACHE',OOO00O000O0OOO000 )
									try :
										O0OOO00O0000000OO =O0O0O0O0OO0OOOO0O [1 ]
										OO0OOO000O000OO00 =O0O0O0O0OO0OOOO0O [0 ]
										OO0000OO0O0OO0OOO +=1 
										OO000000O000OOO00 (OO0000OO0O0OO0OOO ,OOO00O000O0OOO000 ,'LIKE',OO0OOO000O000OO00 ,O0OOO00O0000000OO )
										OO0OO0O000OO0O00O =0 
										if OO0000OO0O0OO0OOO %O0O0OO0O0O0OO0OOO ==0 :
											OOO0O00OO0OOOOOO0 (14 );print (f'{lam}Số Xu Hiện Tại: {vang}{O0OOO00O0000000OO} {red}| {lam}Số Tài Khoản Instagram {vang}{len(O0OO0O00O0000000O)}');OOO0O00OO0OOOOOO0 (14 );OOOO0OO00OO00OO0O =1 ;break 
										if OO0000OO0O0OO0OOO %O0OOO0O0OOO00O0O0 ==0 :
											OOO00OO0000OOO00O (OOO000OO0OOOO0O0O )
										else :
											O0O0OO0OOO0OO00O0 (O0O00O0OO00000OOO ,O0O0000OOOOO0O00O )
									except :
										O0OOO00OO0OOO0OO0 (OOO00O000O0OOO000 ,'LIKE')
										OO0OO0O000OO0O00O +=1 
								if OO0OO0O000OO0O00O >=5 :
									O00000O00O00O0000 =OOOO0OO00O000OO00 .name ()
									if O00000O00O00O0000 ==False :
										print (f'  {red}Cookie Tài Khoản {O0O000O0O00OOOOOO} Đã Bị Out !!!                ')
									else :
										print (f' {red}Tài Khoản {O0O000O0O00OOOOOO} Đã Bị Block Like !!!					')
									O0OO0O00O0000000O .remove (OOOOOOOO0O0OOOO0O )
									OOOO0OO00OO00OO0O =1 
									break 
				if OOOO0OO00OO00OO0O ==1 :
					break 
				if OOO0O0OO00O0000O0 ==1 :
					O000OO0O0OO0OO000 =OO0O0OO0O00000O00 .get_nv ('instagram_follow')
					if O000OO0O0OO0OO000 ==False :
						print (f'{red}Không Get Được Nhiệm Vụ Follow              ',end ='\r');sleep (2 );print (f'                                                        ',end ='\r')
						OOO0O0OO00O0000O0 =0 
					elif 'error'in O000OO0O0OO0OO000 .text :
						if O000OO0O0OO0OO000 .json ()['error']=='Thao tác quá nhanh vui lòng chậm lại':
							OO00000O000OO0OOO =O000OO0O0OO0OO000 .json ()['countdown']
							print (f'{red}Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(OO00000O000OO0OOO, 3))}              ',end ='\r');sleep (2 );print (f'                                                       ',end ='\r')
						else :
							print (O000OO0O0OO0OO000 .json ()['error'],end ='\r')
						OOO0O0OO00O0000O0 =0 
					else :
						try :
							O000OO0O0OO0OO000 =O000OO0O0OO0OO000 .json ()['data']
						except :
							print (f'{red}Không Get Được Nhiệm Vụ Follow              ',end ='\r');sleep (2 );print (f'                                                        ',end ='\r')
							OOO0O0OO00O0000O0 =0 ;O000OO0O0OO0OO000 =[]
						if len (O000OO0O0OO0OO000 )==0 :
							print (f'{red}Hết Nhiệm Vụ FOLLOW                             ',end ='\r');sleep (2 );print (f'                                                        ',end ='\r')
							OOO0O0OO00O0000O0 =0 
						else :
							print (f'{luc}Tìm Thấy {vang}{len(O000OO0O0OO0OO000)}{luc} Nhiệm Vụ Follow                       ',end ='\r');sleep (2 );print (f'                                                        ',end ='\r')
							for O00OOOOOO00OOO00O in O000OO0O0OO0OO000 :
								OOO00O000O0OOO000 =O00OOOOOO00OOO00O ['id']
								OOO0OO00OO00OOO00 =O00OOOOOO00OOO00O ['link']
								OOOOOOO0OO0000O00 =OOO00O000O0OOO000 .split ('_')[0 ]if '_'in OOO00O000O0OOO000 else OOO00O000O0OOO000 
								OO0O00OOO0OO00000 =OOOO0OO00O000OO00 .follow (OOOOOOO0OO0000O00 )
								if OO0O00OOO0OO00000 ==False :
									O0OOO00OO0OOO0OO0 (OOO00O000O0OOO000 ,'FOLLOW')
									O0O0O0O0OO0OOOO0O =OO0O0OO0O00000O00 .nhan_xu ('INS_FOLLOW_CACHE',OOO00O000O0OOO000 )
									OOOO00O00O00O0OOO +=1 
								else :
									O0O0O0O0OO0OOOO0O =OO0O0OO0O00000O00 .nhan_xu ('INS_FOLLOW_CACHE',OOO00O000O0OOO000 )
									try :
										O0OOO00O0000000OO =O0O0O0O0OO0OOOO0O [1 ]
										OO0OOO000O000OO00 =O0O0O0O0OO0OOOO0O [0 ]
										OO0000OO0O0OO0OOO +=1 
										OO000000O000OOO00 (OO0000OO0O0OO0OOO ,OOO00O000O0OOO000 ,'FOLLOW',OO0OOO000O000OO00 ,O0OOO00O0000000OO )
										OOOO00O00O00O0OOO =0 
										if OO0000OO0O0OO0OOO %O0O0OO0O0O0OO0OOO ==0 :
											OOO0O00OO0OOOOOO0 (14 );print (f'{lam}Số Xu Hiện Tại: {vang}{O0OOO00O0000000OO} {red}| {lam}Số Tài Khoản Instagram {vang}{len(O0OO0O00O0000000O)}');OOO0O00OO0OOOOOO0 (14 );OOOO0OO00OO00OO0O =1 ;break 
										if OO0000OO0O0OO0OOO %O0OOO0O0OOO00O0O0 ==0 :
											OOO00OO0000OOO00O (OOO000OO0OOOO0O0O )
										else :
											O0O0OO0OOO0OO00O0 (O0O00O0OO00000OOO ,O0O0000OOOOO0O00O )
									except :
										O0OOO00OO0OOO0OO0 (OOO00O000O0OOO000 ,'FOLLOW')
										OOOO00O00O00O0OOO +=1 
								if OOOO00O00O00O0OOO >=5 :
									O00000O00O00O0000 =OOOO0OO00O000OO00 .name ()
									if O00000O00O00O0000 ==False :
										print (f'  {red}Cookie Tài Khoản {O0O000O0O00OOOOOO} Đã Bị Out !!!                ')
									else :
										print (f' {red}Tài Khoản {O0O000O0O00OOOOOO} Đã Bị Block Follow !!!					')
									O0OO0O00O0000000O .remove (OOOOOOOO0O0OOOO0O )
									OOOO0OO00OO00OO0O =1 
									break 
				if OOOO0OO00OO00OO0O ==1 :
					break 
				if O0O00O0O00OOO000O ==1 :
					OO000O00OOO0O000O =OO0O0OO0O00000O00 .get_nv ('instagram_comment')
					if OO000O00OOO0O000O ==False :
						print (f'{red}Không Get Được Nhiệm Vụ Comment              ',end ='\r');sleep (2 );print (f'                                                        ',end ='\r')
						O0O00O0O00OOO000O =0 
					elif 'error'in OO000O00OOO0O000O .text :
						if OO000O00OOO0O000O .json ()['error']=='Thao tác quá nhanh vui lòng chậm lại':
							OO00000O000OO0OOO =OO000O00OOO0O000O .json ()['countdown']
							print (f'{red}Đang Get Nhiệm Vụ Comment, COUNTDOWN: {str(round(OO00000O000OO0OOO, 3))}              ',end ='\r');sleep (2 );print (f'                                                       ',end ='\r')
						else :
							print (OO000O00OOO0O000O .json ()['error'],end ='\r')
						O0O00O0O00OOO000O =0 
					else :
						try :
							OO000O00OOO0O000O =OO000O00OOO0O000O .json ()['data']
						except :
							print (f'{red}Không Get Được Nhiệm Vụ Comment              ',end ='\r');sleep (2 );print (f'                                                        ',end ='\r')
							O0O00O0O00OOO000O =0 ;OO000O00OOO0O000O =[]
						if len (OO000O00OOO0O000O )==0 :
							print (f'{red}Hết Nhiệm Vụ Comment                             ',end ='\r');sleep (2 );print (f'                                                        ',end ='\r')
							O0O00O0O00OOO000O =0 
						else :
							print (f'{luc}Tìm Thấy {vang}{len(OO000O00OOO0O000O)}{luc} Nhiệm Vụ Comment                       ',end ='\r');sleep (2 );print (f'                                                        ',end ='\r')
							for O00OOOOOO00OOO00O in OO000O00OOO0O000O :
								OOO00O000O0OOO000 =O00OOOOOO00OOO00O ['id']
								OOO0OO00OO00OOO00 =O00OOOOOO00OOO00O ['link']
								OO0OOO000O000OO00 =O00OOOOOO00OOO00O ['noidung']
								OOOOOOO0OO0000O00 =OOO00O000O0OOO000 .split ('_')[0 ]if '_'in OOO00O000O0OOO000 else OOO00O000O0OOO000 
								OO0OO000O00000O00 =OOOO0OO00O000OO00 .cmt (OO0OOO000O000OO00 ,OOOOOOO0OO0000O00 )
								if OO0OO000O00000O00 ==False :
									O0OOO00OO0OOO0OO0 (OOO00O000O0OOO000 ,'COMMENT')
									O0O0O0O0OO0OOOO0O =OO0O0OO0O00000O00 .nhan_xu ('INS_COMMENT_CACHE',OOO00O000O0OOO000 )
									O0OOO00O0OOO0O0OO +=1 
								else :
									O0O0O0O0OO0OOOO0O =OO0O0OO0O00000O00 .nhan_xu ('INS_COMMENT_CACHE',OOO00O000O0OOO000 )
									try :
										O0OOO00O0000000OO =O0O0O0O0OO0OOOO0O [1 ]
										OO0OOO000O000OO00 =O0O0O0O0OO0OOOO0O [0 ]
										OO0000OO0O0OO0OOO +=1 
										OO000000O000OOO00 (OO0000OO0O0OO0OOO ,OOO00O000O0OOO000 ,'COMMENT',OO0OOO000O000OO00 ,O0OOO00O0000000OO )
										O0OOO00O0OOO0O0OO =0 
										if OO0000OO0O0OO0OOO %O0O0OO0O0O0OO0OOO ==0 :
											OOO0O00OO0OOOOOO0 (14 );print (f'{lam}Số Xu Hiện Tại: {vang}{O0OOO00O0000000OO} {red}| {lam}Số Tài Khoản Instagram {vang}{len(O0OO0O00O0000000O)}');OOO0O00OO0OOOOOO0 (14 );OOOO0OO00OO00OO0O =1 ;break 
										if OO0000OO0O0OO0OOO %O0OOO0O0OOO00O0O0 ==0 :
											OOO00OO0000OOO00O (OOO000OO0OOOO0O0O )
										else :
											O0O0OO0OOO0OO00O0 (O0O00O0OO00000OOO ,O0O0000OOOOO0O00O )
									except :
										O0OOO00OO0OOO0OO0 (OOO00O000O0OOO000 ,'COMMENT')
										O0OOO00O0OOO0O0OO +=1 
								if O0OOO00O0OOO0O0OO >=5 :
									O00000O00O00O0000 =OOOO0OO00O000OO00 .name ()
									if O00000O00O00O0000 ==False :
										print (f'  {red}Cookie Tài Khoản {O0O000O0O00OOOOOO} Đã Bị Out !!!                ')
									else :
										print (f' {red}Tài Khoản {O0O000O0O00OOOOOO} Đã Bị Block Comment !!!					')
									O0OO0O00O0000000O .remove (OOOOOOOO0O0OOOO0O )
									OOOO0OO00OO00OO0O =1 
									break 
				if OOOO0OO00OO00OO0O ==1 :
					break 
				if OOO0O0OO00O0000O0 +O0O00O0O00OOO000O +O0OOOOO00OO00OOOO ==0 :
					for OOO0000OOO000OOOO in range (10 ,0 ,-1 ):
						print (f'{trang} Tất Cả Các Nhiệm Vụ Đã Hết, Vui Lòng Chờ {OOO0000OOO000OOOO} Giây ',end ='\r');sleep (1 );print (f'                                                        ',end ='\r')
OOO0O000000O00O00 ()