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
O00O00OOO0O000OO0 =0 
OO000000OOO0O0O0O ='mb'if platform [0 :3 ]=='lin'else 'pc'
def OO0OOOOOO00O00000 (OO0O0OOOOO0O0000O ):
	for O00O0O0000OO0O0O0 in range (OO0O0OOOOO0O0000O ):
		print (red +'────',end ='')
	print ('')
class O00O0O0OOOO0O0OOO (object ):
	def __init__ (OOO0OOO00O00O00OO ,OO0OO0OO0OO0O000O ):
		OOO0OOO00O00O00OO .token =OO0OO0OO0OO0O000O 
	def main (O0O0OOOO0O0OOOOO0 ):
		try :
			O00OO0OOOO00O0OO0 =requests .get ('https://traodoisub.com/api/?fields=profile&access_token='+O0O0OOOO0O0OOOOO0 .token ).json ()
			try :
				return O00OO0OOOO00O0OO0 ['data']
			except :
				False 
		except :
			return False 
	def run (OOOOOOOO000OO000O ,O0000OO00000O00O0 ):
		try :
			O0O00OO0OOOO0O0O0 =requests .get (f'https://traodoisub.com/api/?fields=tiktok_run&id={O0000OO00000O00O0}&access_token={OOOOOOOO000OO000O.token}').json ()
			try :
				return O0O00OO0OOOO0O0O0 ['data']
			except :
				return False 
		except :
			return False 
	def get_job (OOO000O0OO00000O0 ,O000OOO0O00OO0O0O ):
		try :
			OO0O000OOO0OOOOOO =requests .get (f'https://traodoisub.com/api/?fields={O000OOO0O00OO0O0O}&access_token={OOO000O0OO00000O0.token}')
			return OO0O000OOO0OOOOOO 
		except :
			return False 
	def cache (OO00O0O00OO00O00O ,O0O000O00OO0O0O00 ,O0OOOOOO0O00O0OOO ):
		try :
			O0OO0O0000O0OOO0O =requests .get (f'https://traodoisub.com/api/coin/?type={O0OOOOOO0O00O0OOO}&id={O0O000O00OO0O0O00}&access_token={OO00O0O00OO00O00O.token}').json ()
			try :
				O0OO0O0000O0OOO0O ['cache']
				return True 
			except :
				return False 
		except :
			return False 
	def nhan_xu (OO0O0OO0OO0000000 ,O0O0O000O0OO00O00 ,OO000OOOO0O0O000O ):
		try :
			OO0OOO0OO0000O000 =requests .get (f'https://traodoisub.com/api/coin/?type={OO000OOOO0O0O000O}&id={O0O0O000O0OO00O00}&access_token={OO0O0OO0OO0000000.token}')
			try :
				O0000000000OO0000 =OO0OOO0OO0000O000 .json ()['data']['xu']
				O00000OOOOOOO0O00 =OO0OOO0OO0000O000 .json ()['data']['msg']
				O00000O0000O0000O =OO0OOO0OO0000O000 .json ()['data']['job_success']
				OO0OO0OO00OOO0O00 =OO0OOO0OO0000O000 .json ()['data']['xu_them']
				global O00O00OOO0O000OO0 
				O00O00OOO0O000OO0 +=OO0OO0OO00OOO0O00 
				OO0OOOOOO00O00000 (14 )
				print (f'{lam}Nhận Thành Công {O00000O0000O0000O} Nhiệm Vụ {red}| {luc}{O00000OOOOOOO0O00} {red}| {luc}TOTAL {vang}{O00O00OOO0O000OO0} {luc}Xu {red}| {vang}{O0000000000OO0000} ')
				OO0OOOOOO00O00000 (14 )
				if O00000O0000O0000O ==0 :
					return True 
			except :
				if '"code":"error","msg"'in OO0OOO0OO0000O000 .text :
					O000O00OOOO000O0O =OO0OOO0OO0000O000 .json ()['msg'];print (red +O000O00OOOO000O0O )
				elif '"error":'in OO0OOO0OO0000O000 .text :
					O000O00OOOO000O0O =OO0OOO0OO0000O000 .json ()['error'];print (red +O000O00OOOO000O0O )
				else :
					print (red +'Nhận Xu Thất Bại, Vui Lòng Thử Lại !')
				return False 
		except :
			print (red +'Nhận Xu Thất Bại, Vui Lòng Thử Lại !')
			return False 
def OOOO00OOO00O0O0OO (O0000O00O0OOO0O0O ):
  try :
    for O0000OO0O00O000OO in range (O0000O00O0OOO0O0O ,-1 ,-1 ):
       print (f'{vang}[{trang}NGOCTOOL{vang}][{trang}'+str (O0000OO0O00O000OO )+vang +']           ',end ='\r')
       sleep (1 )
  except :
     sleep (O0000O00O0OOO0O0O )
     print (O0000O00O0OOO0O0O ,end ='\r')
def O000000OO0000O00O (OO0000OOO0O00OO00 ,OOOOO00OO0OO0OOOO ):
	if OOOOO00OO0OO0OOOO =='mb':
		os .system (f'xdg-open {OO0000OOO0O00OO00}')
	else :
		os .system (f'cmd /c start {OO0000OOO0O00OO00}')
def OOOO00O0OOOO00000 ():
	OOO000O0OO00OO000 =0 
	banner ()
	while True :
		if os .path .exists ('configtds.txt'):
			with open ('configtds.txt','r')as OO0O0000O00O0OO0O :
				O000OO0OOO0OO00O0 =OO0O0000O00O0OO0O .read ()
			O00000OOO0O0O00OO =O00O0O0OOOO0O0OOO (O000OO0OOO0OO00O0 )
			OOOOO0O0O0O0OOOOO =O00000OOO0O0O00OO .main ()
			try :
				print (f'{thanh_xau}{luc}Nhập {vang}[{trang}1{vang}] {luc}Giữ Lại Tài Khoản '+vang +OOOOO0O0O0O0OOOOO ['user'])
				print (f'{thanh_xau}{luc}Nhập {vang}[{trang}2{vang}] {luc}Nhập Access_Token TDS Mới')
				OOOO0OOO0O0O0000O =input (f'{thanh_xau}{luc}Nhập {trang}===>: {vang}')
				if OOOO0OOO0O0O0000O =='2':
					os .remove ('configtds.txt')
				elif OOOO0OOO0O0O0000O =='1':
					pass 
				else :
					print (red +'Lựa chọn không xác định !!!');OO0OOOOOO00O00000 (14 )
					continue 
			except :
				os .remove ('configtds.txt')
		if not os .path .exists ('configtds.txt'):
			O000OO0OOO0OO00O0 =input (f'{thanh_xau}{luc}Nhập Access_Token TDS: {vang}')
			with open ('configtds.txt','w')as OO0O0000O00O0OO0O :
				OO0O0000O00O0OO0O .write (O000OO0OOO0OO00O0 )
		with open ('configtds.txt','r')as OO0O0000O00O0OO0O :
			O000OO0OOO0OO00O0 =OO0O0000O00O0OO0O .read ()
		O00000OOO0O0O00OO =O00O0O0OOOO0O0OOO (O000OO0OOO0OO00O0 )
		OOOOO0O0O0O0OOOOO =O00000OOO0O0O00OO .main ()
		try :
			O0OO00OOOOO00OOO0 =OOOOO0O0O0O0OOOOO ['xu']
			OO0O0OO0O00O00O00 =OOOOO0O0O0O0OOOOO ['xudie']
			O0O00O00O0OOOOOO0 =OOOOO0O0O0O0OOOOO ['user']
			print (lam +' Đăng Nhập Thành Công ')
			break 
		except :
			print (red +'Access Token Không Hợp Lệ! Xin Thử Lại ')
			os .remove ('configtds.txt')
			continue 
	OO0OOOOOO00O00000 (14 )
	banner ()
	print (f'{thanh_xau}{luc}Tên Tài Khoản: {vang}{O0O00O00O0OOOOOO0} ')
	print (f'{thanh_xau}{luc}Xu Hiện Tại: {vang}{O0OO00OOOOO00OOO0}')
	print (f'{thanh_xau}{luc}Xu Bị Phạt: {vang}{OO0O0OO0O00O00O00} ')
	while True :
		OO000O0O000000O00 =0 
		OO0OOOOOO00O00000 (14 )
		print (f'{thanh_xau}{luc}Nhập {red}[{vang}1{red}] {luc}Để Chạy Nhiệm Vụ Tim')
		print (f'{thanh_xau}{luc}Nhập {red}[{vang}2{red}] {luc}Để Chạy Nhiệm Vụ Follow')
		print (f'{thanh_xau}{luc}Nhập {red}[{vang}3{red}] {luc}Để Chạy Nhiệm Vụ Follow Tiktok Now')
		OOO0OOO00O000O00O =input (f'{thanh_xau}{luc}Nhập Số Để Chạy Nhiệm Vụ: {vang}')
		OO00OO0O0O000O0O0 =int (input (f'{thanh_xau}{luc}Nhập Delay: {vang}'))
		while True :
			if OO000O0O000000O00 ==2 :
				break 
			OO000O0O000000O00 =0 
			OO0OOOOOO00O00000 (14 )
			OOOOOOO000OO00O0O =int (input (f'{thanh_xau}{luc}Sau Bao Nhiêu Nhiệm Vụ Thì Nhận Xu: {vang}'))
			if OOOOOOO000OO00O0O <8 :
				print (red +'Trên 8 Nhiệm Vụ Mới Được Nhận Tiền!')
				continue 
			"""if nv_nhan > 15:
				print(red+'Nhận Xu Dưới 15 Nhiệm Vụ Để Tránh Lỗi')
				continue"""
			O0O0000O00O0O0OOO =input (f'{thanh_xau}{luc}Nhập User Name Tik Tok Cần Cấu Hình: {vang}')
			OOOO0O00O00O0O000 =O00000OOO0O0O00OO .run (O0O0000O00O0O0OOO )
			if OOOO0O00O00O0O000 !=False :
				O0O00O00O0OOOOOO0 =OOOO0O00O00O0O000 ['uniqueID']
				O00O00OO000000O0O =OOOO0O00O00O0O000 ['id']
				OO0OOOOOO00O00000 (14 )
				print (f'{luc}Đang Cấu Hình ID: {vang}{O00O00OO000000O0O} {red}| {luc}User: {vang}{O0O00O00O0OOOOOO0} {red}| ')
				OO0OOOOOO00O00000 (14 )
			else :
				print (f'{red}Cấu Hinh Thất Bại User: {vang}{O0O0000O00O0O0OOO} ')
				continue 
			while True :
				if OO000O0O000000O00 ==1 or OO000O0O000000O00 ==2 :break 
				if '1'in OOO0OOO00O000O00O :
					O0O0OO0OOO0OO0O0O =O00000OOO0O0O00OO .get_job ('tiktok_like')
					if O0O0OO0OOO0OO0O0O ==False :
						print (red +'Không Get Được Nhiệm Vụ Like              ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
					elif '"error":'in O0O0OO0OOO0OO0O0O .text :
						if O0O0OO0OOO0OO0O0O .json ()['error']=='Thao tác quá nhanh vui lòng chậm lại':
							OOOOOO000OOOO00O0 =O0O0OO0OOO0OO0O0O .json ()['countdown']
							print (f'{red}Đang Get Nhiệm Vụ Like, COUNTDOWN: {str(round(OOOOOO000OOOO00O0, 3))} ',end ='\r');sleep (2 );print ('                                                       ',end ='\r')
						elif O0O0OO0OOO0OO0O0O .json ()['error']=='Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							OO00O00OO0OO0OOOO =O00000OOO0O0O00OO .nhan_xu ('TIKTOK_LIKE_API','TIKTOK_LIKE')
						else :
							print (red +O0O0OO0OOO0OO0O0O .json ()['error'],end ='\r');sleep (2 );print ('                                                        ',end ='\r')
					else :
						try :
							O0O0OO0OOO0OO0O0O =O0O0OO0OOO0OO0O0O .json ()['data']
						except :
							print (red +'Hết Nhiệm Vụ Like                             ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
							continue 
						if len (O0O0OO0OOO0OO0O0O )==0 :
							print (red +'Hết Nhiệm Vụ Like                             ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
						else :
							print (f'{luc}Tìm Thấy {vang}{len(O0O0OO0OOO0OO0O0O)} {luc}Nhiệm Vụ Like                       ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
							for O00000O00O0OO00O0 in O0O0OO0OOO0OO0O0O :
								OOO0OOOOO0OOOOOO0 =O00000O00O0OO00O0 ['id']
								OOO00OOO0OOOOOOO0 =O00000O00O0OO00O0 ['link']
								O000000OO0000O00O (OOO00OOO0OOOOOOO0 ,OO000000OOO0O0O0O )
								O000OO0OOO00OO0O0 =O00000OOO0O0O00OO .cache (OOO0OOOOO0OOOOOO0 ,'TIKTOK_LIKE_CACHE')
								if O000OO0OOO00OO0O0 !=True :
									O0OOO0000O0O00O0O =datetime .now ().strftime ('%H:%M:%S')
									OOO00OO0000O0O0OO =f'{vang}[{red}X{vang}] {red}| {lam}{O0OOO0000O0O00O0O} {red}| {vang}TIM {red}| {trang}{OOO0OOOOO0OOOOOO0} {red}|';print (OOO00OO0000O0O0OO ,end ='\r');sleep (1 );print ('                                                                                        ',end ='\r')
								else :
									OOO000O0OO00OO000 +=1 
									O0OOO0000O0O00O0O =datetime .now ().strftime ('%H:%M:%S')
									print (f'{vang}[{trang}{OOO000O0OO00OO000}{vang}] {red}| {lam}{O0OOO0000O0O00O0O} {red}| {Colorate.Horizontal(Colors.yellow_to_red, "TIM")} {red}| {trang}{OOO0OOOOO0OOOOOO0} {red}|')
									OOOO00OOO00O0O0OO (OO00OO0O0O000O0O0 )
									if OOO000O0OO00OO000 %OOOOOOO000OO00O0O ==0 :
										OO00O00OO0OO0OOOO =O00000OOO0O0O00OO .nhan_xu ('TIKTOK_LIKE_API','TIKTOK_LIKE')
										if OO00O00OO0OO0OOOO ==True :
											print (luc +'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ')
											print (f'{thanh_xau}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
											print (f'{thanh_xau}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
											print (f'{thanh_xau}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
											OOOO0OOO0O0O0000O =input (f'{thanh_xau}{luc}Nhập {trang}===>: {vang}')
											if OOOO0OOO0O0O0000O =='1':
												OO000O0O000000O00 =2 
												break 
											elif OOOO0OOO0O0O0000O =='2':
												OO000O0O000000O00 =1 
												break 
											OO0OOOOOO00O00000 (14 )
				if OO000O0O000000O00 ==1 or OO000O0O000000O00 ==2 :break 
				if '2'in OOO0OOO00O000O00O :
					O000OOO00000OO0O0 =O00000OOO0O0O00OO .get_job ('tiktok_follow')
					if O000OOO00000OO0O0 ==False :
						print (red +'Không Get Được Nhiệm Vụ Follow              ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
					elif '"error":'in O000OOO00000OO0O0 .text :
						if O000OOO00000OO0O0 .json ()['error']=='Thao tác quá nhanh vui lòng chậm lại':
							OOOOOO000OOOO00O0 =O000OOO00000OO0O0 .json ()['countdown']
							print (red +f'Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(OOOOOO000OOOO00O0, 3))} ',end ='\r');sleep (2 );print ('                                                       ',end ='\r')
						elif O000OOO00000OO0O0 .json ()['error']=='Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							OO00O00OO0OO0OOOO =O00000OOO0O0O00OO .nhan_xu ('TIKTOK_FOLLOW_API','TIKTOK_FOLLOW')
						else :
							print (red +O000OOO00000OO0O0 .json ()['error'],end ='\r');sleep (2 );print ('                                                        ',end ='\r')
					else :
						try :
							O000OOO00000OO0O0 =O000OOO00000OO0O0 .json ()['data']
						except :
							print (red +'Hết Nhiệm Vụ Follow                             ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
							continue 
						if len (O000OOO00000OO0O0 )==0 :
							print (red +'Hết Nhiệm Vụ Follow                             ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
						else :
							print (luc +f'Tìm Thấy {vang}{len(O000OOO00000OO0O0)} {luc}Nhiệm Vụ Follow                       ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
							for O00000O00O0OO00O0 in O000OOO00000OO0O0 :
								OOO0OOOOO0OOOOOO0 =O00000O00O0OO00O0 ['id']
								OOO00OOO0OOOOOOO0 =O00000O00O0OO00O0 ['link']
								O000000OO0000O00O (OOO00OOO0OOOOOOO0 ,OO000000OOO0O0O0O )
								O000OO0OOO00OO0O0 =O00000OOO0O0O00OO .cache (OOO0OOOOO0OOOOOO0 ,'TIKTOK_FOLLOW_CACHE')
								if O000OO0OOO00OO0O0 !=True :
									O0OOO0000O0O00O0O =datetime .now ().strftime ('%H:%M:%S')
									OOO00OO0000O0O0OO =f'{vang}[{red}X{vang}] {red}| {lam}{O0OOO0000O0O00O0O} {red}| {vang}FOLLOW {red}| {trang}{OOO0OOOOO0OOOOOO0} {red}|';print (OOO00OO0000O0O0OO ,end ='\r');sleep (1 );print ('                                                                                        ',end ='\r')
								else :
									OOO000O0OO00OO000 +=1 
									O0OOO0000O0O00O0O =datetime .now ().strftime ('%H:%M:%S')
									print (f'{vang}[{trang}{OOO000O0OO00OO000}{vang}] {red}| {lam}{O0OOO0000O0O00O0O} {red}| {Colorate.Horizontal(Colors.yellow_to_red, "FOLLOW")} {red}| {trang}{OOO0OOOOO0OOOOOO0} {red}|')
									OOOO00OOO00O0O0OO (OO00OO0O0O000O0O0 )
									if OOO000O0OO00OO000 %OOOOOOO000OO00O0O ==0 :
										OO00O00OO0OO0OOOO =O00000OOO0O0O00OO .nhan_xu ('TIKTOK_FOLLOW_API','TIKTOK_FOLLOW')
										if OO00O00OO0OO0OOOO ==True :
											print (luc +'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ')
											print (f'{thanh_xau}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
											print (f'{thanh_xau}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
											print (f'{thanh_xau}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
											OOOO0OOO0O0O0000O =input (f'{thanh_xau}{luc}Nhập {trang}===>: {vang}')
											if OOOO0OOO0O0O0000O =='1':
												OO000O0O000000O00 =2 
												break 
											elif OOOO0OOO0O0O0000O =='2':
												OO000O0O000000O00 =1 
												break 
											OO0OOOOOO00O00000 (14 )
				if OO000O0O000000O00 ==1 or OO000O0O000000O00 ==2 :break 
				if '3'in OOO0OOO00O000O00O :
					O000OOO00000OO0O0 =O00000OOO0O0O00OO .get_job ('tiktok_follow')
					if O000OOO00000OO0O0 ==False :
						print (red +'Không Get Được Nhiệm Vụ Follow              ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
					elif '"error":'in O000OOO00000OO0O0 .text :
						if O000OOO00000OO0O0 .json ()['error']=='Thao tác quá nhanh vui lòng chậm lại':
							OOOOOO000OOOO00O0 =O000OOO00000OO0O0 .json ()['countdown']
							print (f'{red}Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(OOOOOO000OOOO00O0, 3))} ',end ='\r');sleep (2 );print ('                                                       ',end ='\r')
						elif O000OOO00000OO0O0 .json ()['error']=='Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							OO00O00OO0OO0OOOO =O00000OOO0O0O00OO .nhan_xu ('TIKTOK_FOLLOW_API','TIKTOK_FOLLOW')
						else :
							print (red +O000OOO00000OO0O0 .json ()['error'],end ='\r');sleep (2 );print ('                                                        ',end ='\r')
					else :
						try :
							O000OOO00000OO0O0 =O000OOO00000OO0O0 .json ()['data']
						except :
							print (red +'Hết Nhiệm Vụ Follow                             ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
							continue 
						if len (O000OOO00000OO0O0 )==0 :
							print (red +'Hết Nhiệm Vụ Follow                             ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
						else :
							print (f'{luc}Tìm Thấy {vang}{len(O000OOO00000OO0O0)} {luc}Nhiệm Vụ Follow                       ',end ='\r');sleep (2 );print ('                                                        ',end ='\r')
							for O00000O00O0OO00O0 in O000OOO00000OO0O0 :
								OOO0OOOOO0OOOOOO0 =O00000O00O0OO00O0 ['id']
								O000OOO0OOO0OOOO0 =OOO0OOOOO0OOOOOO0 .split ('_')[0 ]
								OOO00OOO0OOOOOOO0 =O00000O00O0OO00O0 ['link']
								OOO000O00O0OOO00O =O00000O00O0OO00O0 ['uniqueID']
								if OO000000OOO0O0O0O =='mb':
									O000000OO0000O00O (f'tiktoknow://user/profile?user_id={O000OOO0OOO0OOOO0}',OO000000OOO0O0O0O )
								else :
									O000000OO0000O00O (f'https://now.tiktok.com/@{OOO000O00O0OOO00O}',OO000000OOO0O0O0O )
								O000OO0OOO00OO0O0 =O00000OOO0O0O00OO .cache (OOO0OOOOO0OOOOOO0 ,'TIKTOK_FOLLOW_CACHE')
								if O000OO0OOO00OO0O0 !=True :
									O0OOO0000O0O00O0O =datetime .now ().strftime ('%H:%M:%S')
									OOO00OO0000O0O0OO =f'{vang}[{red}X{vang}] {red}| {lam}{O0OOO0000O0O00O0O} {red}| {vang}FOLLOW_TIKTOK_NOW {red}| {trang}{OOO0OOOOO0OOOOOO0} {red}|';print (OOO00OO0000O0O0OO ,end ='\r');sleep (1 );print ('                                                                                        ',end ='\r')
								else :
									OOO000O0OO00OO000 +=1 
									O0OOO0000O0O00O0O =datetime .now ().strftime ('%H:%M:%S')
									print (f'{vang}[{trang}{OOO000O0OO00OO000}{vang}] {red}| {lam}{O0OOO0000O0O00O0O} {red}| {Colorate.Horizontal(Colors.yellow_to_red, "FOLLOW_TIKTOK_NOW")} {red}| {trang}{OOO0OOOOO0OOOOOO0} {red}|')
									OOOO00OOO00O0O0OO (OO00OO0O0O000O0O0 )
									if OOO000O0OO00OO000 %OOOOOOO000OO00O0O ==0 :
										OO00O00OO0OO0OOOO =O00000OOO0O0O00OO .nhan_xu ('TIKTOK_FOLLOW_API','TIKTOK_FOLLOW')
										if OO00O00OO0OO0OOOO ==True :
											print (luc +'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ')
											print (f'{thanh_xau}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
											print (f'{thanh_xau}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
											print (f'{thanh_xau}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
											OOOO0OOO0O0O0000O =input (f'{thanh_xau}{luc}Nhập {trang}===>: {vang}')
											if OOOO0OOO0O0O0000O =='1':
												OO000O0O000000O00 =2 
												break 
											elif OOOO0OOO0O0O0000O =='2':
												OO000O0O000000O00 =1 
												break 
											OO0OOOOOO00O00000 (14 )
OOOO00O0OOOO00000 ()