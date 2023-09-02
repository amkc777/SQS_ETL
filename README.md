### Exercise Details

For a comprehensive understanding of the exercise requirements, please refer to the [Fetch Rewards Data Engineering Exercise](https://fetch-hiring.s3.amazonaws.com/data-engineer/pii-masking.pdf).


### Fetch-Rewards Data Engineering Take Home Project

Welcome to the Fetch-Rewards Data Engineering Take Home Project, where we perform some truly impressive ETL magic! This project showcases our ability to read JSON data from an AWS SQS Queue, transform that data, and write it into a PostgreSQL database. We've spiced up the process with some creative flair to make it an unforgettable experience.

## Overview

This project demonstrates an ETL (Extract, Transform, Load) process to read data from an AWS SQS Queue, mask personally identifiable information (PII) fields, and write the transformed data to a PostgreSQL database. It is designed to meet the requirements outlined in the Fetch Rewards Data Engineering Take Home exercise.

## Project Setup

To set up and run the project, follow these steps:

**Project Overview**

In this project, we have created a Python script that performs the following tasks:

Reads JSON data containing user login behavior from an AWS SQS Queue.
Masks sensitive personal identifiable information (PII) fields, namely device_id and ip, in a way that allows data analysts to identify duplicate values.
Writes each record into a PostgreSQL database.

**Exercise Details**
For detailed exercise instructions, please refer to the Fetch Rewards Data Engineering Task document.

**Prerequisites**
Before you can run this project, ensure that you have the following prerequisites installed on your local machine:

- Install Docker Desktop with Docker Compose: [Docker Install Guide](https://docs.docker.com/get-docker/)
- Install PostgreSQL: [PostgreSQL Download](https://www.postgresql.org/download/)

**Python Dependencies**

Install the required Python libraries:
```bash
pip install subprocess.run psycopg2-binary hashlib awscli-local
```

**Project Setup**

1. **Clone the project repository to your local machine:**
```bash
git clone https://github.com/amkc777/SQS_ETL.git
```
2. **Navigate to the project directory:**
```bash
cd SQS_ETL
```
3. **Start the required Docker containers (Localstack and PostgreSQL):**
```bash
docker-compose up
```
Confirm that the containers are running as expected.

**Running the ETL Pipeline**
Open a terminal and navigate to the project directory.
Run the ETL script to perform data extraction, transformation, and loading:
```bash
python task.py
```
This script will process messages from the SQS queue, mask PII data, and store the transformed data in the PostgreSQL database.

To stop the ETL process, press CTRL + C.

**Development Decisions**

As we developed this solution, we carefully considered several key design choices to ensure the effectiveness of our ETL (Extract, Transform, Load) process:

1. **How Will We Read Messages from the Queue?**
To read messages from the AWS SQS queue, we opted for a straightforward approach using the AWS Command Line Interface (CLI) via a Python subprocess. This decision made it easy to interact with the queue without the need for complex AWS credentials, simplifying the local development setup.

2. **What Type of Data Structures Should Be Used?**
For handling data efficiently, we turned to the PySpark library, a powerful tool for data extraction and transformation. We chose to work with PySpark's DataFrame structure, which allowed us to manage structured data seamlessly and apply transformations with ease.

3. **How Will We Mask PII Data for Duplicate Identification?**
Protecting personally identifiable information (PII), such as device_id and ip, was a priority. To achieve this, we employed the SHA256 hash function provided by Python's hashlib library. This decision not only ensured the security of sensitive data but also enabled us to identify duplicate values accurately. When two inputs produce the same hash, we can confidently identify them as duplicates.

4. **What Is Our Strategy for Connecting and Writing to PostgreSQL?**
To connect to PostgreSQL and write data, we chose the psycopg2 library. psycopg2 simplifies database interactions in Python, making it straightforward to execute SQL queries and commit data to the PostgreSQL database. This choice streamlined our data pipeline and ensured efficient data storage.

5. **Where and How Will Our Application Run?**
Our application is designed to run locally on your development machine. We've provided comprehensive instructions in the Installation and Running the ETL Pipeline sections above to guide you through the setup process. This local setup ensures that you can easily test and develop your ETL process in a controlled environment.

These design decisions were made to prioritize efficiency, data security, and user-friendliness, ensuring a smooth ETL process for local development.


**Deployment in Production**

1. **How Would You Deploy This Application in Production?**

 Deploying this application for production involves a structured approach:

* Setting Up the Foundation: We'll start by creating an AWS SQS Queue to handle incoming messages. Additionally, we'll establish a PostgreSQL database, either within AWS or another cloud provider, to manage our data.
* Containerization: To simplify deployment, we package the application into a Docker container. This containerization makes it easy to move our application across different environments.
* Container Registry: We publish our Docker container to a container registry like Amazon ECR or Docker Hub. This step ensures that our containerized application is readily available for deployment.
* Orchestration and Management: For efficient management and scaling of our application, we rely on container orchestration tools like Kubernetes or AWS ECS. These tools help us maintain multiple instances of our application seamlessly.
* Configuration Handling: We ensure that configuration settings are well-organized, allowing us to easily adapt to different environments while maintaining security and consistency.
* Monitoring and Security: Monitoring and logging using services like AWS CloudWatch or ELK Stack helps us keep a close eye on the health of our application.
Security measures, such as IAM roles and data encryption, are implemented to protect our application and data.

2. **What Other Components Would You Want to Add to Make This Production Ready?**

 To ensure our application is ready for production use, we've considered these additional components:

* Robust Error Handling: Implementing comprehensive error handling allows our application to gracefully handle unexpected issues without causing disruptions.
* Testing Frameworks: We employ a suite of tests, including unit tests, integration tests, and performance tests, to ensure our application's reliability and maintainability.
* CI/CD Automation: We set up continuous integration and continuous deployment (CI/CD) pipelines to automate testing and deployment processes, ensuring smoother and more consistent releases.
* Data Backup and Recovery: We establish automated backup procedures and data recovery mechanisms to safeguard against data loss.
* Scalability Measures:With auto-scaling groups and load balancers, we can dynamically adjust resource allocation to handle increased traffic effectively.
* Data Warehousing Options: For handling larger datasets, we explore data warehousing solutions like AWS Redshift, which offer efficient storage and analytical capabilities.

**Scalability with a Growing Dataset**

3. **How Can This Application Scale with a Growing Dataset?**

 As our dataset grows, we're prepared to handle it seamlessly:

* Load Balancing: We use load balancing to evenly distribute incoming traffic across multiple instances of our application, ensuring optimal performance even during high-demand periods.
* Auto-scaling Groups: By employing auto-scaling groups, our application can automatically adjust the number of instances based on real-time workloads, providing the necessary scalability.
* Efficient Resource Utilization: We optimize the utilization of cloud resources, including CPU and memory, to manage increasing data volumes efficiently.
* Continuous Monitoring: Through continuous monitoring using cloud-native tools, we gain insights into application performance, enabling us to make informed decisions as our dataset continues to expand.
  
**Data Recovery**

4. **How Can PII Be Recovered Later On?**

 Recovering personally identifiable information (PII) is a crucial aspect:

* Secure Data Storage: We securely store the original PII data, including user IDs and sensitive information, in a separate, encrypted location with restricted access.
* Hash Comparison: When the need arises for PII data recovery, we apply the same SHA256 hash function used for masking to the original data.
* Matching Hashes: By comparing the generated hash with the stored hashed values, we can confidently identify the original data corresponding to the masked PII.
  
**Assumptions**

5. **What Assumptions Were Made?**

 During the development of this solution, we worked with the following assumptions:

* Local Development Environment: We assumed that Localstack and PostgreSQL are available locally, allowing us to access them via AWS CLI calls and PostgreSQL, respectively.
* Message Format and Sequence: We expect that messages in the SQS queue are correctly formatted and arrive in the expected sequence for processing.
* Message Deletion: We assumed that messages are promptly deleted from the SQS queue after successful processing and storage in the PostgreSQL database.
* Data Type Adjustment: To accommodate version formats like '2.5.0', we made a necessary adjustment by changing the SQL data type of "app_version" from an integer to char(9).
* AWS Credentials: We opted not to use Boto3, a common AWS SDK for Python, as it typically requires AWS region and credentials, which were neither available nor required for our local development.


Feel free to adapt and extend this project based on your specific requirements. Enjoy working with your impressive ETL pipeline! 🚀

---

**Connect with the Author:**
[LinkedIn](https://www.linkedin.com/in/amkc777/)
