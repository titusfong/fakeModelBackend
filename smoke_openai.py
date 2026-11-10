from openai_backend import OpenAIModelBackend
from model_backend import ModelRequest

backend = OpenAIModelBackend()
request = ModelRequest(request_id="test-001", prompt="Explain a model gateway in one short sentence.")
response = backend.generate(request)
print(response)