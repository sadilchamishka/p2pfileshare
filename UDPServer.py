import socket
import threading
from concurrent.futures import ThreadPoolExecutor

import constants as CONST

class UDPServer:
	def __init__(self, ip, port, listen = 5):
		self.ip = ip
		self.port = port
		self.listen = listen
		self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.server.bind((self.ip, self.port))
		self.server.listen(self.listen)
	
	def serve(self):
		threading.Thread(target=self.__start, args=(self.server,)).start()

	def __start(self, server):
		executor = ThreadPoolExecutor(max_workers=10)
		while True:
			conn, addr = server.accept()
			executor.submit(self.__processRequest, conn=conn)

	def __recieve(conn)

		data_header = conn.recv(CONST.HEADER_SIZE)
		data_length = int(message_header.decode('utf-8').strip())

		data = conn.recv(data_length)
		data = message_header.decode('utf-8').strip()
		return list(data)
    
	def __processRequest(self, conn):
		print("start handling request")
		data = __recieve(conn)
		conn.send(bytes("Recieved","utf-8"))
		conn.close()

		
