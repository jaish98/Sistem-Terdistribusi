# import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer

# import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler

import threading

# import library yg dibutuhkan
import csv
from pathlib import Path
from datetime import datetime

# insialisasi variabel secara global berbentuk list, untuk menyimpan aktivitas
datas = []

class RequestHandler(SimpleXMLRPCRequestHandler):
    # Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya
    rpc_paths = ('/RPC2',)
    def __init__(self, request, client_address, server):
        # mengosongkan variabel datas, agar setiap aktivitas tidak ter-stack
        datas.clear()
        # inisialisasi timestamp
        request_date = datetime.now().strftime('%A %d-%m-%Y %H:%M')
        # melakukan print ip serta port dari aktivitas client
        print("Alamat IP Client: ",client_address[0]," Port: ",client_address[1])
        # melakukan print timestamp dari aktivitas client
        print("Waktu Aktivitas Client: ",request_date)
        # menyimpan data ip, port, serta timestamp kedalam variabel datas
        datas.extend([client_address[0],client_address[1],request_date])
        SimpleXMLRPCRequestHandler.__init__(self, request, client_address, server)

class CalcFunction:
    # Fungsi untuk menyimpan data kedalam file CSV
    def savetocsv(self, datas):
        # membuka file csv
        with open('log.csv', 'a') as file:
            # inisialisasi untuk melakukan penulisan file
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
            # menulis data yg telah tersedia kedalam file CSV
            writer.writerow(datas)

    # Fungsi untuk operasi penambahan
    def tambah(self,x,y):
        # insialisasi aktivitas yg dilakukan
        activity = 'Melakukan fungsi tambah'
        # melakukan print aktivitas
        print(activity)
        # menyimpan data aktivitas kedalam variabel datas
        datas.append(activity)
        # memanggil fungsi savetocsv
        self.savetocsv(datas)
        # mengembalikan hasil dari fungsi tambah
        return x + y

    # Fungsi untuk operasi pengurangan
    def kurang(self,x,y):
        # insialisasi aktivitas yg dilakukan
        activity = ('Melakukan fungsi kurang')
        # melakukan print aktivitas
        print(activity)
        # menyimpan data aktivitas kedalam variabel datas
        datas.append(activity)
        # memanggil fungsi savetocsv
        self.savetocsv(datas)
        # mengembalikan hasil dari fungsi kurang
        return x - y

    # Fungsi untuk operasi perkalian
    def kali(self,x,y):
        # insialisasi aktivitas yg dilakukan
        activity = ('Melakukan fungsi kali')
        # melakukan print aktivitas
        print(activity)
        # menyimpan data aktivitas kedalam variabel datas
        datas.append(activity)
        # memanggil fungsi savetocsv
        self.savetocsv(datas)
        # mengembalikan hasil dari fungsi kali
        return x * y

    # Fungsi untuk operasi pembagian
    def bagi(self,x,y):
        # insialisasi aktivitas yg dilakukan
        activity = ('Melakukan fungsi bagi')
        # melakukan print aktivitas
        print(activity)
        # menyimpan data aktivitas kedalam variabel datas
        datas.append(activity)
        # memanggil fungsi savetocsv
        self.savetocsv(datas)
        # mengembalikan hasil dari fungsi bagi
        return x / y

    # Fungsi untuk mencari data pada CSV berdasarkan waktu
    def cari(self,x):
        # insialisasi variabel berbentuk list, untuk menyimpan hasil pencarian
        search = []
        # true = file tersedia
        if Path('log.csv').is_file():
            # membuka file csv
            with open('log.csv', 'r') as file:
                # inisialisasi untuk melakukan pembacaan file
                reader = csv.reader(file)
                # looping terhadap jumlah baris yg terdapat pada file
                for num, row in enumerate(reader):
                    # true = ip-nya sesuai & timestamp sesuai
                    if x in row[2] and row[0] == datas[0]:
                        # menyimpan data hasil search kedalam variabel search
                        search.append([row[2],row[3]])
                    else:
                        # menyimpan data hasil search kedalam variabel search
                        search = 'Data tidak ditemukan'
        else:
            # menyimpan data hasil search kedalam variabel search
            search = 'File tidak ditemukan'
        # mengembalikan hasil dari fungsi cari
        return search
        
# Buat server
with SimpleXMLRPCServer(("192.168.1.42", 8008),requestHandler=RequestHandler,allow_none=True) as server:
    print ("Listening on port 8008...")
    # registrasi fungsi untuk client
    server.register_instance(CalcFunction())
    server.register_introspection_functions()
    # menjalankan server
    server.serve_forever()
