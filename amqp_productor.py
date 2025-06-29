import pika
import time
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='ordenes_bancarias')

for i in range(5):
    orden = f"Orden #{i+1} - Monto: ${random.randint(100, 1000)}"
    channel.basic_publish(exchange='', routing_key='ordenes_bancarias', body=orden)
    print(f"AMQP → Enviada: {orden}")
    time.sleep(1)

connection.close()
