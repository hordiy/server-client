import socket, time
host = "127.0.0.1"
port = 9090

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print("###### [Server Started] ######")
power = True

while power:
	try:
		data, addr = s.recvfrom(1024)

		if addr not in clients:
			clients.append(addr)

		itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

		print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime + "]/", end="")
		print(data.decode("utf-8"))

		for client in clients:
			if addr != client:
				s.sendto(data, client)
	except:
		print("\n###### [Server Stopped] ######")
		power = False

s.close() 