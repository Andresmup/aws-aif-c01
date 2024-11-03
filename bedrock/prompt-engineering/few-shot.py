import json
import os
import sys

import boto3

client = boto3.client("bedrock-runtime")

prompt_data = """
Tweet: "I hate it when my phone battery dies.”: Sentiment: Negative
Tweet: "My day has been great”: Sentiment: Positive
Tweet: "This is the link to the article”: Sentiment: Neutral
Tweet: "This new music video was incredible” Sentiment:
"""

resp = client.invoke_model(
    modelId='amazon.titan-text-express-v1',
    body=json.dumps({
        "inputText": prompt_data
    })
)
body = json.loads(resp.get("body").read())

print(body['results'][0]['outputText'])
