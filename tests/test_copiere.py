"""
Run python tests for copiere:

    > mkvirtualenv --python=python3.9 kata1
    > pip install pytest==7.2.2 .
    > pytest test_copiere.py
"""

import pytest
from unittest.mock import Mock, patch, call, ANY
from copiere.copy import copy_file_or_dir


# patch shutil
def test_copiere_copies_file():
    # Arrange
    # ...

    # Act
    # copy_file_or_dir(myfile, ...)

    # Assert
    # assert that shutil func was called with correct arguments
    # for file copying
    assert False


# patch shutil
def test_copiere_copies_dir():
    # Arrange
    # ...

    # Act
    # copy_file_or_dir(mydir, ...)

    # Assert
    # assert that shutil func was called with correct arguments
    # for directory copying
    assert False
