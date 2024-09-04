### 🐋️ Lambda Function and Docker

AWS Lambda imposes several quotas that can impact the design and deployment of your functions:

1. **Deployment Package Size:**

ZIP File: The maximum size is 50 MB when uploaded directly or 250 MB when uploaded via Amazon S3.
Docker Image: The maximum size is 10 GB, which allows for more complex dependencies and larger applications.

2. **Memory Allocation:**

Lambda functions can be allocated between 128 MB and 10,240 MB of memory. This memory is shared between your code and the execution environment, including libraries and dependencies.

3. **Execution Timeout:**

The maximum execution timeout for a Lambda function is 15 minutes. If your workload requires longer processing time, you might need to rethink your architecture or split tasks.

4. **Concurrency Limits:**

By default, there is a limit on the number of concurrent executions of Lambda functions, typically set to 1,000 concurrent executions per region, though this can be increased by request.

5. **Environment Variables:**

Lambda functions can have up to 4 KB of environment variables. If your configuration exceeds this limit, you may need to explore alternatives like using Amazon S3 or AWS Secrets Manager.

> Using **Docker** containers as an alternative deployment method helps to bypass these limitations, enabling more complex and scalable applications.
<br>

#### How to create a Docker image

Examples of Docker images [here](https://gallery.ecr.aws/lambda/python).
<br>

* Create a file named `Dockerfile`.

```dockerfile
# Inside config/Dockerfile
RUN echo ' > Init dockerfile. '
FROM public.ecr.aws/lambda/python:3.10
RUN echo '   Using a aws/lambda/python3.10 image as base.'

# Copy requirements.txt
RUN echo ' > Copy requirements.txt ...'
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Copy function code
RUN echo ' > Copy lambda function code ...'
COPY hello.py ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN echo ' > Install requirements.txt ...'
RUN pip install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
RUN echo ' > Defines the default executable of a Docker image as the lambda function ...'
CMD [ "hello.hello_from_docker" ]
```
<br>

* Build the image with a name and give it a _test_ tag:

```bash
    # In root of this project:
    # Dockerfile inside de onfig folder
    # lambda-ex-image is the name of the image
    docker build . --platform linux/amd64 -t lambda-ex-image:test -f config/Dockerfile 
```
<br>

* For see docker images:
```bash
    docker images
```

Example of expected output : 

|REPOSITORY  |    TAG     |   IMAGE ID    |   CREATED   |      SIZE    |
|------------|------------|---------------|-------------|--------------|
|lambda-ex-image |      test |          bd74aba00bdb |  About a minute ago  | 776MB |
<br>

* Test image locally

Open a terminal and run:

```bash
docker run -p 9500:8080 lambda-ex-image:test
```

In other terminal make a request, is expected to return the handler of lambda function:

```bash
curl "http://localhost:9500/2015-03-31/functions/function/invocations" -d '{}'
```

<br>

#### AWS Container Regostry

The `Amazon Elastic Container Registry (ECR)` is a fully managed service that allows you to store, manage, and deploy container images.

<br>

#### 📌 Run the project

**First Steps** 

Install **AWS CLI**, [click here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

```bash
# Configure credentials
$ aws configure --profile mlops
AWS Access Key ID [None]: ????????????
AWS Secret Access Key [None]: ????????????????????????????????
Default region name [None]: us-east-2
Default output format [None]:

# Set profile
$ export AWS_PROFILE=mlops

# List the names of lambda functions associated with your account:
$ aws lambda list-functions --query "Functions[*].FunctionName" --output text
```
<br>

Create a `venv` and install dependencies:

```bash
    # Create environment
    python3 -m venv venv  

    # Activate environment
    source venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt
``` 

Create a `.env` file inside `config/` folder with user and password of RabbitMQ:

```bash
    # .env content'
    AWS_ACCESS_KEY_ID="XXXXXXXXXXXXXX"
    AWS_SECRET_ACCESS_KEY="aaaaaaaaaaaaaaaaaaaaaaaaaaa"
    AWS_REGION="xx-xxxx-2"
    AWS_LAMBDA_ROLE_ARN="arn:xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
``` 

**Run the project** 

Run the project with the following command:

```bash
    python3 main.py
```

Code variables:

```python 
   # ---- Omitted Code ----

    lambda_filename = # Filename that contain the lambda function that will be deployed
    lambda_compress = # Name of filename that contain the zipped lambda function

    lambda_function_name =  # Lambda Function Name in AWS Lambda
    handler_function_name = # Funcion name that will be deplyed
    username = # Username of the account (Optional value)

    layer_name = # Function Layer name  
    layer_package = # .zip dependency package

    api_gateway_name = # Api name

    # ---- Omitted Code ----
``` 

<br>
@2024, Insper. 9° Semester,  Computer Engineering.
<br>

_Machine Learning Ops & Interviews Discipline_