# DECRYPTED BY xXx_not_found_xXx
# Github : https://github.com/hamalord4444
 # uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: Sumarr ID
import os, sys, shutil
from app import main as app
base_url = 'https://mbasic.facebook.com'
if sys.version_info.major != 2:
    sys.exit('\n\x1b[0;97m{\x1b[0;92mWARNING\x1b[0;97m} \x1b[0;91mTools ini menggunakan bahasa python2.\nsegera upgrade terlebih dahulu\x1b[0m')
try:
    shutil.rmtree('app/__pycache__')
except:
    pass

try:
    shutil.rmtree('src/__pycache__')
except:
    pass

for filename in os.listdir('app'):
    if filename[-3:] == 'pyc':
        try:
            os.remove('app/' + filename)
        except:
            pass

for filename in os.listdir('src'):
    if filename[-3:] == 'pyc':
        try:
            os.remove('src/' + filename)
        except:
            pass

awokawokawok = app.Brute(base_url)
awokawokawok.start()