import socket

s = socket.socket() 

host = "192.168.43.196"                        
port = 23457

try:
    s.connect((host, port))                               
except:
    print("Unable to establish socket: " + str(host) + ":" + str(port))
else:
    handshake = s.recv(1024)
    print(handshake.decode())

    out_msg = ""

    while out_msg != "x":
        out_msg = input("Message to send to server: ")
        s.send(out_msg.encode())
    s.close()
    print("Disconnecting to: " + str(host) + ":" + str(port))

