import json
import os
import sys

import boto3

client = boto3.client("bedrock-runtime")


prompt_data = """
Human: 
Sulfuric acid reacts with sodium chloride, and gives <chemical1>_____</chemical1> and <chemical2>_____</chemical2>:
Assistant:
"""

resp = client.invoke_model(
    modelId='anthropic.claude-v2',
    contentType='application/json',
    accept='application/json',
    body=json.dumps({
        "prompt": prompt_data,
        "max_tokens_to_sample": 200,
        "temperature": 1.0
    })
)

body = json.loads(resp.get("body").read())

print(body['completion'])
