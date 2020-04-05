# import paho mqtt
import paho.mqtt.client as mqtt

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime

# definisikan nama broker yang akan digunakan
broker_address = "192.168.43.114"

# buat client baru bernama P2
print("Creating new instance")
client = mqtt.Client("P2")

#client.on_publish=on_publish

# koneksi ke broker
print("Connecting to broker")
client.connect(broker_address, port=1883)

# mulai loop client
client.loop_start()

# lakukan 20x publish waktu dengan topik 1
print("Publish something")

for i in range (20):
    # sleep 1 detik
    time.sleep(1)
    
    # publish waktu sekarang
    client.publish("waktu", f'{datetime.datetime.now()}')

#stop loop
client.loop_stop()