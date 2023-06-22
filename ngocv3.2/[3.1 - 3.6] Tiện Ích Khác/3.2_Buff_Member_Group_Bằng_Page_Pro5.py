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
from sys import platform
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
dem=0

def bongoc(so):
	a= red+"────"*so
	for i in range(len(a)):
		sys.stdout.write(a[i])
		sys.stdout.flush()
		sleep(0.003)
	print()
	
def nghingoi(delay):
	for x in range(delay,0,-1):
		print("\r\033[1;93m   N-TOOL \033[1;91m ~>       \033[1;92m LO      \033[1;91m | "+str(x)+" | \r ", end='')
		sleep(0.14)
		print("\r\033[1;91m   N-TOOL \033[1;91m   ~>     \033[1;92m LOA     \033[0;31m | "+str(x)+" | \r ", end='')
		sleep(0.14)
		print("\r\033[1;92m   N-TOOL \033[1;91m     ~>   \033[1;92m LOAD    \033[0;31m | "+str(x)+" | \r", end='')
		sleep(0.14)
		print("\r\033[1;94m   N-TOOL \033[1;91m       ~> \033[1;92m LOADI   \033[0;31m | "+str(x)+" | \r", end='')
		sleep(0.14)
		print("\r\033[1;95m   N-TOOL \033[1;91m        ~>\033[1;92m LOADIN  \033[0;31m | "+str(x)+" | \r", end='')
		sleep(0.14)
		print("\r\033[1;96m   N-TOOL \033[1;91m        ~>\033[1;92m LOADING \033[0;31m | "+str(x)+" | \r", end='')
		sleep(0.14)
		print("\r\033[1;93m   N-TOOL \033[1;91m        ~>\033[1;92m LOADING.\033[0;31m | "+str(x)+" | \r", end='')
		sleep(0.14)
	print("\r\r\033[1;95m    ⚡ Nguyễn Chính Ngọc ⚡                         \r", end='')
	sleep(0.1)
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
			url = requests.get('https://mbasic.facebook.com/profile.php',headers=self.headers).url
			home = requests.get(url,headers=self.headers).text
			self.fb_dtsg = home.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
			self.jazoest = home.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
			ten = home.split('<title>')[1].split('</title>')[0]
			self.user_id = cookie.split('c_user=')[1].split(';')[0]
			print(f'{luc}Tên Facebook: {vang}{ten} {red}| {luc}ID: {vang}{self.user_id} ', end='')
			sys.stdout.flush()
		except:
			print(red+'Không Get Được Thông Tin ! ')
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
			print(f'{red}| {vang}{tong} {luc}Page Profile')
			return data_pro5
		except:
			print(red+'\nKhông Get Được Page Profile ')
			return 0
	def check_gr(self,id):
		headers={
				'Connection':'keep-alive',
				'Keep-Alive':'300',
				'authority': 'm.facebook.com',
				'ccept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
				'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
				'cache-control': 'max-age=0',
				'upgrade-insecure-requests': '1',
				'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-site': 'none',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'document',
				'cookie':self.cookie
          	 	}
		try:
			get=requests.get('https://mbasic.facebook.com/groups/'+id+'/', headers=headers).text
			ten = get.split('<title>')[1].split('</title>')[0]
			if ten != 'Không tìm thấy trang' and ten != 'Không tìm thấy nội dung':
				return ten
			else:
				return ten
		except:
			return 'error'
		
	def group (self, id, ten, id_page, name, dem):
		cookie = self.cookie
		ck_pro5 = 'sb={}; datr={}; c_user={}; wd={}; xs={}; fr={}; i_user={};'.format(cookie.split('sb=')[1].split(';')[0], cookie.split('datr=')[1].split(';')[0], cookie.split('c_user=')[1].split(';')[0],cookie.split('wd=')[1].split(';')[0], cookie.split('xs=')[1].split(';')[0],cookie.split('fr=')[1].split(';')[0],id_page)
		headers = {
			'authority': 'www.facebook.com',
			#:method: POST
			#:path: /api/graphql/
			#:scheme: https
			'accept':'*/*',
			'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': ck_pro5,
			'origin': 'https://www.facebook.com',
			'referer':'https://www.facebook.com/groups/'+id+'/?ref=share_group_link',
			'sec-ch-prefers-color-scheme': 'light',
			'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
			'viewport-width': '824',
			'x-fb-friendly-name': 'GroupCometJoinForumMutation',
			'x-fb-lsd': 'gUTCqdEnK_GG757IZ8OiXr',
		}
		data={
			'av':id_page,
			'fb_dtsg': self.fb_dtsg,
			'jazoest': self.jazoest,
			'fb_api_caller_class': 'RelayModern',
			'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
			'variables': '{"feedType":"DISCUSSION","groupID":"'+id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1669693169873,34680,2361831622,","group_id":"'+id+'","group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":false},"actor_id":"'+id_page+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":1,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":false}',
			'server_timestamps': 'true',
			'doc_id': '5608919199222447',
			'fb_api_analytics_tags': '["qpl_active_flow_ids=431626709"]'
		}
		like=requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
		try:
			
			a = like.json()
			memb = a['data']['group_request_to_join']['group']['profile_header_renderer']['group']['group_member_profiles']['formatted_count_text']
			#ten_gr = a['data']['group_request_to_join']['viewer']['groups_tab']['tab_groups_list']['edges'][0]['node']['name']
			print(f'{vang}[{trang}{dem}{vang}] {luc}[{lam}{name} {red}| {trang}{id_page}{luc}]{red} => {luc}[{lam}{ten} {red}| {trang}{id}{luc}]{red} => {vang}{memb} ')
		except:
			print(f'{vang}[{trang}{dem}{vang}] {luc}[{lam}{name} {red}| {trang}{id_page}{luc}]{trang} =>{red} ERROR ')
			
#cookie='datr=ZsNGYuK0Z7Iz5lCL464SXvL5;sb=ZsNGYr819Cgzwd0S9cHc8amb;m_pixel_ratio=2.75;dpr=2.75;usida=eyJ2ZXIiOjEsImlkIjoiQXJsa25mOTFiaGYzZzkiLCJ0aW1lIjoxNjY4ODIyMTY1fQ%3D%3D;c_user=100047062781231;fbl_ci=687934915665403;fbl_cs=AhDxYoUaRnCAzVSvfsKiSvlQGDMzVEZ5RDB3RTl0eTFIaHEzOGxkYXJNSA;m_page_voice=100047062781231;locale=vi_VN;vpd=v1%3B730x393x2.75;xs=48%3ACDVdTsV8Fh5EBQ%3A2%3A1668854606%3A-1%3A6297%3A%3AAcX7VwKj7gjQhW9zGWPUi9dSX7uxNqRMeDW3O_R0WA;fr=0nZgPjCHu05tl4ypH.AWXda-Mo0thf8NSUo4oSMu8UnUk.BjfBLX.P6.AAA.0.0.BjfBLX.AWXRERNoQEo;wd=393x730;x-referer=eyJyIjoiL250L3NjcmVlbi8%2FcGFyYW1zPSU3QiUyMnRva2VuJTIyJTNBJTIyQVZnQ2RhVXlPa2MtbFV1RkdialFESGR5UzBoa0RoeFo5a3dwZ0tQR3MwNDhTOGJkQ2tOcFBtN3lLamhVUGNxN3NQVm02eGpSelZPUUFPU2Z1WmV2MngwY3hPRFlxMFNWMHlTeUZUemFrU0Z5Z3NxZy1QS3ptQWlUX2hRWlVJYWZ2a1pKa0VRM0wwVHpxYnMxTWg5UTZUb2wzb042eFVaX1NDYlJmdDdGMDFGLXpMNjlnS0pGbWlBbEtiem51cE1BZ3ZPZWdodnBuN2Q4ZkRhZ1NGR0V2S0ZsU19pT1ZNVDRWOHlmb1UzNXU2QjVhc2RXY0VPZVJnMUdwbWNTWk11TXpXZ21aQ3VFV3F1VHVpazZybGgweXE5aWNlYVV0eGJPSjBRcGNjbGpQb0lpNWxaakJHY3NvOWJGMW9BakdoZGotSTEySnMySFdrdlpNcWt3bkVpZ25sRWpXaGFLSm5OUEtlZ1UtOG9iWlJ3QW9xX2QwLWk3ZndzN1EtUEJmNkptekJDViUyMiUyQyUyMnNob3dfc3VydmV5JTIyJTNBdHJ1ZSU3RCZwYXRoPSUyRm50JTJGY2hlY2twb2ludCUyRjgyODI4MTAzMDkyNzk1NiUyRm91dHJvJnN0YXRlIiwiaCI6Ii8iLCJzIjoibSJ9;fbl_st=101435816%3BT%3A27818277'
#cookie='datr=1nlmYiL0N_oPLQ_efFzUIWVJ;sb=1nlmYpOQCHFPsJoJVVYcxhB9;m_pixel_ratio=2.75;vpd=v1%3B730x393x2.75;locale=vi_VN;dpr=2.75;x-referer=eyJyIjoiL250L3NjcmVlbi8%2FcGFyYW1zPSU3QiU3RCZwYXRoPSUyRnBhZ2VzJTJGbnRfbGF1bmNocG9pbnRfcmVkZXNpZ24lMkZob21lc2NyZWVuJTJGbXRvdWNoJTJGJnBhaXB2PTAmZWF2PUFmYTRrbVkybnBKcUxheUlKNU1yNFFLSndaLS1OUzFXWGctVktFV3FYSVljSEtSSU1HLUhSVzU5Z2xvdzZwSXJTQnMiLCJoIjoiL250L3NjcmVlbi8%2FcGFyYW1zPSU3QiU3RCZwYXRoPSUyRnBhZ2VzJTJGbnRfbGF1bmNocG9pbnRfcmVkZXNpZ24lMkZob21lc2NyZWVuJTJGbXRvdWNoJTJGJnBhaXB2PTAmZWF2PUFmYTRrbVkybnBKcUxheUlKNU1yNFFLSndaLS1OUzFXWGctVktFV3FYSVljSEtSSU1HLUhSVzU5Z2xvdzZwSXJTQnMiLCJzIjoibSJ9;usida=eyJ2ZXIiOjEsImlkIjoiQXJsbWM1c3hzdHZ4eCIsInRpbWUiOjE2Njg5MDA4ODB9;wd=393x730;fr=0kPBaNYsgyKoix0y5.AWW1FJsdjLzBK9gjw1l--6xRSTU.BjbJWs.pN.AAA.0.0.BjfGf3.AWWne9GqJWY;c_user=100060781202490;xs=41%3AAaylS8gnhXZMAQ%3A2%3A1669097463%3A-1%3A6281;fbl_st=101528087%3BT%3A27818291;fbl_cs=AhBOr%2F4aN3Nk4jf3nLB4feMmGFJpTGxWcnBCQjF0SnY3M0FHNjBmR2NzWQ;fbl_ci=1552334505129880'

#cookie='datr=ZsNGYuK0Z7Iz5lCL464SXvL5;sb=ZsNGYr819Cgzwd0S9cHc8amb;m_pixel_ratio=2.75;dpr=2.75;usida=eyJ2ZXIiOjEsImlkIjoiQXJsa25mOTFiaGYzZzkiLCJ0aW1lIjoxNjY4ODIyMTY1fQ%3D%3D;c_user=100047062781231;fbl_ci=687934915665403;fbl_cs=AhDxYoUaRnCAzVSvfsKiSvlQGDMzVEZ5RDB3RTl0eTFIaHEzOGxkYXJNSA;m_page_voice=100047062781231;locale=vi_VN;vpd=v1%3B730x393x2.75;xs=48%3ACDVdTsV8Fh5EBQ%3A2%3A1668854606%3A-1%3A6297%3A%3AAcX7VwKj7gjQhW9zGWPUi9dSX7uxNqRMeDW3O_R0WA;fr=0nZgPjCHu05tl4ypH.AWXda-Mo0thf8NSUo4oSMu8UnUk.BjfBLX.P6.AAA.0.0.BjfBLX.AWXRERNoQEo;wd=393x730;x-referer=eyJyIjoiL250L3NjcmVlbi8%2FcGFyYW1zPSU3QiUyMnRva2VuJTIyJTNBJTIyQVZnQ2RhVXlPa2MtbFV1RkdialFESGR5UzBoa0RoeFo5a3dwZ0tQR3MwNDhTOGJkQ2tOcFBtN3lLamhVUGNxN3NQVm02eGpSelZPUUFPU2Z1WmV2MngwY3hPRFlxMFNWMHlTeUZUemFrU0Z5Z3NxZy1QS3ptQWlUX2hRWlVJYWZ2a1pKa0VRM0wwVHpxYnMxTWg5UTZUb2wzb042eFVaX1NDYlJmdDdGMDFGLXpMNjlnS0pGbWlBbEtiem51cE1BZ3ZPZWdodnBuN2Q4ZkRhZ1NGR0V2S0ZsU19pT1ZNVDRWOHlmb1UzNXU2QjVhc2RXY0VPZVJnMUdwbWNTWk11TXpXZ21aQ3VFV3F1VHVpazZybGgweXE5aWNlYVV0eGJPSjBRcGNjbGpQb0lpNWxaakJHY3NvOWJGMW9BakdoZGotSTEySnMySFdrdlpNcWt3bkVpZ25sRWpXaGFLSm5OUEtlZ1UtOG9iWlJ3QW9xX2QwLWk3ZndzN1EtUEJmNkptekJDViUyMiUyQyUyMnNob3dfc3VydmV5JTIyJTNBdHJ1ZSU3RCZwYXRoPSUyRm50JTJGY2hlY2twb2ludCUyRjgyODI4MTAzMDkyNzk1NiUyRm91dHJvJnN0YXRlIiwiaCI6Ii8iLCJzIjoibSJ9;fbl_st=101435816%3BT%3A27818277'

#cookie='datr=VCPCYc-UdobB3bWelY6PbFGo; sb=VCPCYczUeudS4GkeAGBkHM4C; m_pixel_ratio=2.75; c_user=100000886402731; xs=49%3AlHAYcZlPy-zgjw%3A2%3A1662999035%3A-1%3A10818; fbl_ci=421380822646831; m_page_voice=100000886402731; vpd=v1%3B730x393x2.75; x-referer=eyJyIjoiL250L3NjcmVlbi8%2FcGFyYW1zPSU3QiUyMnRva2VuJTIyJTNBJTIyQVZpcTlWODRIc3VnZ09KTHc2ek5ZVUYzdjROWUNpWlV1czk4Y1dzSDN2SmN5UmlTR0JQSmF4WldfY29HRWFuNXpUTDJQNTMtRnNHeGdIZXotUEs5MnI2Z1hwMDFEYlkxbEtyX3RMdWlIbTJxS1ltVFNBZDFHMXJ5ODlPSkpZRmNHYlZwU3MxTFR1YzltbzRqbVJLVjgxSTNfNF9Fa2Z2dXpPcWNYcWNkVGR2TTJURTBDeWFrSEs0Q2FCRFc3aGNLNWwwT2p3U21remFhTmtoc05nbzBjRl9BN244Z0dlbzh5emZHUlNfeUVIbHBya1BXNWJhOXZJa1U0Sl9Hc09NMkRIRGdwaXdSTGNIbkFYLUw1V2tiaFRRT0hqVjdZeGoycXR6bVE1YXMwWk5mUVlpd1Q4cTJ2MmxMUlNwUVdNLUFycEl5VmNYVjVEc0JrZVhGd2Z1S0FFdFRfWElYT1RkM1UwTS1vd2Vrd0ppbjVzTFhpc3E2QWpMY2g1MlhiMjIybW05ZUpRJTIyJTJDJTIyc2hvd19zdXJ2ZXklMjIlM0F0cnVlJTdEJnBhdGg9JTJGbnQlMkZjaGVja3BvaW50JTJGODI4MjgxMDMwOTI3OTU2JTJGb3V0cm8mc3RhdGUiLCJoIjoiLyIsInMiOiJtIn0%3D; locale=vi_VN; dpr=2.75; usida=eyJ2ZXIiOjEsImlkIjoiQXJsaXRudGJ5ZWE0aCIsInRpbWUiOjE2Njg3MzY5Mzd9; fbl_cs=AhDwsptc473S73uLC6U70MfdGGp1RTc3cXZFc05waEZES3VvYTlVR01maA; wd=393x873; fr=0f3lg327qmDJf8wTx.AWXa592Anolgge_PVmSo_mJGsBE.BjMVjd.gK.AAA.0.0.Bjed4H.AWWF0A_HD4M; fbl_st=100437456%3BT%3A27815518'

#cookie='sb=AUYMYnk8OfqoWYsDXWBOP2Iq; datr=BUYMYh0yAiMXl5yhZgUCPLXO; locale=vi_VN; c_user=100084450153910; xs=1%3AjbdH0hymtiTFIg%3A2%3A1669689855%3A-1%3A5585; m_page_voice=100084450153910; fr=09wuJ0MkdwGaxMi7q.AWXvYtrec1uNpG-u84aBH20STiY.BjBC3r.Jr.AAA.0.0.BjhXrC.AWXYi8ZRKUI; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1669691155300%2C%22v%22%3A1%7D; wd=223x385'

banner()
while True:
	cookie=input (thanh_xau+luc+'Nhập Cookie Nick Cầm Page Profile: '+vang)
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
dl = int(input(thanh_xau+luc+'Nhập Delay: '+vang))
print(f'{red}[{vang}LƯU Ý{red}]{luc} Bật Cho Page Tham Gia Group Và Mở Công Khai Group ')
while True:
	id = input(thanh_xau+luc+'Nhập ID Group: '+vang)
	ten=fb.check_gr(id)
	if ten != 'Không tìm thấy trang' and ten != 'Không tìm thấy nội dung' and ten != 'error':
		print(luc+'Tên Group: '+ lamd + ten)
		break
	elif ten != 'Không tìm thấy trang' or ten != 'Không tìm thấy nội dung':
		print(red+ten)
	else:
		print(red+'Không Get Được Thông Tin Group') 
for x in data_pro5:
	id_page=x['profile']['id']
	name=x['profile']['name']
	dem+=1
	fb.group(id, ten, id_page, name, dem)
	nghingoi(dl)


