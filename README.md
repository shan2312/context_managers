### README for CSV File Reader

This project provides utilities for reading CSV files using context managers in Python. It includes both a class-based context manager and a function-based context manager for flexible and lazy reading of CSV files with automatic delimiter detection.

## Overview

- **Class-Based Context Manager**: `CsvFileReaderContext` class for reading CSV files and providing rows as named tuples.
- **Function-Based Context Manager**: `csv_file_reader` function for reading CSV files lazily with automatic delimiter detection.

## Features

- **Automatic Delimiter Detection**: Detects the delimiter used in the CSV file.
- **Named Tuple Representation**: Converts each row of the CSV into a named tuple using the header row for field names.
- **Lazy Reading**: Reads CSV files lazily to manage memory efficiently.

## Installation

No additional installation is required. This code uses built-in Python modules and is compatible with Python 3.6 and later.

## Usage

### Class-Based Context Manager

The `CsvFileReaderContext` class allows you to open a CSV file, iterate over rows, and access data as named tuples.

#### Example

```python
from your_module import CsvFileReaderContext  # Replace with the actual module name

file_name = 'data.csv'

with CsvFileReaderContext(file_name) as reader:
    for row in reader:
        print(row.field_name1, row.field_name2)  # Replace with actual field names
```

### Function-Based Context Manager

The `csv_file_reader` function provides an alternative way to read CSV files lazily.

#### Example

```python
from your_module import csv_file_reader  # Replace with the actual module name

file_name = 'data.csv'

with csv_file_reader(file_name) as row_generator:
    for row in row_generator:
        print(row.field_name1, row.field_name2)  # Replace with actual field names
```

## Implementation Details

### `detect_delimiter`

This function detects the delimiter used in a CSV file by analyzing a sample of the file.

#### Arguments

- `sample_text` (str): Text from which to detect the delimiter.

#### Returns

- `str`: The most likely delimiter.

### `CsvFileReaderContext` Class

#### Methods

- `__enter__()`: Opens the file, detects the delimiter, and initializes the CSV reader.
- `__iter__()`: Returns the iterator object.
- `__next__()`: Returns the next row as a named tuple.
- `__exit__(self, exc_type, exc_value, exc_tb)`: Ensures the file is closed properly.

### `csv_file_reader` Function

#### Arguments

- `fname` (str): The path to the CSV file.

#### Yields

- `Iterator[namedtuple]`: Rows of the CSV file as named tuples.

## Error Handling

- **File Not Found**: A `FileNotFoundError` will be raised if the specified file does not exist.
- **Invalid Header**: If the CSV file lacks a header row, the program will raise a `ValueError`.

## Contribution

Contributions are welcome. If you encounter issues or have suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
---