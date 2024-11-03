import json
import os
import sys

import boto3


client = boto3.client("bedrock-runtime")


prompt_data = """
On a given week, the viewers for a TV channel were
Monday: 6500 viewers
Tuesday: 6400 viewers
Wednesday: 6300 viewers


Question: How many viewers can we expect on Friday?
Answer: Based on the numbers given and without any more information, there is a daily decrease of 100 viewers. If we assume this trend will continue during the following days, we can expect 6200 viewers on the next day that would be Thursday, and therefore 6100 viewers on the next day that would be Friday.

Question: How many viewers can we expect on Saturday? (Think Step-by-Step)
Answer: ?

Solve the anwser
"""

resp = client.invoke_model(
        modelId='amazon.titan-text-express-v1',
        body=json.dumps({
            "inputText": prompt_data
        })
)

body = json.loads(resp.get("body").read())

print("######## FULL RESPONSE ################")
print(resp)

print("######## TOKEN INPUT COUNT ################")
print(resp['ResponseMetadata']['HTTPHeaders']["x-amzn-bedrock-input-token-count"])

print("######## TOKEN INPUT COUNT ################")
print(resp['ResponseMetadata']['HTTPHeaders']["x-amzn-bedrock-output-token-count"])

print("######## MODEL RESPONSE ################")
print(body['results'][0]['outputText'])

