import socket
import threading
from concurrent.futures import ThreadPoolExecutor

class UDPServer:
	def __init__(self, ip, port, listen = 5):
		self.ip = ip
		self.port = port
		self.listen = listen
		self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serv.bind((self.ip, self.port))
		self.serv.listen(self.listen)
	
	def startServer(self):
		threading.Thread(target=self.start, args=(self.serv,)).start()

	def start(self, serv):
		executor = ThreadPoolExecutor(max_workers=3)
		while True:
			conn, addr = serv.accept()
			executor.submit(self.processRequest, conn=conn)
    
	def processRequest(self, conn):
		print("start handling request")
		data = conn.recv(1024)
		print (data.decode("utf-8"))
		conn.send(bytes("Recieved","utf-8"))
		conn.close()

		
