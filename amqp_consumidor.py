import pika

def callback(ch, method, properties, body):
    print(f"AMQP ← Recibida: {body.decode()}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='ordenes_bancarias')
channel.basic_consume(queue='ordenes_bancarias', on_message_callback=callback, auto_ack=True)

print("AMQP ← Esperando órdenes bancarias...")
channel.start_consuming()
