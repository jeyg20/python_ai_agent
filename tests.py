import unittest

from functions.path_util import get_file_content, get_files_info, run_python_file, write_file


def main():
    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))


class TestGetFileInfo(unittest.TestCase):
    def test_dot_dir(self):
        actual_output = get_file_content("calculator", ".")
        expected_output = 'Error: Cannot list "." as it is outside the permitted working directory'
        self.assertEqual(actual_output, expected_output)

    def test_pgk_dir(self):
        actual_output = get_file_content("calculator", "pgk")
        expected_output = 'Error: "pgk" is not a directory'
        self.assertEqual(actual_output, expected_output)

    def test_bin_dir(self):
        actual_output = get_file_content("calculator", "/bin")
        expected_output = 'Error: Cannot list "/bin" as it is outside the permitted working directory'
        self.assertEqual(actual_output, expected_output)

    def test_parent_dir(self):
        actual_output = get_file_content("calculator", "../")
        expected_output = 'Error: Cannot list "../" as it is outside the permitted working directory'
        self.assertEqual(actual_output, expected_output)

    def test_write_file(self):
        actual_output = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        expected_outut = 'Successfully wrote to "lorem.txt" (28 characters written)'
        self.assertEqual(actual_output, expected_outut)

    def test_write_file_parent_dir(self):
        actual_output = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        expected_outut = 'Successfully wrote to "pkg/morelorem.txt" (26 characters written)'
        self.assertEqual(actual_output, expected_outut)

    def test_file_outside_working_dir(self):
        actual_output = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        expected_outut = 'Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory'
        self.assertEqual(actual_output, expected_outut)


if __name__ == "__main__":
    main()
