
import socklib as s

class Irc:
	def __init__(self, user, nick):
		#estabelece conexão com o irc
		url = 'irc.chknet.cc'
		port = 6667
		self.irc = s.Socket(url, port)
		print(self.irc.recv())

		#dados de cadastro
		#nick = 'jezuis_matrix'
		#user = 'jezuis'
		
		#envia o nick escolhido para fazer login
		comando_nick = f'NICK {nick} \r\n'
		self.irc.send(comando_nick)
		# o msm requisito àcima
		comando_user = f'USER {user} {user} {user} :rainbow pie \r\n'
		self.irc.send(comando_user)

	def join(self, channel):
		#envia a msg(comando) entrar(JOIN) no canal 
		self.irc.send(f'JOIN {channel} \r\n')

		#checa o ping
	def checa_ping(self,msg):
		if 'PING :' in msg:
			codigo_ping = msg.split('PING :')[-1]
			resposta_pong = 'PONG :{}'.format(codigo_ping)
			self.irc.send(resposta_pong)

		#comando hi para permanecer no irc
	def hi(self, msg):
		if msg.find('hi') != -1:
			self.irc.send((str('PRIVMSG ' + msg.split()[2]) + ' Hi! \r\n'))
	

		#escreve um arquivo salvando as msg's
	def save(self, msg, file):
		f = open(file,'a')
		f.write((msg)+' \n')
		f.close()
		
	#envia as msg's
	def send(self, msg):
		self.irc.send(msg)
		
	#recebe as msg's
	def recv(self):
		res = self.irc.recv()
		return res




