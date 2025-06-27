import unittest

from functions.path_util import get_file_content, get_files_info, write_file


def main():
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


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
