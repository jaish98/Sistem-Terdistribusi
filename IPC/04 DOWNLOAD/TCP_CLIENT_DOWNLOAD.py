import socket as sok
import os

TCP_IP="192.168.1.26"
TCP_PORT=5512
BUFFER_SIZE=1024
downloadDir = "\tmp"

filename = "file_didownload.txt"
s=sok.socket(sok.AF_INET, sok.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
s.send(filename.encode())


with open('hasil_download'+".txt", 'wb') as file_to_write:
    data = s.recv(BUFFER_SIZE)
    print(data)
    if data:
        print("file berhasil didownload")
        file_to_write.write(data)
        file_to_write.close()
s.close()

