#!/usr/bin/python

import os
import sys


def count_lines(folder, file):
    f_id = open(os.path.join(folder, file), encoding="ISO-8859-1")
    count = sum(1 for _ in f_id)
    f_id.close()
    return count


def count(root):
    total = 0
    for folder, dirs, files in os.walk(root):
        for file in files:
            if file.endswith('.' + sys.argv[2]):
                total += count_lines(folder, file)
    return total


if __name__ == "__main__":
    assert len(sys.argv) == 3, 'Folder name and file extension are required'
    print('Total de linhas', sys.argv[2], ':', count(sys.argv[1]))
