import socket

s = socket.socket()

host = socket.gethostname()
port = 12345
s.bind(('172.16.3.174',port))

host_test = socket.gethostbyname(socket.getfqdn())
socket.gethostname()
print(str(host_test))

s.listen(5)


while True:
      c, addr = s.accept()
      print( 'Got connection from', addr)
      c.send('Thank you for connecting')
      c.close()

      
