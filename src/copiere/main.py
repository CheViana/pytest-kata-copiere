import pathlib

from copiere.copy import copy_file_or_dir


def run_example():
    """
    When run as main, script expects in working dir:
    - example.txt
    - sour/ex1.txt
    - sour/ex2.txt
    - dest/ - empty directory

    Run:
    > mkvirtualenv --python=python3.9 kata1
    > ... create example files
    > python copiere.py
    """
    copy_file_or_dir(pathlib.Path("example.txt"), "dest")
    copy_file_or_dir(pathlib.Path("sour"), "dest")


if __name__ == '__main__':
    run_example()
