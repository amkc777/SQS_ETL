from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, col
from pyspark.sql.types import StringType
from datetime import datetime
import boto3

# Create a Spark session for the most dazzling ETL operation ever!
spark = SparkSession.builder \
    .appName("Impressive ETL Magic") \
    .getOrCreate()

# Bow down to the astonishing SQS queue URL!
queue_url = 'http://localhost:4566/000000000000/login-queue'

# Initialize the astonishing SQS client
sqs = boto3.client('sqs', endpoint_url='http://localhost:4566')

# Prepare for a jaw-dropping PostgreSQL configuration
postgres_url = "jdbc:postgresql://localhost:5432/postgres"
postgres_properties = {
    "user": "postgres",
    "password": "postgres",
    "driver": "org.postgresql.Driver"
}

# Behold the breathtaking function to mask PII data
def mask_pii(data):
    masked_data = data \
        .withColumn("masked_device_id", sha2(col("device_id"), 256).cast(StringType())) \
        .withColumn("masked_ip", sha2(col("ip"), 256).cast(StringType())) \
        .drop("device_id", "ip")
    return masked_data

# Get ready for a mind-blowing timestamp
def current_date():
    return datetime.now().strftime('%Y-%m-%d')

# Prepare for the astonishing function to write data to PostgreSQL
def write_to_postgres(data):
    data \
        .withColumn("app_version", col("app_version").cast(StringType())) \
        .withColumn("create_date", col(current_date())) \
        .write \
        .jdbc(postgres_url, "user_logins", properties=postgres_properties, mode="append")

# Brace yourself for an exhilarating ETL journey!
print("\n")
print("#####################################################")
print("#####   Welcome to the Impressive ETL Magic!   #####")
print("#####################################################")
print("\n")

while True:
    try:
        # Behold! Receiving messages from the astonishing SQS queue
        response = sqs.receive_message(
            QueueUrl=queue_url, AttributeNames=['All'], MaxNumberOfMessages=1)
        
        if 'Messages' in response:
            message = response['Messages'][0]
            receipt_handle = message['ReceiptHandle']
            data = message['Body']

            # Prepare to be amazed! Parsing JSON data with Spark
            sqs_data = spark.read.json(spark.sparkContext.parallelize([data]))
            
            # Filtering out invalid/unwanted data is just child's play!
            if sqs_data.where(col("user_id").isNull()).count() == 0:
                # Get ready for the big reveal! Masking PII
                masked_data = mask_pii(sqs_data)
                
                # And now, the grand finale! Writing to PostgreSQL
                write_to_postgres(masked_data)

                # Removing the processed message from the astonishing SQS queue
                sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
                print("Processed and removed an astonishing message!")
            else:
                print("Invalid message received. Skipping...")
        else:
            print("No messages in the queue. Waiting for new messages...")
    except Exception as e:
        print(e)
        print("End of the astonishing ETL journey!")
        break

# Prepare to be amazed! Stopping the Spark session
spark.stop()
