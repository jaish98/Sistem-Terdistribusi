# import library socket karena akan digunakan request reply protocol sederhana
import socket as sock

# definisikan IP dan port dari webserver yang akan kita gunakan. Port HTTP adalah 80
IP= "192.168.1.22"
port= 8080


buffersize=1024

# buat socket bertipe TCP
s=sock.socket(sock.AF_INET, sock.SOCK_STREAM)

# lakukan binding 

s.bind((IP,port))
# socket mendengarkan
s.listen(1)

# tampilkan dengan print () "Server berjalan dan melayani HTTP pada port xx"
print("Server Berjalan dan Melayani HTTP pada port 8080")

# loop forever
while True:
    # socket menerima koneksi
    conn, addr=s.accept()
    
    # socket menerima data
    
    data=conn.recv(buffersize)
    # print data hasil koneksi
    print("data hasil koneksi", data.decode())
    
    # buat response sesuai spesifikasi HTTP untuk diberikan kepada client
    http_response = """\HTTP/1.1 200 OK

<html>
<head>
<title>Web Server Sederhana</title>
</head>
<body>

<h1>Web Server Sederhana</h1>
<p>Ini adalah contoh paragraf.</p>
<p>Webserver Kelompok Salman,Abudllah,Jaish,Haris. </p>
<p> Haris Saputra (1301174227)</p>
<p> Abdullah Azzam (1301174360)</p>
<p> Salman Rachmadi (1301174440)</p>
<p> Jaish Muhammad (1301174542)</p>
<img src="https://www.surfertoday.com/images/stories/surfetiquette.jpg">

</body>
</html>
"""
    # kirim response kepada client dengan sendall() jangan lupa diencode response dengan utf-8 
    conn.sendall(http_response.encode('utf-8'))
    print("Send all data response")
    
    # tutup koneksi
conn.close()
    

# Selamat! Kamu telah berhasil membuat web server sederhana. 
