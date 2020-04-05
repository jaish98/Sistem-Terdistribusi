import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://192.168.1.21:8001")

with open("hasil_download.txt","wb") as handle:
    handle.write(proxy.file_download().data)
    
    
    
