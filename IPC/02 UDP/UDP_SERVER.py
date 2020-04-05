import socket as sok

UDP_IP="192.168.1.26"
UDP_PORT=54321
sock=sok.socket(sok.AF_INET, sok.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
    data, addr= sock.recvfrom(128)
    print(addr)
    print("pesan diterima: ", data.decode())
