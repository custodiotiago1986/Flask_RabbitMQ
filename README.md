## RabbitMQ - Flask Example
This project demonstrates how to use RabbitMQ with Flask to send and receive messages between two applications. The sender application sends data every 10 seconds, and the receiver application displays this data in a web interface.
![image](https://github.com/user-attachments/assets/3e3b308f-28a8-4a9c-97f1-c8c664f7cc71)


### Dependencies
Ensure you have the following dependencies installed:

- Python 3.x
- Flask
- pika (Python client for RabbitMQ)
- RabbitMQ server

Install the Python dependencies with:

> pip install flask pika

### RabbitMQ Setup
- Install RabbitMQ: Follow the instructions for your OS on the RabbitMQ website.
- Start RabbitMQ:

For Windows:
> rabbitmq-service.bat install
> rabbitmq-service.bat start

For Unix/Linux:

> sudo service rabbitmq-server start

Enable RabbitMQ Management Plugin:

> rabbitmq-plugins enable rabbitmq_management

Access the RabbitMQ Management Console:
Open a browser and go to http://localhost:15672. The default credentials are:  

Username: guest  
Password: guest  

### Running the Applications
- Sender Application
The sender application sends sensor data every 10 seconds.  
- Navigate to the sender directory.
- Run the application:

> python send_data.py  
![image](https://github.com/user-attachments/assets/e106cb5b-5462-4601-bab1-c1fea40bd70d)
![image](https://github.com/user-attachments/assets/e78842e3-2fa7-4baf-b497-66c35908865a)


- Receiver Application
The receiver application displays received sensor data on a web page.  

- Navigate to the receiver directory. 
- Run the application:  


> python app.py

Open a browser and go to http://localhost:5001 to see the data table.  
![image](https://github.com/user-attachments/assets/122b1628-5b1a-4a13-bece-3caa4f32abfd)


### How It Works
- Sender: Generates sensor data (sensor ID, temperature, humidity) and publishes it to the RabbitMQ queue sensor_data.  
![image](https://github.com/user-attachments/assets/8eca890c-fff4-4d74-9365-4c23f6173485)

- Receiver: Consumes messages from the sensor_data queue and displays the data in a table on the web page. The table is updated every 5 seconds with new data.  
![image](https://github.com/user-attachments/assets/92522a38-66f1-426c-9d72-c04b669fb6b7)


### Monitoring RabbitMQ
You can monitor the message flow and queue status using the RabbitMQ Management Console at http://localhost:15672. Log in with the default credentials and navigate to the "Queues" tab to see the sensor_data queue, where you can observe messages being published and consumed.
![image](https://github.com/user-attachments/assets/cca47959-3f96-4982-bf35-a21af82838b8)


### Notes
Ensure RabbitMQ server is running before starting the applications.
The sender and receiver applications communicate via the RabbitMQ server, which acts as a message broker.
The receiver application uses a separate thread to handle message consumption and Flask to serve the web interface.
