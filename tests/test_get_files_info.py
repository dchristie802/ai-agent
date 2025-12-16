
import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_get_files_current_directory(self):
        result = get_files_info("calculator", ".")
        self.assertIn("main.py", result)
        self.assertIn("pkg", result)
        self.assertNotIn("Error:", result)

    def test_get_files_pkg_directory(self):
        result = get_files_info("calculator", "pkg")
        self.assertIn("calculator.py", result)
        self.assertIn("render.py", result)
        self.assertNotIn("Error:", result)

    def test_get_files_outside_bin(self):
        result = get_files_info("calculator", "/bin")
        self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')

    def test_get_files_parent_directory(self):
        result = get_files_info("calculator", "../")
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')

if __name__ == '__main__':
    unittest.main()
