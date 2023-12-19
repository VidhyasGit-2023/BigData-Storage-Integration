# BigData-Storage-Integration
Linux-GCP-Hadoop-Hive-Kafka-Spark-Scala

Requirements:
NewsAPI, clean and process it, and load it into a Spark DataFrame for analysis and predictions. You will be using Apache Kafka for data ingestion into HDFS, Spark SQL module for data analysis and Spark ML for prediction.

Project Solution Report:

As per the instruction using the email ID an account is created in the following portal for NewsAPI – https://newsapi.org/. Received the specific client ID in order to access the NewsArticle API. 
To utilize the Apache Kafka in the GCP terminal zookeeper and confluent should be available and the corresponding servers had to be started. There was a challenge as earlier I was using cloudera. So, I have freshly installed and started the servers. 
Once the servers are started successfully, then a new topic needs to be created with the corresponding brokers distribution and factors. Since I was executing the full process multiple times the topic was already available and topic name is "vidhya-my-news".
Challenges Faced:
Since I have been using Cloudera and this is the first time I am using GCP, so it was bit challenging to start with the project but managed and learned to work with GCP as well. Initially I didn’t install the zookeeper and confluent assuming that it would be existing but then Identified and I have installed and started successfully. Then the next challenge was I was getting an error that the broker was not available when Python file was executed then resolved the issue that we need to create a new topic and then use the same topic in the producer and consumer python file and to have the python files in the root path and execute those files in the terminal and then it worked properly. Finally, there was a challenge in reading and writing the stream but followed the lecture exercise and achieved and completed it.
Python file has been created to initiate the consumer with the same topic and group_id and the consumer creation python file has been executed and it is waiting for the producer to send the message. Once the Producer sends the message the Consumer will receive the message and write each of the message into HDFS storage in a specific path.
Python file has been created to initiate the producer with the same topic and group_id and the producer creation python file has been executed and the Producer is initiated and it is retrieving the list of article from the NewsAPI.
Now start the spark shell server and scale mode is ON.
In the scala mode, define the structure of message which is stored in the HDFS storage and using the read stream to read the message continuously and using the write stream append the message to the actual file.
Validating if the stored file is stored properly in the defined structure
With the spark-shell server running and in the Scala mode execute the Spark scala ML program. In the below program the data which is stored based on the structure will be retrieved using Spark SQL query to executed on “description” column to categorize which article is under positive or negative news based on a couple of positive words. Then using the Logistic Regression with the cleaned data using regex, tokenizer and stopword remover to split the data into test and training data and on the trained model prediction can be generated and finally the accuracy is been evaluated.
Here is the Prediction and the corresponding accuracy evaluator.
