

import socket 
import time
from datetime import datetime as h

#criando o socket
class Socket:
	def __init__(self,proxy, port=80):
		#instânceia os protocolos nescessários
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.proxy = proxy
		self.port = port
		self.ip = socket.gethostbyname(self.proxy)
		# test de estabelescimento de conexão com ping
		try:
			init = time.perf_counter()
			self.s.connect((self.ip,self.port))
			self.ping = time.perf_counter() - init
			sucess = True
		except:
			print(f'verifique se o proxy {self.proxy} está disponivel')
			raise
			exit()
		if sucess:
			print(f'connected in {self.proxy}[{self.ip}]')
	
	
	#envia pacotes de dados na forma de bit(.encode)
	def send(self, msg):
		self.s.send(msg.encode())
	
		
	#envia pacotes via http
	def send_http(self, terms):
		self.send('GET /'+terms+'HTTP/1.1\r\n')
		self.send('Host: '+terms+'\r\n\r\n')
		
		
	#funcao que testa o ping com pacote
	def pingNet(self,n=10, pacot='', prnt=False):
		p = 0
		listPing = []
		for i in range(n):
			try:
				self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				init = time.perf_counter()
				self.s.connect((self.ip,self.port))
				self.send_http(pacot)
				self.ping = time.perf_counter() - init
				#lista com os pingTime's
				listPing.append([i])
				listPing[i].append(self.ping)
				if prnt:
					print(self.ping)
					p += self.ping
			except:
				print(f'o proxy {self.proxy} falhou na resposta ao ping')
				exit()
		res = p/n
		return listPing
	
	
	#recebe a resposta do servidor
	def recv(self, type='utf-8',bit=2048):
		res = ''
		msg = ''
		try:
				res = self.s.recv(bit).decode(type)
				hh = (h.now().strftime('%d/%m/%Y %H:%M:%S'))
				msg = (f'[{hh}]__{res}')
		except:
			pass
		return msg
