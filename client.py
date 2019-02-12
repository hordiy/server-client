import socket
import threading

key = 9687

power = True
join = True

def receving(name, sock):
	while power:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				data = data.decode("utf-8")
				# XOR
				decrypt = ""; k = True
				for i in data:
					if i == ":":
						k = False
						decrypt += i
					elif k == True or i == " ":
						decrypt += i
					else:
						decrypt += chr(ord(i)^key)
				print(decrypt)
		except: pass

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("127.0.0.1", 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

name = input("Name: ")

rT = threading.Thread(target = receving, args = ("RecvThread", s))
rT.start()

while power:
	if join == True:
		s.sendto(("[" + name + "] => join chat ").encode("utf-8"), server)
		join = False
	else:
		try:
			message = input(":> ")
			# XOR
			encrypt = ""
			for i in message:
				encrypt += chr(ord(i)^key)
			message = encrypt

			if message != "":
				s.sendto(("[" + name + "] :: " + message).encode("utf-8"), server)
		except:
			s.sendto(("[" + name + "] <= left chat ").encode("utf-8"), server)
			power = False

rT.join()
s.close()
