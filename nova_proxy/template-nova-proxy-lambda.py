import json
import boto3
import os
from openai import OpenAI

### Secret manager

# This is the name of the secret that will be holding the API key for nova.amazon.com/dev
SECRET_NAME = os.getenv("SECRET_MANAGER_SECRET_NAME", "nova-api-default-secret-holder-name")

# This is the region that the secret is in
REGION = os.getenv("AWS_REGION", "us-east-1")

# This is the secret manager client that will be used to pull the api key from secret manager
secrets_client = boto3.client("secretsmanager", region_name=REGION)

### NOVA API
NOVA_API_DNS = os.getenv("nova_api_dns", "https://api.nova.amazon.com/v1")

### JSON RESPONSE
# Use this field to decide whether you want the full Json object or just the message content output
JSON_RESPONSE = False

# This is the function that you can invoke to pull the api key
def get_api_key():
    """Fetch API key from Secrets Manager."""
    resp = secrets_client.get_secret_value(SecretId=SECRET_NAME)
    # This setup assumes you have the secret in plain text inside of secret manager
    return resp["SecretString"]

def lambda_handler(event, context):
    """
    Expected event:
    {
       "model": "nova-2-lite-v1",
       "messages": [
           {"role": "user", "content": "hello!"}
       ]
    }
    """
    try:
        if isinstance(event, str):
            body = json.loads(event)
        else:
            body = event


        api_key = get_api_key()

        # Initialize OpenAI client for your backend
        client = OpenAI(
            base_url=NOVA_API_DNS,
            api_key=api_key
        )

        # Forward request to backend
        completion = client.chat.completions.create(
            model=body["model"],
            messages=body["messages"]
        )

        if JSON_RESPONSE:
            return {
                "statusCode": 200,
                "body": json.dumps(completion.model_dump())
            }
        else:
            return completion.choices[0].message.content

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

# Use this if you want to test your lambda locally
if __name__ == "__main__":
    example_event = {
       "model": "nova-2-lite-v1",
       "messages": [
           {"role": "user", "content": "hello!"}
       ]
    }
    result = lambda_handler( example_event, {})
    print(json.dumps(result, indent=2))