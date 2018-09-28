import tempfile
import unittest
import os
import pickle


def makes_temp():
    os_file_handle, file_path = tempfile.mkstemp()
    os.close(os_file_handle)
    return file_path


def pickle_file(obj, temp_file):
    with open(temp_file, 'wb') as fh:
        pickle.dump(obj, fh, protocol=pickle.HIGHEST_PROTOCOL)


def pickle_load(temp_file):
    with open(temp_file, 'rb') as file_handle:
        return pickle.load(file_handle)


class TestPickle(unittest.TestCase):

    def test_00_can_pickle_dict(self):
        im = {1: 'a', 2: 'b', 3: 'c'}
        temp_file = makes_temp()

        pickle_file(im, temp_file)

        loaded_im = pickle_load(temp_file)

        self.assertEqual(im, loaded_im)

        os.remove(temp_file)


if __name__ == '__main__':
    unittest.main()
