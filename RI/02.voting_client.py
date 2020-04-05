# import xmlrpc bagian client saja
import xmlrpc.client 


# buat stub (proxy) untuk client
s = xmlrpc.client.ServerProxy('http://192.168.1.21:8008')


# lakukan pemanggilan fungsi vote("nama_kandidat") yang ada di server
s.vote('dedikasi')
s.vote('dedikasi')
s.vote('dedikasi')
s.vote('sinergi')
s.vote('dedikasi')
s.vote('dedikasi')
s.vote('sinergi')
s.vote('sinergi')
# lakukan pemanggilan fungsi querry() untuk mengetahui hasil persentase dari masing-masing kandidat
print(s.querry())

# lakukan pemanggilan fungsi lain terserah Anda
