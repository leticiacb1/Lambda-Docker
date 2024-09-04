from dataclass.compress import CompressFile
from dataclass.lambda_function import LambdaFunction
from dataclass.gateway import Gateway
from dataclass.container import ContainerRegistry

import time
import requests

# Variaveis
username = 'leticiacb1'
repository_name = 'test1-mlops' + username

try: 
    # Instances
    ecr = ContainerRegistry()

    # Create ECR
    ecr.create_client()
    ecr.create_repository(repository_name= repository_name)

except Exception as e:
    print(f"\n    [ERROR] An error occurred: \n {e}")
finally:
    # Cleaning:
    ecr.cleanup(repository_name= repository_name)