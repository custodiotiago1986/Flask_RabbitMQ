import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='sensor_data')

data_list = []

def callback(ch, method, properties, body):
    data = json.loads(body)
    data_list.append(data)
    print(f"Received: {data}")

def receive_data():
    channel.basic_consume(queue='sensor_data',
                          on_message_callback=callback,
                          auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    receive_data()
