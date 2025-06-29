import time
import random
import paho.mqtt.client as mqtt

broker = "localhost"
topic = "sensores/temperatura"

client = mqtt.Client()
client.connect(broker, 1883)

while True:
    temperatura = round(random.uniform(18.0, 30.0), 2)
    client.publish(topic, f"{temperatura} °C")
    print(f"MQTT → Publicado: {temperatura} °C")
    time.sleep(2)
