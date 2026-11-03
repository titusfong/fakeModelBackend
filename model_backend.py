from dataclasses import dataclass

@dataclass
class ModelRequest:
    request_id: str
    prompt: str

@dataclass
class ModelResponse:
    request_id: str
    text: str
    backend: str

class FakeModelBackend:
    def __init__(self, reply_text: str):
        self.reply_text = reply_text

    def generate(self, request: ModelRequest) -> ModelResponse:
        reply_text = self.reply_text
        if request.prompt == "" or request.prompt is None or request.prompt.isspace():
            raise ValueError("Prompt cannot be empty or whitespace")
        if request.request_id == "" or request.request_id is None or request.request_id.isspace():
            raise ValueError("Request ID cannot be empty or whitespace")
        return ModelResponse(
            request_id=request.request_id,
            text=reply_text,
            backend="fake"
        )

