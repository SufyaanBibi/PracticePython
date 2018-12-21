import unittest
import tempfile
import os
from CodingPractice.OOPPractice.assignments.LogFile import *


def get_file_contents(file_name):
    with open(file_name, 'r') as file_handle:
        return '\n'.join([line for line in file_handle.readlines()])


def makes_temp():
    os_file_handle, file_path = tempfile.mkstemp()
    os.close(os_file_handle)
    return file_path


class LogFileTests(unittest.TestCase):

    def test_can_write_to_file(self):

        temporary_file = makes_temp()

        lw = LogFile(temporary_file)
        message = 'This is a test.'
        lw.write_line(message)

        log_file_contents = get_file_contents(temporary_file)
        self.assertTrue(message in log_file_contents)

        os.remove(temporary_file)

    def test_can_write_to_delim_file(self):

        tmp_file = makes_temp()

        delim = DelimFile(tmp_file)
        message = ['1', '2', '3']
        delim.write(message)

        delim_file_contents = get_file_contents(tmp_file)
        self.assertTrue('1,2,3' in delim_file_contents)

        os.remove(tmp_file)

    def test_can_write_delim_fields(self):
        tmp_file = makes_temp()

        delim = DelimFile(tmp_file)
        message = ['1', '2', '3,b']
        delim.write(message)

        delim_file_contents = get_file_contents(tmp_file)
        self.assertTrue('1,2,"3,b"' in delim_file_contents)

        os.remove(tmp_file)


if __name__ == '__main__':
    unittest.main()
