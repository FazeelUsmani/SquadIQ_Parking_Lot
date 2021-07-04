import os
from typing import IO

def read_file(file_name: str) -> IO:
    try:
        if os.path.getsize(file_name) == 0:
            print('File is empty')
            exit(1)
        return open(file_name)
    except FileNotFoundError as msg:
        # Custom exception
        print('The file ', file_name, 'does not exist,' 
                'please check the file name and try again.', msg)
        exit(1)


def parse_line(line):
    command, *args = line.strip().split(' ')
    return command, args
