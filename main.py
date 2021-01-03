from UDPServer import UDPServer
from FlaskServer import FlaskServer
from Node import Node
from Utillities import BoostrapRegistrate, BoostrapUnRegistrate
import socket

name = input("Please enter name : ")
port = int(input("Please enter port : "))
BootstrapNode = Node("127.0.0.1", 55555)
ClientNode = Node("127.0.0.1", port, name)

BoostrapRegistrate(BootstrapNode, ClientNode)
   
udpServer = UDPServer(socket.gethostname(), port)
udpServer.startServer()

flaskServer = FlaskServer('file server')
flaskServer.add_endpoint(endpoint='/<file>', endpoint_name='download file endpoint')
flaskServer.run()

while True:
   user_input  = input("What you need ........")
   if user_input=="exit":
      BoostrapUnRegistrate(BootstrapNode, ClientNode)
      break

