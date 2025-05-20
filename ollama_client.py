# https://github.com/ollama/ollama-python
from ollama import Client
client = Client(
  host='http://localhost:11432',
  headers={'Content-Type': 'application/json'}
)
response = client.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response)