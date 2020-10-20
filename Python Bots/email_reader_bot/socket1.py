import socket

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('mail.google.com/mail', 80))
cmd = 'GET http://mail.google.com/mail/u/0/#inbox HTTP/1.0\n\n'.encode()
mySock.send(cmd)

while True:
    data = mySock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mySock.close()