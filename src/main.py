import sys
import file_reader
import runner

"""Initializing parking lot"""
def initialize_parking_lot(line):
    command, arg = file_reader.parse_line(line)    
    return runner.create_parking_lot(command, arg)


if __name__ == '__main__':
    """
    Run using command line
    python -m main 'tests/input.txt' or ABSOLUTE PATH
    """
    try:
        input_file = sys.argv[1]
    except (IndexError, NameError):
        print("Use command line syntax in below format to run this application\n"
              " python -m main ABSOLUTE_FILE_PATH or simply 'tests/input.txt' ")
        exit()

    with file_reader.read_file(input_file) as file:
        parking_lot = initialize_parking_lot(file.readline())
        for line in file:
            command, args = file_reader.parse_line(line)            
            runner.execute_command(parking_lot, command, args)
