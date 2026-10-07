# File Organizer CLI

A simple and reliable command-line tool written in Python that organizes files into folders based on their file types.

Instead of manually sorting files, this tool automatically places them into categories such as Documents, Images, Audio, Videos, and Others.

## Features

- Organizes files automatically by extension
- Supports Documents, Images, Audio, Videos, and Others
- Creates category folders automatically
- Handles missing folders with helpful error messages
- Handles permission errors
- Handles duplicate files safely
- Supports `--help`
- Supports `--dry-run`
- Handles Ctrl+C interruption
- Uses meaningful exit codes
- Includes automated tests using pytest

## Technologies Used

- Python
- argparse
- os
- shutil
- pytest

## Project Structure

```text
File-Organizer-CLI/
│
├── fileorganizer/
│   ├── __init__.py
│   ├── __main__.py
│   └── cli.py
│
├── tests/
│   ├── test_errors.py
│   ├── test_file_movement.py
│   └── test_organizer.py
│
└── README.md