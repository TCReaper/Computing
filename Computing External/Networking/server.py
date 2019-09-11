import socket

s = socket.socket()
host = "192.168.43.196"
port = 23456

s.bind((host, port))

s.listen(100)
while True:
    c_soc, addr = s.accept()
    print("Connection from: " + str(addr))

    msg = "Connected to: " + str(host) + ":" + str(port)
    c_soc.send(msg.encode())

    in_msg = ""

    while in_msg != "x":
        in_msg = c_soc.recv(1024).decode()
        print("{0}: {1}".format(str(addr),in_msg))
    c_soc.close()
    print("Disconnected: " + str(host) + ":" + str(port))
