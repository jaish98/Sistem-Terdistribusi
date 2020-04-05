import socket as sok

TCP_IP="192.168.1.26"
TCP_PORT=5512
BUFFER_SIZE =1024

s=sok.socket(sok.AF_INET, sok.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(5)

while 1:
    conn, addr= s.accept()
    print("Alamat: ", addr)
    reqFile = conn.recv(BUFFER_SIZE)
    print(reqFile)
    with open(reqFile.decode(), 'rb') as file_to_send:
        for data in file_to_send:
            print(data)
            conn.send(data)      
    conn.close()
    
s.close()

