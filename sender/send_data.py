import pika
import json
import time
import threading

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='sensor_data')

sending = False

def send_data():
    global sending
    sending = True
    while sending:
        sensor_data = {
            'sensor_id': 'sensor_1',
            'temperature': 22.5,
            'humidity': 45.0
        }
        channel.basic_publish(exchange='',
                              routing_key='sensor_data',
                              body=json.dumps(sensor_data))
        print(f"Sent: {sensor_data}")
        time.sleep(10)

def stop_sending():
    global sending
    sending = False

if __name__ == "__main__":
    threading.Thread(target=send_data).start()
