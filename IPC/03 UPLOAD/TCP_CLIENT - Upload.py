import socket as sok

TCP_IP="192.168.1.26"
TCP_PORT=3215

s=sok.socket(sok.AF_INET, sok.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
f = open('file_upload.txt', 'rb')
l =f.read(2048)
if (1):
    s.send(l)
    l=f.read(2048)
    print("Upload Berhasil")
s.close


