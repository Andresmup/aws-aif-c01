import json
import os
import sys
import boto3

client = boto3.client("bedrock-runtime")

prompt_data = """
Please provide a summary of the following text, please do not exceed 30 words. Do not add any information that is not mentioned in the text below.

<text>
AWS took all of that feedback from customers, and today we are excited to announce Amazon Bedrock, \
a new service that makes FMs from AI21 Labs, Anthropic, Stability AI, and Amazon accessible via an API. \
Bedrock is the easiest way for customers to build and scale generative AI-based applications using FMs, \
democratizing access for all builders. Bedrock will offer the ability to access a range of powerful FMs \
for text and images—including Amazons Titan FMs, which consist of two new LLMs we’re also announcing \
today—through a scalable, reliable, and secure AWS managed service. With Bedrock’s serverless experience, \
customers can easily find the right model for what they’re trying to get done, get started quickly, privately \
customize FMs with their own data, and easily integrate and deploy them into their applications using the AWS \
tools and capabilities they are familiar with, without having to manage any infrastructure (including integrations \
with Amazon SageMaker ML features like Experiments to test different models and Pipelines to manage their FMs at scale).
</text>
"""

body = json.dumps({
    "inputText": prompt_data,
    "textGenerationConfig": {
        "maxTokenCount":1024,
        "stopSequences":[],
        "temperature":0,
        "topP":1
    }
})

resp = client.invoke_model(
    body=body, 
    modelId="amazon.titan-tg1-large", 
    accept='application/json', 
    contentType='application/json'
)

body = json.loads(resp.get('body').read())


print(body.get('results')[0].get('outputText'))
