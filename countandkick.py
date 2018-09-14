#!/usr/bin/env python3
import time
import datetime
import pygame
import  sys
CTRL_C = 3
CR=13
LF=10
import  subprocess
import  sys
PlayLoop=1
CountDown=1

#musicfile="ThreeMarchesMilitaires_Schubert.mp3" # mp3 file cause error because cant get music length.
musicfile="musics/Toreador_song_cleaned.ogg"


def input_with_no_echo():
  message=""
  try:
    from msvcrt import getch
  except ImportError:
    def getch():
      import sys
      import tty
      import termios
      fd = sys.stdin.fileno()
      old = termios.tcgetattr(fd)
      try:
        tty.setraw(fd)
        return sys.stdin.read(1)
      finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
 
  while True:
    key = ord(getch())
    if key == CTRL_C:
      return(3)
    if key == CR:
#      if (message == "" ):
#        print()
      break 
    if key == LF:
#      if (message == "" ):
#        print()
      break
    else:
       
      getstr = '{0}'.format(chr(key))
#      print (getstr,end='')
      sys.stdout.flush()
    message = message + getstr
#  print(message,end='')
  return(message)



t = time.time()
sys.stdout.write('Enter Return Key:')
sys.stdout.flush()
key=input_with_no_echo()
count=CountDown
sys.stdout.write("\033[?25l")
while (count >=0 ):
    time.sleep(1)
#    print ( count )
    sys.stdout.write("\033[2K\033[G%s" % count)
    sys.stdout.flush()
    #sys.stdout.write("\033[1A")
    count=count-1
# subprocess.run("echo \"これはテストです\" | open_jtalk -x /var/lib/mecab/dic/open-jtalk/naist-jdic -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice -ow /dev/stdout | aplay "
#  ,shell=True
#  ,stdout=subprocess.DEVNULL
#  ,stderr=subprocess.DEVNULL)
pygame.mixer.init()
music=pygame.mixer.Sound(musicfile)
#pygame.mixer.music.load(musicfile)
#pygame.mixer.music.set_volume(0.1)
music.set_volume(0.1)
seconds=music.get_length()*(PlayLoop) # 再生時間の取得[ms]
music.play(PlayLoop-1)
print(seconds)
# pygame.mixer.music.play(1)
print("##")
d1=datetime.datetime.now()
td=datetime.timedelta(seconds=seconds)
d2=d1+td
c = (d2-datetime.datetime.now())
while c.total_seconds() > 0:
    time.sleep(1)
    c = (d2-datetime.datetime.now())
    sys.stdout.write("\033[2K\033[G%s" % c)
    sys.stdout.flush()
while True:
    time.sleep(1)
    c = (datetime.datetime.now()-d2)
    sys.stdout.write("\033[2K\033[G%s" % c)
    sys.stdout.flush()
print('end')



