import unittest
from model_backend import FakeModelBackend
from model_backend import ModelRequest

class TestFakeModelBackend(unittest.TestCase):
    def test_generate_returns_expected_response(self):
        backend = FakeModelBackend(reply_text="Scan requested.")
        request = ModelRequest(
            request_id="req-001",
            prompt="Please scan this synthetic text.",
        )

        response = backend.generate(request)
        self.assertEqual(response.backend , "fake")
        self.assertEqual(response.text, "Scan requested.")
        self.assertEqual(response.request_id, "req-001")

    def test_generate_returns_different_request_id(self):
        backend = FakeModelBackend(reply_text="Scan requested.")
        request = ModelRequest(
            request_id="req-002",
            prompt="Please scan this synthetic text.",
        )

        response = backend.generate(request)
        self.assertEqual(response.backend , "fake")
        self.assertEqual(response.text, "Scan requested.")
        self.assertEqual(response.request_id, "req-002")

    def test_generate_returns_different_request_id_same_backend(self):
        backend = FakeModelBackend(reply_text="Scan requested.")
        requestA = ModelRequest(
            request_id="req-001",
            prompt="Please scan this synthetic text.",
        )
        requestB = ModelRequest(
            request_id="req-002",
            prompt="Please scan this synthetic text.",
        )
        responseA = backend.generate(requestA)
        responseB = backend.generate(requestB)
        self.assertEqual(responseA.backend , "fake")
        self.assertEqual(responseA.text, "Scan requested.")
        self.assertEqual(responseA.request_id, "req-001")
        self.assertEqual(responseB.backend , "fake")
        self.assertEqual(responseB.text, "Scan requested.")
        self.assertEqual(responseB.request_id, "req-002")

    
    def test_generate_prompt_is_white_space(self):
        backend = FakeModelBackend(reply_text="Scan requested.")
        request = ModelRequest(
            request_id="req-003",
            prompt="   ",
        )

        with self.assertRaises(ValueError):
            backend.generate(request)

    def test_generate_request_id_is_white_space(self):
        backend = FakeModelBackend(reply_text="Scan requested.")
        request = ModelRequest(
            request_id=" ",
            prompt="Please scan this synthetic text.",
        )

        with self.assertRaises(ValueError):
            backend.generate(request)

    def test_generate_returns_expected_response_A_B(self):
        backendA = FakeModelBackend(reply_text="reply_A")
        backendB = FakeModelBackend(reply_text="Scan requested.")

        requestA= ModelRequest(
            request_id="req-001",
            prompt="Please scan this synthetic text.",
        )

        requestB= ModelRequest(
            request_id="req-002",
            prompt="Please scan this synthetic text.",
        )
        responseA = backendA.generate(requestA)
        responseB = backendB.generate(requestB)
        responseA = backendA.generate(requestA)

        self.assertEqual(responseA.backend , "fake")
        self.assertEqual(responseA.text, "reply_A")
        self.assertEqual(responseA.request_id, "req-001")
        self.assertEqual(responseB.backend , "fake")
        self.assertEqual(responseB.text, "Scan requested.")
        self.assertEqual(responseB.request_id, "req-002")
        self.assertIsNot(responseA, responseB)

    def test_generate_returns_expected_response_twice(self):
        backend = FakeModelBackend(reply_text="Scan requested.")
        requestA = ModelRequest(
            request_id="req-001",
            prompt="Please scan this synthetic text.",
        )
        requestB = ModelRequest(
            request_id="req-002",
            prompt="Please scan this synthetic text.",
        )
        response = backend.generate(requestA)
        self.assertEqual(response.backend , "fake")
        self.assertEqual(response.text, "Scan requested.")
        self.assertEqual(response.request_id, "req-001")
        response = backend.generate(requestB)
        self.assertEqual(response.backend , "fake")
        self.assertEqual(response.text, "Scan requested.")
        self.assertEqual(response.request_id, "req-002")
        self.assertIsNot(backend.generate(requestA), backend.generate(requestB))
        response_a = backend.generate(requestA)
        response_b = backend.generate(requestA)

        self.assertEqual(response_a, response_b)
        self.assertIsNot(response_a, response_b)

    def test_generate_prompt_is_empty(self):
        backend = FakeModelBackend(reply_text="Scan requested.")
        request = ModelRequest(
            request_id="req-003",
            prompt="",
        )

        with self.assertRaises(ValueError):
            backend.generate(request)

    def test_generate_request_id_is_empty(self):
        backend = FakeModelBackend(reply_text="Scan requested.")
        request = ModelRequest(
            request_id="",
            prompt="Please scan this synthetic text.",
        )

        with self.assertRaises(ValueError):
            backend.generate(request)



    def test_generate_returns_empty_response(self):
        backend = FakeModelBackend(reply_text="")
        request = ModelRequest(
            request_id="req-001",
            prompt="Please scan this synthetic text.",
        )

        response = backend.generate(request)
        self.assertEqual(response.backend , "fake")
        self.assertEqual(response.text, "")
        self.assertEqual(response.request_id, "req-001")

    def test_generate_returns_space_request(self):
        backend = FakeModelBackend(reply_text="Scan requested.")
        request = ModelRequest(
            request_id=" req-001 ",
            prompt=" Please scan this synthetic text. ",
        )

        response = backend.generate(request)
        self.assertEqual(response.backend , "fake")
        self.assertEqual(response.text, "Scan requested.")
        self.assertEqual(response.request_id, " req-001 ")
        self.assertEqual(request.request_id, " req-001 ")
        self.assertEqual(request.prompt, " Please scan this synthetic text. ")
        
if __name__ == "__main__":
    unittest.main()