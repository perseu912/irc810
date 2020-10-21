#Reinan Bezerra 7/4/2020

from tools import save_file_on
import time
from colorama import *
import irc as i

irc = i.Irc
nick = 'jezuis_matrix'
user = 'jezuis'
irc = irc(user, nick)
#save = irc.save()

mg = ''
j = 0
b = 0
while True:
  msg = (irc.recv())
  if((msg != mg)):
    print(msg)
#    irc.save(msg,'chat.txt
    save_file_on(msg,'msg.txt')
    if((msg.find('JOIN') != -1) and (j==0)):
      j = 1
      irc.join('#brazil')
    try:
      if(msg.index('REPROVADO') > -1):
        # irc.join('#brasil')
        #irc.save(msg, 'br.txt')
        cc = msg
        init_cc = cc.index('✘ » ')+4
        print(init_cc)
        end_cc = cc.index(' | ')
        print(end_cc)
        cc = '|'.join(cc[init_cc:end_cc].split(' » '))
        print(cc,' reprovada')
        
        save_file_on(cc,'cc_reprovada.txt')
        
#        irc.save(cc,'cc_reprovada.txt')
        
        print(Fore.YELLOW+msg)
        print(Style.RESET_ALL)
    except:
      pass
  #salvando aprovada 
    try:
      if(msg.index('APROVADA') > -1 or msg.index('approved') > -1 or msg.index('✔ »') > -1):
#        irc.save(msg, 'cc.txt')
        print(Fore.GREEN+msg)
        print(Style.RESET_ALL)
        
        cc = msg
        init_cc = cc.index('✔ »')+4
        print(init_cc)
        end_cc = cc.index(' | ')
        print(end_cc)
        cc = '|'.join(cc[init_cc:end_cc].split(' » '))
        print(cc,' aprovada')
        
        save_file_on(cc,'cc_aprovada.txt')
        
#        irc.save(cc,'cc_aprovada.txt')
      
    except:
      pass
    irc.hi(msg)
    irc.checa_ping(msg)
  else:
    pass
  mg = msg

	
