from confluent_kafka import Consumer, KafkaException, KafkaError
import concurrent.futures
from queue import Queue

# Kafka consumer configuration (same as before)
bootstrap_servers = 'your_kafka_broker:9092'
group_id = 'your_consumer_group'
topic = 'your_topic_name'
conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False
}

# Create a Kafka consumer (same as before)
consumer = Consumer(conf)
consumer.subscribe([topic])

# Create a blocking queue with a maximum size of 20
blocking_queue = Queue(maxsize=20)

# Function to consume messages from Kafka
def consume_kafka():
    while True:
        # Poll for messages
        messages = consumer.consume(num_messages=100, timeout=1.0)

        # Process the polled messages
        for message in messages:
            if message is None:
                continue
            elif not message.error():
                # Put the message into the blocking queue
                blocking_queue.put(message)

                # Commit the message offset
                consumer.commit(message)
            elif message.error().code() == KafkaError._PARTITION_EOF:
                # End of partition reached
                print('Reached end of partition {}, offset {}:'.format(message.topic(), message.offset()))
            else:
                # Error occurred
                print('Error occurred: {}'.format(message.error().str()))

        # If the number of messages polled is less than 100, sleep for 10 seconds
        if len(messages) < 100:
            time.sleep(10)

# Function to process messages from the blocking queue
def process_messages():
    while True:
        message = blocking_queue.get()  # Get a message from the blocking queue
        process_message(message)  # Process the message

# Function to process the Kafka message
def process_message(message):
    # Implement your message processing logic here
    pass

# Create and start the threads
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit the Kafka consumer function to the executor
    kafka_consumer_thread = executor.submit(consume_kafka)
    # Submit the process_messages function to the executor
    process_messages_thread = executor.submit(process_messages)

# Wait for the Kafka consumer thread to finish (use KeyboardInterrupt to stop)
try:
    while not kafka_consumer_thread.done() or not process_messages_thread.done():
        time.sleep(1)
except KeyboardInterrupt:
    pass

finally:
    # Close the consumer
    consumer.close()
