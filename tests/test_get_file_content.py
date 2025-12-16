import unittest
from functions.get_file_content import get_file_content

class TestGetFileContent(unittest.TestCase):
    def test_get_existing_file_content(self):
        result = get_file_content("calculator", "lorem.txt")
        self.assertEqual(result, "wait, this isn't lorem ipsum")

    def test_get_main_py_content(self):
        result = get_file_content("calculator", "main.py")
        # Assuming the content is known, but for test, check it's not error
        self.assertIn("import sys", result)
        self.assertFalse(result.startswith("Error:"))

    def test_get_pkg_calculator_content(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        self.assertIn("class Calculator", result)
        self.assertFalse(result.startswith("Error:"))

    def test_get_outside_directory(self):
        result = get_file_content("calculator", "/bin/cat")
        self.assertEqual(result, 'Error: Cannot read "/bin/cat" as it is outside the permitted working directory')

    def test_get_nonexistent_file(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        self.assertEqual(result, 'Error: File not found or is not a regular file: "pkg/does_not_exist.py"')

if __name__ == '__main__':
    unittest.main()
