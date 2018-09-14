#!/usr/bin/env python3
print("hello");
import  subprocess
import  sys
CTRL_C = 3
BS=8
CR=13
LF=10
DEL=127

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
#    print(key)
#    print len((message))
    if key == CTRL_C:
      return(3)
    if key == CR:
      if (message == "" ):
        print()
      break 
    if key == BS:   # ^H key
      sys.stdout.write("\033[1D")
      sys.stdout.flush()
    if key == DEL:  # BS key
      if (message != "" ):
        message = message[:-1]
        message = message[:-1]
        sys.stdout.write("\033[1D") # 一文字削除
        sys.stdout.write("\033[1D") # 一文字削除
        sys.stdout.flush()
    if key == LF:
      if (message == "" ):
        print()
      break
    else:
       
      getstr = '{0}'.format(chr(key))
      print (getstr,end='')
      sys.stdout.flush()
    message = message + getstr
#  print(message,end='')
  return(message)




while 1:
  key=input_with_no_echo()
  if key == CTRL_C:
        break
  if key == CR:
        break
  if key == LF:
        break
  subprocess.run("echo \""+key+"\" | open_jtalk -x /var/lib/mecab/dic/open-jtalk/naist-jdic -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice -ow /dev/stdout | aplay "
  ,shell=True
  ,stdout=subprocess.DEVNULL
  ,stderr=subprocess.DEVNULL)
