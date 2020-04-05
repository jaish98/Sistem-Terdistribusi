import socket as sok

TCP_IP="192.168.1.26"
TCP_PORT=12345
BUFFER_SIZE =1024

s=sok.socket(sok.AF_INET, sok.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(5)

while 1:
    conn, addr= s.accept()
    print("Alamat: ", addr)
    data = conn.recv(BUFFER_SIZE)
    print("data diterima: ", data.decode())
    pesan="Pesan diterima jendral!!"
    conn.send(pesan.encode())
conn.close()

