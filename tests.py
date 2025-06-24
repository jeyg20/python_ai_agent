import unittest

from functions.get_file_content import get_file_content


def main():
    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))


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


if __name__ == "__main__":
    main()
