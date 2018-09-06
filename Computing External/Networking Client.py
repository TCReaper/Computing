import socket

s = socket.socket()

host = socket.gethostname()
port = 80

s.connect(('172.16.3.174',port))
s.send("GET / HTTP/1.0\r\n\r\n".encode(encoding='utf-8'))

chunks = []
while True:
      chunk = s.recv(2048).decode()
      if not chunk:
            break
      chunks.append(chunk)
s.close()
print("".join(chunks))

      
