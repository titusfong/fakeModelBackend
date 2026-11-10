import os 
from dotenv import load_dotenv
from model_backend import ModelRequest, ModelResponse   
from openai import OpenAI

load_dotenv()
class OpenAIModelBackend:
    def generate(self, request: ModelRequest) -> ModelResponse:
        if request.prompt == "" or request.prompt is None or request.prompt.isspace():
            raise ValueError("Prompt cannot be empty or whitespace")
        if request.request_id == "" or request.request_id is None or request.request_id.isspace():
            raise ValueError("Request ID cannot be empty or whitespace")
        with OpenAI(api_key=os.getenv("OPENAI_API_KEY"), max_retries=0,  timeout=30) as client:
            response = client.responses.create(
                model="gpt-5-nano",
                input=request.prompt,
                max_output_tokens=512
            )
            if response.status != "completed":
                raise RuntimeError(f"The program is not yet complete; its current status is: {response.status}")
            if not response.output_text or response.output_text == "":
                raise RuntimeError("The response text is empty")
            return ModelResponse(request_id=request.request_id, text=response.output_text, backend="openai")

if __name__ == "__main__":
    self.main()