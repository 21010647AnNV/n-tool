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

import requests, json, os, sys
from threading import Thread
import threading
from datetime import datetime
from time import strftime
from time import sleep
import random
camxuc=[]
dem=0


class Facebook:
	def __init__(self,cookie):
		self.cookie = cookie
		self.headers = {
			'authority': 'mbasic.facebook.com',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
			'cache-control': 'max-age=0',
			'cookie': cookie,
			'origin': 'https://www.facebook.com',
			'referer': 'https://www.facebook.com',
			'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
			}
			#continue 
	def get_thongtin(self):
		try:
			url=requests.get('https://mbasic.facebook.com/profile.php',headers=self.headers).url
			home = requests.get(url,headers=self.headers).text
			self.fb_dtsg = home.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
			self.jazoest = home.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
			ten = home.split('<title>')[1].split('</title>')[0]
			self.user_id = cookie.split('c_user=')[1].split(';')[0]
			print(f'Tên Facebook: {ten} | ID: {self.user_id} ', end='')
			sys.stdout.flush()
		except:
			print('Không Get Được Thông Tin ! ')
			return 0
	def get_pro5(self):
		headers={
           	     'authority': 'www.facebook.com',
            	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          	      'accept-language': 'vi',
       	         'cookie': self.cookie,
           	     'sec-ch-prefers-color-scheme': 'light',
            	    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            	    'sec-ch-ua-mobile': '?0',
          	      'sec-ch-ua-platform': '"Windows"',
          	      'sec-fetch-dest': 'document',
           	     'sec-fetch-mode': 'navigate',
           	     'sec-fetch-site': 'none',
           	     'sec-fetch-user': '?1',
             	   'upgrade-insecure-requests': '1',
           	     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            	    'viewport-width': '1366',
          	 	 }
		data ={
					'av':self.user_id,
					'fb_dtsg':self.fb_dtsg,
					'jazoest':self.jazoest,
					'fb_api_caller_class':'RelayModern',
					'fb_api_req_friendly_name':'CometSettingsDropdownListQuery',
					'variables':'{"fetchTestUserProfileListCell":false,"includeHorizBadging":false,"inProfileSwitcherEntry":false,"inSimpleHeaderEntry":true,"scale":2}',
					'server_timestamps':'true',
					'doc_id':'8179507702122101',
				}
		try:
			a=requests.post('https://www.facebook.com/api/graphql/', headers=headers,data=data).json()
			get = a['data']['viewer']['actor']['profile_switcher_eligible_profiles']
			tong = get['count']
			data_pro5 = get['nodes']
			print(f'| {tong} Page Profile')
			return data_pro5
		except:
			print('\nKhông Tìm Thấy Page Profile !')
			exit()

	def View(self,story_url,id_page,name):
		cookie = self.cookie
		ck_pro5 = 'sb={}; datr={}; c_user={}; wd={}; xs={}; fr={}; i_user={};'.format(cookie.split('sb=')[1].split(';')[0], cookie.split('datr=')[1].split(';')[0], cookie.split('c_user=')[1].split(';')[0],cookie.split('wd=')[1].split(';')[0], cookie.split('xs=')[1].split(';')[0],cookie.split('fr=')[1].split(';')[0],id_page)
		bucket_id = story_url.split('facebook.com/stories/')[1].split('/')[0]
		story_id = story_url.split(f'{bucket_id}/')[1].split('/')[0]
		headers = {
			'authority': 'www.facebook.com',
			'accept': '*/*',
			'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
			'cookie': ck_pro5,
			'origin': 'https://www.facebook.com',
			'referer': 'https://www.facebook.com',
			'sec-ch-prefers-color-scheme': 'dark',
			'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
			'x-fb-friendly-name': 'storiesUpdateSeenStateMutation',
		}
		data = {
			'av': id_page,
			'fb_dtsg': self.fb_dtsg,
			'jazoest': self.jazoest,
			'fb_api_caller_class': 'RelayModern',
			'fb_api_req_friendly_name': 'storiesUpdateSeenStateMutation',
			'variables': '{"input":{"bucket_id":"'+bucket_id+'","story_id":"'+story_id+'","actor_id":"'+id_page+'","client_mutation_id":"1"},"scale":1}',
			'server_timestamps': 'true',
			'doc_id': '5127393270671537',
		}

		#view = requests.post('https://www.facebook.com/api/graphql/',headers=headers, data=data).json()
		#return view
		try:
			xem = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()
			check = xem['data']['direct_message_thread_update_seen_state']['story']['story_card_seen_state']['is_seen_by_viewer']
			print(f'[√] | {bucket_id} | VIEW | {id_page} | {name} |')
		except:
			print(f'[×] | {bucket_id} | ERROR | {id_page} | {name}')
			
	def reaction_str(self, story_url, type, id_page, name):
		cookie = self.cookie
		ck_pro5 = 'sb={}; datr={}; c_user={}; wd={}; xs={}; fr={}; i_user={};'.format(cookie.split('sb=')[1].split(';')[0], cookie.split('datr=')[1].split(';')[0], cookie.split('c_user=')[1].split(';')[0],cookie.split('wd=')[1].split(';')[0], cookie.split('xs=')[1].split(';')[0],cookie.split('fr=')[1].split(';')[0],id_page)
		bucket_id = story_url.split('facebook.com/stories/')[1].split('/')[0]
		story_id = story_url.split(f'{bucket_id}/')[1].split('/')[0]
		if type == '1': cx = '👍'
		elif type == '2': cx = '❤️'
		elif type == '3': cx = '😆'
		elif type == '4': cx = '🤗'
		elif type == '5': cx = '😮'
		elif type == '6': cx = '😢'
		elif type == '7': cx = '😡'
		else: cx = '☠️'
		headers={
			'Host':'www.facebook.com',
			'sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"',
			'sec-ch-ua-mobile':'?0',
			'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
			'viewport-width':'980',
			'content-type':'application/x-www-form-urlencoded',
			'x-fb-lsd':'B3F7Ig_Qv4qJimRIo4q4eT',
			'x-fb-friendly-name':'useStoriesSendReplyMutation',
			'sec-ch-prefers-color-scheme':'light',
			'sec-ch-ua-platform':'"Linux"',
			'accept':'*/*',
			'origin':'https://www.facebook.com',
			'sec-fetch-site':'same-origin',
			'sec-fetch-mode':'cors',
			'sec-fetch-dest':'empty',
			'referer':story_url,
			'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
			'cookie':ck_pro5
		}
		data={
			'av': id_page,
			'fb_dtsg': self.fb_dtsg,
			'jazoest': self.jazoest,
			'fb_api_caller_class':'RelayModern',
			'fb_api_req_friendly_name':'useStoriesSendReplyMutation',
			'variables':'{"input":{"attribution_id_v2":"StoriesCometSuspenseRoot.react,comet.stories.viewer,via_cold_start,1669267579816,844710,,","lightweight_reaction_actions":{"offsets":[0],"reaction":"'+cx+'"},"message":"'+cx+'","story_id":"'+story_id+'","story_reply_type":"LIGHT_WEIGHT","actor_id":"'+id_page+'","client_mutation_id":"1"}}',
			'server_timestamps':'true',
			'doc_id':'4826141330837571',
		}
		try:
			reac=requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()
			check = reac['data']['direct_message_reply']['story']['story_card_info']['story_card_reactions']['edges'][0]['node']['messaging_actions']['count']
			print(f'[√] | {bucket_id} | {cx} | {name} | {id_page} | {check}')
		except:
			print(f'[×] | {bucket_id} | ERROR | {name} | {id_page} |')

banner()
while True:
	while True:
		cookie=input ('Nhập Cookie Nick Cầm Page Profile: ')
		fb = Facebook(cookie)
		bongoc(14)
		a=fb.get_thongtin()
		if a == 0:
			continue
		data_pro5 = fb.get_pro5()
		bongoc(14)
		if data_pro5 == 0:
			continue
		else:
			break
	while True:
		story_url = input('Nhập Link Story: ')
		try:
			bucket_id = story_url.split('facebook.com/stories/')[1].split('/')[0]
			story_id = story_url.split(f'{bucket_id}/')[1].split('/')[0]
			bongoc(14)
			break
		except:
			print('Link Story Gặp Lỗi !')
			bongoc(14)
	print("""Nhập [1] Để Buff View Story
Nhập [2] Để Buff Reaction Story""")
	chon_loai=input('Nhập ==>: ')
	bongoc(14)
	if chon_loai == '1':
		for x in data_pro5:
			id_page=x['profile']['id']
			name=x['profile']['name']
			threading.Thread(target=fb.View,args=(story_url,id_page,name)).start()

	if chon_loai == '2':
		print("""Nhập [1] Để Tăng Cảm Xúc LIKE
Nhập [2] Để Tăng Cảm Xúc LOVE
Nhập [3] Để Tăng Cảm Xúc HAHA
Nhập [4] Để Tăng Cảm Xúc CARE
Nhập [5] Để Tăng Cảm Xúc WOW
Nhập [6] Để Tăng Cảm Xúc SAD
Nhập [7] Để Tăng Cảm Xúc ANGRY
Có Thể Chọn Nhiều Chế Độ (Ví Dụ: 123)""")
		loai=input('Nhập ==>: ')
		soluong = int(input('Nhập Số Lượng Cảm Xúc: '))
		while (dem <= soluong):
			for x in data_pro5:
				id_page=x['profile']['id']
				name=x['profile']['name']
				threading.Thread(target=fb.reaction_str,args=(story_url, random.choice(loai), id_page, name)).start()
				dem+=1