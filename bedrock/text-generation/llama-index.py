from llama_index.llms.bedrock import Bedrock

resp = Bedrock(
    model="amazon.titan-text-express-v1",
).complete("The TV show The Office cast was ")


print(resp)

