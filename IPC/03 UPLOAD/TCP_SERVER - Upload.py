import socket as sok

TCP_IP="192.168.1.26"
TCP_PORT=3215
BUFFER_SIZE =2048

s=sok.socket(sok.AF_INET, sok.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(5)

while 1:
    conn, addr= s.accept()
    print("Alamat: ", addr)
    f = open('hasil_upload'+".txt",'wb')
    while (True):
        l = conn.recv(BUFFER_SIZE)
        if (1):
            f.write(l)
            print("pesan diterima")    

        f.close()
        
    conn.close()
    
s.close()

