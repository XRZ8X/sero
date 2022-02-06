""" 
-------------------------------------------------------------------------
- Cod BY : SidraELEzz
- Github : https://github.com/SidraELEzz
- Telegram: https://t.me/SidraTools
- Telegram: https://t.me/tt_rq
-------------------------------------------------------------------------
      
""" 

try:
	import os,sys,time,requests,json,random,user_agent,threading
	from user_agent import generate_user_agent
	from concurrent.futures import ThreadPoolExecutor
except ImportError:
	os.system("pip install requests")
	os.system("pip install user_agent")
	
	
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"

def baner():
	banera = f"""{E}
    
  88888888888 d8b 888  88888888888       888      
      888     Y8P 888      888           888      
      888         888      888           888      
      888     888 888  888 888   .d88b.  888  888 
      888     888 888 .88P 888  d88""88b 888 .88P 
      888     888 888888K  888  888  888 888888K  
      888     888 888 "88b 888  Y88..88P 888 "88b 
      888     888 888  888 888   "Y88P"  888  888 
                                                                                                 
  \033[1;93m < \033[1;92mTHE TOOL IS FREE\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ\033[1;91m
  ---------------------------
"""     

	for sidra in banera.splitlines():
		time.sleep(0.05)
		print(sidra)
		
def clear():
	if os.name == 'nt':
		os.system('cls')
		os.system('title Cod BY SidraELEzz ')
	else:
		os.system('clear')
		


def TikTok(username,TK, ID):
	ok = 0
	cp = 0
	si = "0987654321"
	sh = "@yahoo.com"
	while True:
		eml = str(''.join(random.choice(si)for i in range(3)))
		email = str(username)+str(eml)+str(sh)
		headers = {
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
       'Connection': 'keep-alive',
       'Host': 'Sidraapi.pythonanywhere.com',
       'User-Agent': str(generate_user_agent())} 
    
		header = {
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
       'Connection': 'keep-alive',
       'Host': 'sidraelezz-v2.herokuapp.com',
       'User-Agent': str(generate_user_agent())} 
       
		Yahoo = requests.get(f"https://sidraapi.pythonanywhere.com/v1/api/check/yahoo/?email={email}",headers=headers)
		Tikpy = requests.get(f"https://sidraelezz-v2.herokuapp.com/check/tiktok/?email={email}",headers=header)
		if (Yahoo.json()["check"])=="True": 
			pass
			if (Tikpy.json()["result"])=="True": 
				ok+=1
				massage = ("• Email TikTok ✓\n =================\n[~] Email : "+str(email)+"\n=================\n• @SidraTools")
				requests.get("https://api.telegram.org/bot"+str(TK)+"/sendMessage?chat_id="+str(ID)+"&text="+str(massage))
				
		else:
			cp+=1
			print("\r\033[1;92m[•] GOOD : {} \033[1;92m[x] \033[1;90mBad :\033[1;93m {} \033[1;92m[-] \033[1;92m{}".format(str(ok),str(cp),str(email),end=''))
			


clear();baner()
TK = input(C+" ("+E+"⌯"+C+") "+C+ "TOKEN BOT :"+B)
ID = input(C+" ("+E+"⌯"+C+") "+C+ "ID  :"+B)
clear();baner()
username = input(C+" ("+E+"⌯"+C+") "+C+ "USERNAME :"+B)
clear();baner()
with ThreadPoolExecutor(max_workers=30) as SidraELEzz:
	SidraELEzz.submit(TikTok,username,TK,ID)
	