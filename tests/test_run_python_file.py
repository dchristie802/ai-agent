import unittest
from functions.run_python_file import run_python_file

class TestRunPythonFile(unittest.TestCase):
    def test_run_main_py_no_args(self):
        result = run_python_file("calculator", "main.py")
        self.assertIn("Calculator App", result)
        self.assertIn("Usage:", result)

    def test_run_main_py_with_args(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        self.assertIn('"result": 8', result)  # JSON output

    def test_run_tests_py(self):
        result = run_python_file("calculator", "tests.py")
        # Assuming tests run, check for output
        self.assertNotIn("Error:", result)

    def test_run_outside_directory(self):
        result = run_python_file("calculator", "../main.py")
        self.assertEqual(result, 'Error: Cannot execute "../main.py" as it is outside the permitted working directory')

    def test_run_nonexistent_file(self):
        result = run_python_file("calculator", "nonexistent.py")
        self.assertEqual(result, 'Error: File "nonexistent.py" not found.')

    def test_run_non_python_file(self):
        result = run_python_file("calculator", "lorem.txt")
        self.assertEqual(result, 'Error: "lorem.txt" is not a Python file.')

if __name__ == '__main__':
    unittest.main()
