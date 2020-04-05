# gunakan library paho
import paho.mqtt.client as mqtt

# gunakan library time
import time

# buat callback pada saat ada pesan masuk
###########################################
def on_message(client, userdata, message):
    # tulis hasil file yang didapat bernama "iris.jpg"
    f = open("iris.jpg", "wb")
    f.write(message.payload)
    f.close()
    print('Photo received')

##########################################
        
# definisikan broker yang akan digunakan
broker_address = "192.168.43.114"

# buat client P2 
print("Creating new instance")
client = mqtt.Client("P2")

# koneksi P2 ke broker
print("Connecting to broker")
client.connect(broker_address, port=1883)


print("Subscribing to topic","photo")
client.subscribe("photo")

# callback diaktifkan
client.on_message = on_message

#client.loop_forever()
while True:
    print("proses..")
    client.loop(15)
    time.sleep(2)