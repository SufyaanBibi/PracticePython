import abc
from datetime import datetime


class WriteFile:

    abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return

    def __init__(self, filename):
        self.filename = filename

    def write_line(self, text):
        fh = open(self.filename, 'a')
        fh.write(text)
        fh.close()

    def date_time(self):
        return datetime.datetime.now().strftime('%Y-%M-%D %H:%M')


class DelimFile(WriteFile):

    def __init__(self, filename, delim=','):
        WriteFile.__init__(self, filename)
        self.delim = delim

    def write(self, this_list):
        r = []
        for element in this_list:
            if self.delim in element:
                r.append(f'"{element}"')
            else:
                r.append(element)
        line = self.delim.join(r)
        self.write_line(f'{line} \n')


class LogFile(WriteFile):

    def write(self, this_line):
        self.write_line(f'{date_time()}, {this_line}')
