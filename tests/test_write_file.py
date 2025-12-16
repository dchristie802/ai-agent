import unittest
from functions.write_file import write_file

class TestWriteFile(unittest.TestCase):
    def test_write_valid_file(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        self.assertEqual(result, 'Successfully wrote to "lorem.txt" (28 characters written)')

    def test_write_valid_nested_file(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        self.assertEqual(result, 'Successfully wrote to "pkg/morelorem.txt" (26 characters written)')

    def test_write_outside_directory(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        self.assertEqual(result, 'Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory')

if __name__ == '__main__':
    unittest.main()
