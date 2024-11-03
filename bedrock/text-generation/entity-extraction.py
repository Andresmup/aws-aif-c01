import json
import os
import sys
import boto3

client = boto3.client("bedrock-runtime")

from pathlib import Path

emails_dir = Path(".") / "emails"
with open(emails_dir / "00_treasure_island.txt") as f:
    book_question_email = f.read()

print(book_question_email)

prompt_data = f"""
You are a helpful assistant that processes orders from a bookstore.

Given the email inside triple-backticks, please read it and analyse the contents.
If a name of a book is mentioned, return it, otherwise return nothing.

Email: ```
{book_question_email}
```
Assistant:
"""

resp = client.invoke_model(
    modelId='anthropic.claude-3-haiku-20240307-v1:0',
    contentType='application/json',
    accept='application/json',
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "messages": [
            {"role": "user","content": [{"type": "text","text": prompt_data }]}
        ],
        "temperature": 0.5,
        "top_p": 0.9
    })
)

body = json.loads(resp.get("body").read())

print(body['content'][0]['text'])
