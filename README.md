# DemoADA-TFU
Pasos para ejecutar la demo:

1. Levantar el broker MQTT (Mosquitto)
Abrí una terminal nueva y ejecutá:
    docker run -it --name mosquitto-broker -p 1883:1883 eclipse-mosquitto

Dejá esta terminal abierta y corriendo todo el tiempo.

2. Levantar el broker AMQP (RabbitMQ)
Abrí otra terminal nueva y ejecutá:
    docker run -it --name rabbitmq-broker -p 5672:5672 -p 15672:15672 rabbitmq:3-management

Dejá esta terminal abierta y corriendo todo el tiempo.

3. Ejecutar el simulador MQTT (sensor de temperatura)
Abrí una tercera terminal:
    python mqtt_sensor.py

Simula un sensor que envía temperaturas al broker MQTT cada 2 segundos.

4. Ejecutar el consumidor AMQP (espera órdenes)
Abrí una cuarta terminal:
    python amqp_consumidor.py

Este script se queda escuchando órdenes bancarias desde una cola RabbitMQ.

5. Ejecutar el productor AMQP (envía órdenes)
Abrí una quinta terminal:
    python amqp_productor.py

Este script envía 5 órdenes simuladas a la cola de RabbitMQ, una por segundo.