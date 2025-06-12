import unittest

from functions.get_files_info import get_files_info


def main():
    print(get_files_info("calculator", "."))
    print(get_files_info("calculator", "pkg"))
    print(get_files_info("calculator", "/bin"))
    print(get_files_info("calculator", "../"))


class TestGetFileInfo(unittest.TestCase):
    def test_dot_dir(self):
        actual_output = get_files_info("calculator", ".")
        expected_output = 'Error: Cannot list "." as it is outside the permitted working directory'
        self.assertEqual(actual_output, expected_output)

    def test_pgk_dir(self):
        actual_output = get_files_info("calculator", "pgk")
        expected_output = 'Error: "pgk" is not a directory'
        self.assertEqual(actual_output, expected_output)

    def test_bin_dir(self):
        actual_output = get_files_info("calculator", "/bin")
        expected_output = 'Error: Cannot list "/bin" as it is outside the permitted working directory'
        self.assertEqual(actual_output, expected_output)

    def test_parent_dir(self):
        actual_output = get_files_info("calculator", "../")
        expected_output = 'Error: Cannot list "../" as it is outside the permitted working directory'
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    main()
