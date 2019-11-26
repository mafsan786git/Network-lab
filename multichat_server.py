import socket
import sys
from thread import *
server=socket.socket()
server.bind(('',4444))
list_of_clients=[]
server.listen(100)
def clientthread(connection,addr):
	connection.send("Welcome to chat room")
	while True:
		message=connection.recv(1024)
		if message:
			print "<"+addr[0]+"> "+message
			message_to_send="<"+addr[0]+"> "+message
			broadcast(message_to_send,connection)
		else:
			connection.close()
			remove(connection)

def broadcast(message,conn):
	for clients in list_of_clients:
		if clients != conn:
			clients.send(message)
		
def remove(conn):
	if conn in list_of_clients:
		list_of_clients.remove(conn)
while True:
	conn,addr=server.accept()
	list_of_clients.append(conn)
	print addr[0] +"connected"
	start_new_thread(clientthread,(conn,addr))
conn.close()
server.close()
