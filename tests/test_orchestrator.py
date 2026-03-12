import unittest
from src.orchestrator import CodeGenOrchestrator

class TestOrchestrator(unittest.TestCase):
    def setUp(self):
        self.orchestrator = CodeGenOrchestrator()

    def test_basic_flow(self):
        result = self.orchestrator.run("Return sum of list")
        self.assertIn("code", result)
        self.assertEqual(result["status"], "success")

if __name__ == "__main__":
    unittest.main()
