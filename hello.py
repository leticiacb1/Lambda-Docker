import sys
import json

def hello_from_docker(event, context) -> json:
    return {
        "created_by": "leticiacb1",
        "message": "Hello World!",
        "version": sys.version
    }