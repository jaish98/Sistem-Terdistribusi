import socket as sok

TCP_IP="10.20.1.161"
TCP_PORT=12345
BUFFER_SIZE=1024
Pesan="hello Jendral SALMAN!"

s=sok.socket(sok.AF_INET, sok.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
s.send(Pesan.encode())
data=s.recv(BUFFER_SIZE)

s.close()

print("data di terima: ", data.decode())
