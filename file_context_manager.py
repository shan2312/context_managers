import csv
from collections import namedtuple
from contextlib import contextmanager
import operator


def detect_delimiter(sample_text: str) -> str:
    """Detects delimiter in a piece of text

    Args:
        sample_text (str): Text for which we need to find delimiter

    Returns:
        str: predicted delimiter for this text
    """
    possible_delimiters = [',', ';', '\t', '|']
    delimiter_counts = {delimiter: sample_text.count(delimiter) for delimiter in possible_delimiters}
    return max(delimiter_counts, key=delimiter_counts.get)

class CsvFileReaderContext:
    def __init__(self, filename: str):
        self._filename = filename
        self._file = None
        self._reader = None


    def __enter__(self):
        self._file = open(self._filename, mode = 'r', newline = '\n', encoding='utf-8')

        delim = detect_delimiter(self._file.read(1024))
        self._file.seek(0)
        self._reader = csv.DictReader(self._file, delimiter=delim, quotechar='"')
        if self._reader is None:
            raise TypeError
        headers = self._reader.fieldnames

        if headers is None:
            raise TypeError
        self.tuple = namedtuple('Object', headers)

        return self
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            row = next(self._reader)
            return self.tuple(**row)
        except StopIteration:
            raise

    def __exit__(self, exc_type, exc_value, exc_tb):
        if not self._file.closed:
            self._file.close()

        return False
    

@contextmanager
def csv_file_reader(fname: str) -> namedtuple:
    """Function for reading a csv file lazily using context managers

    Args:
        fname (str): _description_

    Returns:
        namedtuple: _description_

    Yields:
        Iterator[namedtuple]: _description_
    """
    f = open(fname, mode = 'r', newline = '\n', encoding='utf-8')
    delim = detect_delimiter(f.read(1024))
    f.seek(0)
    reader = csv.DictReader(f, delimiter= delim, quotechar='"')

    try:
        headers = reader.fieldnames
        print(headers)
        tup = namedtuple('Object', headers)
        def row_generator():
            for row in reader:
                yield tup(**row)

        yield row_generator()
    finally:
        f.close()

