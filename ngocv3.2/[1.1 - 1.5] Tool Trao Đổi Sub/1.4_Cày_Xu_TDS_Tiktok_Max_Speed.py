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

import requests ,json 
import os 
from sys import platform 
from time import sleep 
from datetime import datetime 
from time import strftime 
from threading import Thread 
O0OO00OOO000O00O0 =0 
OOOOO0O00O00O00OO ='mb'if platform [0 :3 ]=='lin'else 'pc'
O0OO00000OO00OO00 =0 
def OO0O000O00OOO0OOO (O0O00O0O0O000O0O0 ):
	for O0O0OOOO0000O0000 in range (O0O00O0O0O000O0O0 ):
		print (red +'────',end ='')
	print ('')
class OOO0O0OOOOO000O0O (object ):
	def __init__ (OOOOO0O000OOO0000 ,O0OO0000O0OO0O00O ):
		OOOOO0O000OOO0000 .token =O0OO0000O0OO0O00O 
	def main (OOO0O0O00O0O000OO ):
		try :
			O00OO000O000OOO00 =requests .get ('https://traodoisub.com/api/?fields=profile&access_token='+OOO0O0O00O0O000OO .token ).json ()
			try :
				return O00OO000O000OOO00 ['data']
			except :
				False 
		except :
			return False 
	def run (OOOO00OO000OOO0OO ,OOO0OOOO0OO00O0OO ):
		try :
			OO0OOO0O000O000O0 =requests .get (f'https://traodoisub.com/api/?fields=tiktok_run&id={OOO0OOOO0OO00O0OO}&access_token={OOOO00OO000OOO0OO.token}').json ()
			try :
				return OO0OOO0O000O000O0 ['data']
			except :
				return False 
		except :
			return False 
	def get_job (O0O000O00OO000000 ,O0OO0O00O0O00O000 ):
		try :
			OOO00O000O0O0O000 =requests .get (f'https://traodoisub.com/api/?fields={O0OO0O00O0O00O000}&access_token={O0O000O00OO000000.token}')
			return OOO00O000O0O0O000 
		except :
			return False 
	def cache (O0OOO00OOO0000OO0 ,OO0000O00OO00OOO0 ,OO00000000O000O0O ,O00OOOO0000O00OOO ):
		global O0OO00000OO00OO00 
		O0OO00000OO00OO00 +=1 
		try :
			OO0OOO00OO00O0O00 =requests .get (f'https://traodoisub.com/api/coin/?type={OO00000000O000O0O}&id={OO0000O00OO00OOO0}&access_token={O0OOO00OOO0000OO0.token}').json ()
			OO0OOO00OO00O0O00 ['cache']
		except :
			pass 
		OOO0O0OO000O00OOO =datetime .now ().strftime ('%H:%M:%S')
		print (f'{vang}[{trang}{O0OO00000OO00OO00}{vang}] {red}| {lam}{OOO0O0OO000O00OOO} {red}| {Colorate.Horizontal(Colors.yellow_to_red, O00OOOO0000O00OOO)} {red}| {trang}{OO0000O00OO00OOO0} {red}|')
	def nhan_xu (O0OOOO000OO000OOO ,OOO0OOOOOO0000OOO ,OO000000OO00OO00O ):
		try :
			O00000OO0O0OOOO0O =requests .get (f'https://traodoisub.com/api/coin/?type={OO000000OO00OO00O}&id={OOO0OOOOOO0000OOO}&access_token={O0OOOO000OO000OOO.token}')
			try :
				O0O0O0OO0OOOO000O =O00000OO0O0OOOO0O .json ()['data']['xu']
				O0OOOO000O00O00OO =O00000OO0O0OOOO0O .json ()['data']['msg']
				OOO00O0O0O00OOO00 =O00000OO0O0OOOO0O .json ()['data']['job_success']
				OOOOO00O000OO0000 =O00000OO0O0OOOO0O .json ()['data']['xu_them']
				global O0OO00OOO000O00O0 
				O0OO00OOO000O00O0 +=OOOOO00O000OO0000 
				OO0O000O00OOO0OOO (14 )
				print (f'{lam}Nhận Thành Công {OOO00O0O0O00OOO00} Nhiệm Vụ {red}| {luc}{O0OOOO000O00O00OO} {red}| {luc}TOTAL {vang}{O0OO00OOO000O00O0} {luc}Xu {red}| {vang}{O0O0O0OO0OOOO000O} ')
				OO0O000O00OOO0OOO (14 )
				if OOO00O0O0O00OOO00 ==0 :
					return True 
			except :
				if '"code":"error","msg"'in O00000OO0O0OOOO0O .text :
					OO0OO00O0O000000O =O00000OO0O0OOOO0O .json ()['msg'];print (red +OO0OO00O0O000000O )
				elif '"error":'in O00000OO0O0OOOO0O .text :
					OO0OO00O0O000000O =O00000OO0O0OOOO0O .json ()['error'];print (red +OO0OO00O0O000000O )
				else :
					print (red +'Nhận Xu Thất Bại, Vui Lòng Thử Lại !')
				return False 
		except :
			print (red +'Nhận Xu Thất Bại, Vui Lòng Thử Lại !')
			return False 
def OOOO0OOO0O0000O00 (O000000OO0000000O ):
  try :
    for OOO000O0O0O00OOOO in range (O000000OO0000000O ,-1 ,-1 ):
       print (f'{vang}[{trang}NGOCTOOL{vang}][{trang}'+str (OOO000O0O0O00OOOO )+vang +']           ',end ='\r')
       sleep (1 )
  except :
     sleep (O000000OO0000000O )
     print (O000000OO0000000O ,end ='\r')
def O0OO000O0OOOOOO0O (OOO00O0OOOO0OO0O0 ,O0O00OOO0OO0O0000 ):
	if O0O00OOO0OO0O0000 =='mb':
		os .system (f'xdg-open {OOO00O0OOOO0OO0O0}')
	else :
		os .system (f'cmd /c start {OOO00O0OOOO0OO0O0}')
def OOO0OO0OO00O0O00O ():
	global O0OO00000OO00OO00 
	banner ()
	while True :
		if os .path .exists ('configtds.txt'):
			with open ('configtds.txt','r')as O00OO00OOO000OO00 :
				OOOO00OOOO0OOOOO0 =O00OO00OOO000OO00 .read ()
			O000O000OO0OOOOO0 =OOO0O0OOOOO000O0O (OOOO00OOOO0OOOOO0 )
			OO00O000O0O00O00O =O000O000OO0OOOOO0 .main ()
			try :
				print (f'{thanh_xau}{luc}Nhập {vang}[{trang}1{vang}] {luc}Giữ Lại Tài Khoản '+vang +OO00O000O0O00O00O ['user'])
				print (f'{thanh_xau}{luc}Nhập {vang}[{trang}2{vang}] {luc}Nhập Access_Token TDS Mới')
				O0O00000O0O000OO0 =input (f'{thanh_xau}{luc}Nhập {trang}===>: {vang}')
				if O0O00000O0O000OO0 =='2':
					os .remove ('configtds.txt')
				elif O0O00000O0O000OO0 =='1':
					pass 
				else :
					print (red +'Lựa chọn không xác định !!!');OO0O000O00OOO0OOO (14 )
					continue 
			except :
				os .remove ('configtds.txt')
		if not os .path .exists ('configtds.txt'):
			OOOO00OOOO0OOOOO0 =input (f'{thanh_xau}{luc}Nhập Access_Token TDS: {vang}')
			with open ('configtds.txt','w')as O00OO00OOO000OO00 :
				O00OO00OOO000OO00 .write (OOOO00OOOO0OOOOO0 )
		with open ('configtds.txt','r')as O00OO00OOO000OO00 :
			OOOO00OOOO0OOOOO0 =O00OO00OOO000OO00 .read ()
		O000O000OO0OOOOO0 =OOO0O0OOOOO000O0O (OOOO00OOOO0OOOOO0 )
		OO00O000O0O00O00O =O000O000OO0OOOOO0 .main ()
		try :
			O0OOO000O0O0OOO0O =OO00O000O0O00O00O ['xu']
			O00OO000OOOOO000O =OO00O000O0O00O00O ['xudie']
			OOOO00OOO00000OOO =OO00O000O0O00O00O ['user']
			print (lam +' Đăng Nhập Thành Công ')
			break 
		except :
			print (red +'Access Token Không Hợp Lệ! Xin Thử Lại ')
			os .remove ('configtds.txt')
			continue 
	OO0O000O00OOO0OOO (14 )
	banner ()
	print (f'{thanh_xau}{luc}Tên Tài Khoản: {vang}{OOOO00OOO00000OOO} ')
	print (f'{thanh_xau}{luc}Xu Hiện Tại: {vang}{O0OOO000O0O0OOO0O}')
	print (f'{thanh_xau}{luc}Xu Bị Phạt: {vang}{O00OO000OOOOO000O} ')
	while True :
		OOOOOOO0000O00O00 =0 
		OO0O000O00OOO0OOO (14 )
		print (f'{thanh_xau}{luc}Nhập {red}[{vang}1{red}] {luc}Để Chạy Nhiệm Vụ Tim')
		print (f'{thanh_xau}{luc}Nhập {red}[{vang}2{red}] {luc}Để Chạy Nhiệm Vụ Follow')
		print (f'{thanh_xau}{luc}Nhập {red}[{vang}3{red}] {luc}Để Chạy Nhiệm Vụ Follow Tiktok Now')
		OOO0O0OOOO0OO0OO0 =input (f'{thanh_xau}{luc}Nhập Số Để Chạy Nhiệm Vụ: {vang}')
		O0O00O0OOO00000O0 =int (input (f'{thanh_xau}{luc}Nhập Delay: {vang}'))
		while True :
			if OOOOOOO0000O00O00 ==2 :
				break 
			OOOOOOO0000O00O00 =0 
			OO0O000O00OOO0OOO (14 )
			OOOOOOOO0OOOO0O0O =int (input (f'{thanh_xau}{luc}Sau Bao Nhiêu Nhiệm Vụ Thì Nhận Xu: {vang}'))
			if OOOOOOOO0OOOO0O0O <8 :
				print (red +'Trên 8 Nhiệm Vụ Mới Được Nhận Tiền!')
				continue 
			"""if nv_nhan > 15:
				print(red+'Nhận Xu Dưới 15 Nhiệm Vụ Để Tránh Lỗi')
				continue"""
			OOO0O0OOOO00O000O =input (f'{thanh_xau}{luc}Nhập User Name Tik Tok Cần Cấu Hình: {vang}')
			O00O0O00O0OOOOO0O =O000O000OO0OOOOO0 .run (OOO0O0OOOO00O000O )
			if O00O0O00O0OOOOO0O !=False :
				OOOO00OOO00000OOO =O00O0O00O0OOOOO0O ['uniqueID']
				O00OO0OOOO000O0O0 =O00O0O00O0OOOOO0O ['id']
				OO0O000O00OOO0OOO (14 )
				print (f'{luc}Đang Cấu Hình ID: {vang}{O00OO0OOOO000O0O0} {red}| {luc}User: {vang}{OOOO00OOO00000OOO} {red}| ')
				OO0O000O00OOO0OOO (14 )
			else :
				print (f'{red}Cấu Hinh Thất Bại User: {vang}{OOO0O0OOOO00O000O} ')
				continue 
			while True :
				if OOOOOOO0000O00O00 ==1 or OOOOOOO0000O00O00 ==2 :break 
				if '1'in OOO0O0OOOO0OO0OO0 :
					O0OOO00O000O0OOOO =O000O000OO0OOOOO0 .get_job ('tiktok_like')
					if O0OOO00O000O0OOOO ==False :
						print (red +'Không Get Được Nhiệm Vụ Like              ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
					elif '"error":'in O0OOO00O000O0OOOO .text :
						if O0OOO00O000O0OOOO .json ()['error']=='Thao tác quá nhanh vui lòng chậm lại':
							O000OOO00O0O0O0O0 =O0OOO00O000O0OOOO .json ()['countdown']
							print (f'{red}Đang Get Nhiệm Vụ Like, COUNTDOWN: {str(round(O000OOO00O0O0O0O0, 3))} ',end ='\r');sleep (2 );print ('                                                       ',end ='\r')
						elif O0OOO00O000O0OOOO .json ()['error']=='Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							O000OO0O0000O0O0O =O000O000OO0OOOOO0 .nhan_xu ('TIKTOK_LIKE_API','TIKTOK_LIKE')
						else :
							print (red +O0OOO00O000O0OOOO .json ()['error'],end ='\r');sleep (2 );print ('                                                        ',end ='\r')
					else :
						try :
							O0OOO00O000O0OOOO =O0OOO00O000O0OOOO .json ()['data']
						except :
							print (red +'Hết Nhiệm Vụ Like                             ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
							continue 
						if len (O0OOO00O000O0OOOO )==0 :
							print (red +'Hết Nhiệm Vụ Like                             ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
						else :
							print (f'{luc}Tìm Thấy {vang}{len(O0OOO00O000O0OOOO)} {luc}Nhiệm Vụ Like                       ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
							for O00000O00O00O000O in O0OOO00O000O0OOOO :
								OOO0OOOOOOO000OOO =O00000O00O00O000O ['id']
								O000000O000O0O00O =O00000O00O00O000O ['link']
								Thread (target =O0OO000O0OOOOOO0O ,args =(O000000O000O0O00O ,OOOOO0O00O00O00OO )).start ()
								Thread (target =O000O000OO0OOOOO0 .cache ,args =(OOO0OOOOOOO000OOO ,'TIKTOK_LIKE_CACHE','TIM')).start ()
								OOOO0OOO0O0000O00 (O0O00O0OOO00000O0 )
								if O0OO00000OO00OO00 %OOOOOOOO0OOOO0O0O ==0 :
									O000OO0O0000O0O0O =O000O000OO0OOOOO0 .nhan_xu ('TIKTOK_LIKE_API','TIKTOK_LIKE')
									if O000OO0O0000O0O0O ==True :
										print (luc +'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ')
										print (f'{thanh_xau}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
										print (f'{thanh_xau}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
										print (f'{thanh_xau}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
										O0O00000O0O000OO0 =input (f'{thanh_xau}{luc}Nhập {trang}===>: {vang}')
										if O0O00000O0O000OO0 =='1':
											OOOOOOO0000O00O00 =2 
											break 
										elif O0O00000O0O000OO0 =='2':
											OOOOOOO0000O00O00 =1 
											break 
										OO0O000O00OOO0OOO (14 )
				if OOOOOOO0000O00O00 ==1 or OOOOOOO0000O00O00 ==2 :break 
				if '2'in OOO0O0OOOO0OO0OO0 :
					O0O0O0O0000O0OO00 =O000O000OO0OOOOO0 .get_job ('tiktok_follow')
					if O0O0O0O0000O0OO00 ==False :
						print (red +'Không Get Được Nhiệm Vụ Follow              ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
					elif '"error":'in O0O0O0O0000O0OO00 .text :
						if O0O0O0O0000O0OO00 .json ()['error']=='Thao tác quá nhanh vui lòng chậm lại':
							O000OOO00O0O0O0O0 =O0O0O0O0000O0OO00 .json ()['countdown']
							print (red +f'Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(O000OOO00O0O0O0O0, 3))} ',end ='\r');sleep (2 );print ('                                                       ',end ='\r')
						elif O0O0O0O0000O0OO00 .json ()['error']=='Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							O000OO0O0000O0O0O =O000O000OO0OOOOO0 .nhan_xu ('TIKTOK_FOLLOW_API','TIKTOK_FOLLOW')
						else :
							print (red +O0O0O0O0000O0OO00 .json ()['error'],end ='\r');sleep (2 );print ('                                                        ',end ='\r')
					else :
						try :
							O0O0O0O0000O0OO00 =O0O0O0O0000O0OO00 .json ()['data']
						except :
							print (red +'Hết Nhiệm Vụ Follow                             ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
							continue 
						if len (O0O0O0O0000O0OO00 )==0 :
							print (red +'Hết Nhiệm Vụ Follow                             ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
						else :
							print (luc +f'Tìm Thấy {vang}{len(O0O0O0O0000O0OO00)} {luc}Nhiệm Vụ Follow                       ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
							for O00000O00O00O000O in O0O0O0O0000O0OO00 :
								OOO0OOOOOOO000OOO =O00000O00O00O000O ['id']
								O000000O000O0O00O =O00000O00O00O000O ['link']
								Thread (target =O0OO000O0OOOOOO0O ,args =(O000000O000O0O00O ,OOOOO0O00O00O00OO )).start ()
								Thread (target =O000O000OO0OOOOO0 .cache ,args =(OOO0OOOOOOO000OOO ,'TIKTOK_FOLLOW_CACHE','FOLLOW')).start ()
								OOOO0OOO0O0000O00 (O0O00O0OOO00000O0 )
								if O0OO00000OO00OO00 %OOOOOOOO0OOOO0O0O ==0 :
									O000OO0O0000O0O0O =O000O000OO0OOOOO0 .nhan_xu ('TIKTOK_FOLLOW_API','TIKTOK_FOLLOW')
									if O000OO0O0000O0O0O ==True :
										print (luc +'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ')
										print (f'{thanh_xau}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
										print (f'{thanh_xau}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
										print (f'{thanh_xau}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
										O0O00000O0O000OO0 =input (f'{thanh_xau}{luc}Nhập {trang}===>: {vang}')
										if O0O00000O0O000OO0 =='1':
											OOOOOOO0000O00O00 =2 
											break 
										elif O0O00000O0O000OO0 =='2':
											OOOOOOO0000O00O00 =1 
											break 
										OO0O000O00OOO0OOO (14 )
				if OOOOOOO0000O00O00 ==1 or OOOOOOO0000O00O00 ==2 :break 
				if '3'in OOO0O0OOOO0OO0OO0 :
					O0O0O0O0000O0OO00 =O000O000OO0OOOOO0 .get_job ('tiktok_follow')
					if O0O0O0O0000O0OO00 ==False :
						print (red +'Không Get Được Nhiệm Vụ Follow              ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
					elif '"error":'in O0O0O0O0000O0OO00 .text :
						if O0O0O0O0000O0OO00 .json ()['error']=='Thao tác quá nhanh vui lòng chậm lại':
							O000OOO00O0O0O0O0 =O0O0O0O0000O0OO00 .json ()['countdown']
							print (f'{red}Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(O000OOO00O0O0O0O0, 3))} ',end ='\r');sleep (2 );print ('                                                       ',end ='\r')
						elif O0O0O0O0000O0OO00 .json ()['error']=='Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							O000OO0O0000O0O0O =O000O000OO0OOOOO0 .nhan_xu ('TIKTOK_FOLLOW_API','TIKTOK_FOLLOW')
						else :
							print (red +O0O0O0O0000O0OO00 .json ()['error'],end ='\r');sleep (2 );print ('                                                        ',end ='\r')
					else :
						try :
							O0O0O0O0000O0OO00 =O0O0O0O0000O0OO00 .json ()['data']
						except :
							print (red +'Hết Nhiệm Vụ Follow                             ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
							continue 
						if len (O0O0O0O0000O0OO00 )==0 :
							print (red +'Hết Nhiệm Vụ Follow                             ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
						else :
							print (f'{luc}Tìm Thấy {vang}{len(O0O0O0O0000O0OO00)} {luc}Nhiệm Vụ Follow                       ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
							for O00000O00O00O000O in O0O0O0O0000O0OO00 :
								OOO0OOOOOOO000OOO =O00000O00O00O000O ['id']
								O0OOOO0OOO00000O0 =OOO0OOOOOOO000OOO .split ('_')[0 ]
								O000000O000O0O00O =O00000O00O00O000O ['link']
								OOOOO00OOOOOO0O0O =O00000O00O00O000O ['uniqueID']
								if OOOOO0O00O00O00OO =='mb':
									Thread (target =O0OO000O0OOOOOO0O ,args =(f'tiktoknow://user/profile?user_id={O0OOOO0OOO00000O0}',OOOOO0O00O00O00OO )).start ()
								else :
									Thread (target =O0OO000O0OOOOOO0O ,args =(f'https://now.tiktok.com/@{OOOOO00OOOOOO0O0O}',OOOOO0O00O00O00OO )).start ()
								Thread (target =O000O000OO0OOOOO0 .cache ,args =(OOO0OOOOOOO000OOO ,'TIKTOK_FOLLOW_CACHE','FOLLOW_TIKTOK_NOW')).start ()
								OOOO0OOO0O0000O00 (O0O00O0OOO00000O0 )
								if O0OO00000OO00OO00 %OOOOOOOO0OOOO0O0O ==0 :
									O000OO0O0000O0O0O =O000O000OO0OOOOO0 .nhan_xu ('TIKTOK_FOLLOW_API','TIKTOK_FOLLOW')
									if O000OO0O0000O0O0O ==True :
										print (luc +'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ')
										print (f'{thanh_xau}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
										print (f'{thanh_xau}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
										print (f'{thanh_xau}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
										O0O00000O0O000OO0 =input (f'{thanh_xau}{luc}Nhập {trang}===>: {vang}')
										if O0O00000O0O000OO0 =='1':
											OOOOOOO0000O00O00 =2 
											break 
										elif O0O00000O0O000OO0 =='2':
											OOOOOOO0000O00O00 =1 
											break 
										OO0O000O00OOO0OOO (14 )
OOO0OO0OO00O0O00O ()