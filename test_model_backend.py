import unittest
from model_backend import FakeModelBackend
from model_backend import ModelRequest

class TestFakeModelBackend(unittest.TestCase):
    def test_zero(self):
        backend = FakeModelBackend(reply_text="Scan requested.")
        request = ModelRequest(
            request_id="req-001",
            prompt="Please scan this synthetic text.",
        )

        response = backend.generate(request)
        self.assertEqual(response.backend , "fake")
