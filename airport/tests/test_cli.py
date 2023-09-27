import unittest
from click.testing import CliRunner
from cli import cli  # Import your CLI module

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_add_visitor(self):
        result = self.runner.invoke(cli, ["add_visitor", "--name", "John", "--passport_number", "123"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Visitor added successfully.", result.output)

    # Similar test methods for other commands

if __name__ == "__main__":
    unittest.main()
