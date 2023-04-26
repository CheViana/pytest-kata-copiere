"""
Run python tests for copiere:

    > mkvirtualenv --python=python3.9 kata1
    > pip install pytest==7.2.2 .
    > pytest test_copiere.py
"""

import pytest
from unittest.mock import Mock, patch, call, ANY
from copiere.copy import copy_file_or_dir


@patch("copiere.copy.shutil")
def test_copiere_copies_file(shutil_mock):
    # Arrange
    file_mock = Mock()
    file_mock.is_dir.return_value = False
    file_mock.name = 'myfile.txt'

    # Act
    copy_file_or_dir(file_mock, "dest")

    # Assert
    assert len(shutil_mock.copy2.call_args_list) == 1
    assert len(shutil_mock.copytree.call_args_list) == 0
    copy_call_args = shutil_mock.copy2.call_args_list[0][0]

    actual_file_to_copy = copy_call_args[0]
    assert actual_file_to_copy.name == 'myfile.txt'

    actual_copy_dest = copy_call_args[1]
    assert actual_copy_dest == 'dest/myfile.txt'


@patch("copiere.copy.shutil")
def test_copiere_copies_dir(shutil_mock):
    # Arrange
    dir_mock = Mock()
    dir_mock.is_dir.return_value = True
    dir_mock.parts = ['path', 'to', 'mydir']

    # Act
    copy_file_or_dir(dir_mock, "dest")

    # Assert
    assert len(shutil_mock.copytree.call_args_list) == 1
    assert len(shutil_mock.copy2.call_args_list) == 0
    copy_call_args = shutil_mock.copytree.call_args_list[0]

    assert copy_call_args == call(ANY, "dest/mydir")
