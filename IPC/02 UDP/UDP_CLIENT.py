import socket as sok

UDP_IP="10.20.1.161"
UDP_PORT=54321
Pesan="Selamat Datang Jendral AZZAM"
i=0
while i<10:
    
    soc=sok.socket(sok.AF_INET, sok.SOCK_DGRAM)

    soc.sendto(Pesan.encode(), (UDP_IP,UDP_PORT))
    i=i+1

