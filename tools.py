import time as tm,time,socket
# -*- coding: utf-8 -*-


import os, signal, sys

debug = False

# set stderr to dev/null

sys.stderr = open(os.devnull, "w")
import psutil

# after importing, set stderr to original 
sys.stderr = sys.__stderr__
'''
print("killing python")
proc = psutil.Process(os.getpid())
proc.send_signal(signal.SIGTERM)
'''

#data
def date():
  from datetime import datetime as dt
  dt = dt.now()
  return dt.strftime('%d/%m/%Y %H:%M:%S')

def ram():
	r_max = float(round(psutil.virtual_memory().total/(1024**3),3))
	r_per = float(psutil.virtual_memory().percent)
	r_use = round(r_max*r_per/100,3)
	r_ping = round(time.process_time()*100,1)
	return (r_use,r_max,r_per,r_ping)

def print_sys_stats():
	print('=+='*18)
	print(f'diretorio: {os.getcwd()}')
	print(f'system Platform: {os.uname().sysname}')
	#print(f'Platform Version: {os.uname().version}')
	print(f'Machine: {os.uname().machine}')
	print(f'RAM: {ram()[0]} GB / {ram()[1]} GB ({ram()[2]}% used)')
	#print(f'RAM Used: {psutil.virtual_memory().percent}%')
	print(f'PING CPU: {round(time.process_time()*100,1)}ms') 
	#print(f'vel. process: {round(1/time.process_time(),3)} app/s')
	print(f'data: {date().split()[0]}')
	print(f'hora: {date().split()[1]}')
	print('=+='*18)



import platform,socket,re,uuid,json,psutil,logging

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

#print(json.loads(getSystemInfo()))



#criar pastas
def mkdir(path):
	os.mkdir(path)


#sleep
def cronus(t,text=''):
   s = t
   while(True):
      #f = t
      m = (s // 60)
      mRest = s%60
      h = (m // 60)
      hRest = m%60
      print(f' {h} horas :{m} min :{mRest} seg',text)
      tm.sleep(1)
      s -= 1
      if(s==-1):
         break


#salvando arquivos
def save_file(var,path,code='utf-8',a='w'):
  with open(path,a,encoding=code) as _file:
    puts('salvando variavel...')
    _file.write(str(var))
    puts('variavel salva!')



def puts(*args,sep=' ',on=False,log=True,file_name='log'):
  from datetime import datetime as dt
  dt = dt.now()
  dataTime = dt.strftime('%d/%m/%Y %H:%M:%S')
  input = ''
  
  for i in args:
    input += i+sep
  text = (f'[{dataTime}]: {input} \n')
  
  if debug:
	  text = (f'[CPU: {ram()[2]}%_{ram()[3]}ms]\n[{dataTime}]: {input}')
  
  print(text)
  if log:
    path = open(file_name,'a',encoding='utf-8')
    with path as file_p:
      file_p.write(text+'\n')
      # TODO: write code...
  if(on):
    import requests as rq 
    params = {
      'file':file_name,
      'log':text 
    }
    try:
      rq.get('https://log810.000webhostapp.com/',params)
    except:
      print('on_off')

def save_file_on(content,file_name):
    import requests as rq 
    params = {
      'file':file_name,
      'log':content 
    }
    try:
      rq.get('https://log810.000webhostapp.com/',params)
    except:
      print('on_off')

#puts('test','oi')
#cronus(3_600)


