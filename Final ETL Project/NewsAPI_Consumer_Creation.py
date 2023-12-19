#pip install kafka-python pydoop
from kafka import KafkaConsumer
import pydoop.hdfs as hdfs

# Kafka consumer configuration
topic = "vidhya-my-news"
brokers = "localhost:9092"
group_id = "bigdata_vidhya_group"

# HDFS configuration
hdfs_host = "hdfs://bigdatavidhya-m:8051"
hdfs_directory = "/home/bigdatabigdata107/news/data"
file_name = "kafka_messages.json"  # Specify the file name for the messages

# Complete HDFS path
hdfs_path = f"{hdfs_host}{hdfs_directory}/{file_name}"

# Create the Kafka consumer
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=brokers,
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    group_id = group_id
)

# Create HDFS directory if it doesn't exist
try:
    hdfs.mkdir(hdfs_directory)
except FileExistsError:
    pass  # Directory already exists

# Consume and save messages to HDFS file
with hdfs.open(hdfs_path, "wb") as writer:
    try:
        for message in consumer:
            # Process the message (cleaning, transforming, etc.)
            cleaned_message = message.value.decode('utf-8')
            # Encode the string to bytes before writing
            encoded_message = cleaned_message.encode('utf-8')
            # Write the encoded message to HDFS
            writer.write(encoded_message + b'\n')  # Write each message to a new line
            print("Message written to HDFS:", cleaned_message)
        # Commit the offset after processing the message
        consumer.commit()
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        consumer.close()