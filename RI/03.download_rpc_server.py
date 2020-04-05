from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def file_download():
	with open("file_didownload.txt",'rb') as handle:
		return xmlrpc.client.Binary(handle.read())        
        
server = SimpleXMLRPCServer(("192.168.1.21", 8001),allow_none=True)
print ("Listening on port 8001")
server.register_function(file_download, 'file_download')s
server.serve_forever()
