import os
import sys
import re
import json
import string
import random
import hashlib
import uuid
import time
from datetime import datetime
from threading import Thread
import requests
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
from cfonts import render, say
from colorama import Fore, Style, init
import webbrowser

# Display Tool Banner
print("\n" + "="*60)
print(render('INSTAGRAM', colors=['red', 'yellow'], align='center', font='block'))
print(render('REPORT TOOL', colors=['cyan', 'green'], align='center', font='simple'))
print("="*60)
print(f"{Fore.CYAN}🔥 Advanced Instagram Account Reporting Tool 🔥{Style.RESET_ALL}")
print(f"{Fore.YELLOW}📱 Report spam/bots/fake accounts automatically 📱{Style.RESET_ALL}")
print(f"{Fore.GREEN}⚡ Fast & Efficient | Multi-threaded ⚡{Style.RESET_ALL}")
print(f"{Fore.RED}👨‍💻 Created by: KUNAL 👨‍💻{Style.RESET_ALL}")
print("="*60 + "\n")

webbrowser.open("https://t.me/+GtCvQ_NswDxmZDVl")
init(autoreset=True)
import requests
import random
import os
from datetime import datetime
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
os.system('clear')

user=input(f'{lrd}[{lgn}?{lrd}] {lgn}Enter the target username : {cn}')
name=input(f'\n\n{lrd}[{lgn}?{lrd}] {lgn}Enter the account name : {cn}')
yesno = input(f"\n\n{lrd}[{lgn}?{lrd}] {lgn}Do you want to use a proxy? Maybe the speed will slow down [Y/N] : {cn}")
head={
    "Host": "help.instagram.com",
    "content-length": "715",
    "x-fb-lsd": "AVq5uabXj48",
    "x-asbd-id": "129477",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"99\", \"Google Chrome\";v\u003d\"99\"",
    "sec-ch-ua-platform": "\"Android\"",
    "content-type": "application/x-www-form-urlencoded",
    "accept": "*/*",
    "origin": "https://help.instagram.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://help.instagram.com/contact/723586364339719",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7,fr;q\u003d0.6,hu;q\u003d0.5",
    "cookie": "ig_nrcb\u003d1"}
ti = datetime.now()
print(f'{yw}=======================================\n\n{gn}Username : {rd}{user}\n\n{gn}Name : {rd}{name}\n\n{lgn}Time : {pe}{ti.strftime("%H:%M:%S")}\n\n{yw}=======================================') 
r=0
while True:
 Now = datetime.now()
 Test = str(datetime.timestamp(Now)).split('.')[0]
 Letters='qwertyuiopasdfghjklzxcvbnm._1234567890'
 boy=str("".join(random.choice(Letters)for i in range(10)))
 email=boy+'@gmail.com'
 data=f'jazoest=2931&lsd=AVq5uabXj48&Field258021274378282={user}&Field735407019826414={name}&Field506888789421014[year]=2014&Field506888789421014[month]=11&Field506888789421014[day]=11&Field294540267362199=Parent&inputEmail={email}&support_form_id=723586364339719&support_form_locale_id=en_US&support_form_hidden_fields=%7B%7D&support_form_fact_false_fields=[]&__user=0&__a=1&__req=6&__hs=19552.BP%3ADEFAULT.2.0..0.0&dpr=1&__ccg=GOOD&__rev=1007841948&__s=s4c6vz%3Anapxo9%3An9ncx2&__hsi=7255652935514227640&__dyn=7xe6E5aQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXw5ux60Vo1upE4W0OE2WxO2O1Vwooa81VohwnU1e42C220qu1Tw40wdq0Ho2ewnE3fw6iw4vwbS1Lw4Cwcq&__csr=&__spin_r=1007841948&__spin_b=trunk&__spin_t={Test}'
 try:
  if yesno == 'Y' or yesno == "y":
      proxy = input(f"\n\n{yw}[!] Enter the name of a protocol to use a proxy\n\n{lrd}[{lgn}?{lrd}] {lgn}Enter the protocol name [socks4,socks5] : {cn}")
      proxy_file = input(f"\n\n{lrd}[{lgn}?{lrd}] {lgn}Enter Name File proxy : {cn}")
      proxy_file = open(proxy_file,'r')
      for i in proxy_file:
          res=requests.post('https://help.instagram.com/ajax/help/contact/submit/page',data=data,headers=head, proxies={proxy:i},timeout=5).status_code
  else:
   res=requests.post('https://help.instagram.com/ajax/help/contact/submit/page',data=data,headers=head,timeout=5).status_code
  if res == 200:
   r+=1
   print(f'{lrd}[{lgn}!{lrd}] {gn}Report number : {yw}{r}  {lgn}Sent ! {lgn}{user}')
  else:
   print(f'{lrd}[{rd}!{lrd}] Error Code : {lrd}{res}')
 except:
  print(f'{lrd}[!] Error !!')