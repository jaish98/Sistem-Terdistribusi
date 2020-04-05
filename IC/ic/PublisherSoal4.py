# import paho
import paho.mqtt.client as mqtt

# definsi broker yang digunakan
broker_address = "192.168.43.114"

# buat client bernama P1
print("Creating new instance")
client = mqtt.Client("P1")

# client terkoneksi ke broker
print("Connecting to broker")
client.connect(broker_address, port=1883)

# print "baca file"
print("Read file")

# buka file surf.jpg
f = open("surf.jpg", "rb")

# baca semua isi file
data = f.read()

# ubah file dalam bentuk byte gunakan fungsi byte()
new = data

# publish dengan topik photo dan data dipublish adalah file
print("Publish photo")
client.publish("photo", new)
#print(data)

# client loop mulai
client.loop_start()

# tutup file
f.close()