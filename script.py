import fileinput
import re
import sys

floating_re = re_raise_line = re.compile(r"(?<=\s)\d+\.\D.")


def run(filename):
    for line in fileinput.input(filename, inplace=True):

        line = line.strip()
        match = floating_re.search(line)
        if not match:
            print(line)
            continue

        # TODO: actually update new_line
        new_line = line
        print(new_line, end='')


if __name__ == "__main__":
    filename = sys.argv[1]
    run(filename)
