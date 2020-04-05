# import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer


# import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler

import threading

# Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Buat server
with SimpleXMLRPCServer(("192.168.1.21", 8008),requestHandler=RequestHandler,allow_none=True) as server:
    server.register_introspection_functions()
    # buat data struktur dictionary untuk menampung nama_kandidat dan hasil voting
    my_dict = {'dedikasi':0, 'sinergi':0}
    
    # kode setelah ini adalah critical section, menambahkan vote tidak boeh terjadi race condition
    # siapkan lock
    lock = threading.Lock()
    
    #  buat fungsi bernama vote_candidate()
    def vote_candidate(x):
        
        # critical section dimulai harus dilock
        lock.acquire()
        # s kandidat ada dalam dictionary maka tambahkan  nilai votenya
        if x in my_dict:
            my_dict[x] =  my_dict[x]+1
        
        # critical section berakhir, harus diunlock
        lock.release()
        
    
    # register fungsi vote_candidate() sebagai vote
    server.register_function(vote_candidate, 'vote')

    # buat fungsi bernama querry_result
    def querry_result():
        # critical section dimulai
        lock.acquire()
        
        # hitung total vote yang ada
        total_vote = my_dict['dedikasi'] + my_dict['sinergi']
        
        # hitung hasil persentase masing-masing kandidat
        persentase_dedikasi = my_dict['dedikasi']/total_vote*100
        persentase_sinergi = my_dict['sinergi']/total_vote*100

        return persentase_sinergi,persentase_dedikasi
        
        # critical section berakhir
        lock.release()
        
    # register querry_result sebagai querry
    server.register_function(querry_result, 'querry')    


    print ("Server voting berjalan...")
    # Jalankan server
    server.serve_forever()
    
