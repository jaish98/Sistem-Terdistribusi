# import paho mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time

# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################
def on_message(client, userdata, message):
    # print pesan
    print(f'Message received: {message.payload.decode("utf-8")}')
########################################
    
# buat definisi nama broker yang akan digunakan
broker_address = "192.168.43.114"

# buat client baru bernama P1
print("Creating new instance")
client = mqtt.Client("P1")

# kaitkan callback on_message ke client
client.on_message = on_message

# buat koneksi ke broker
print("Connecting to broker")
client.connect(broker_address, port=1883)

# jalankan loop client
client.loop_start()

# client melakukan subsribe ke topik 1
print("Subscribing to topic","waktu")
client.subscribe("waktu")