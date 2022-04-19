import os.path

import pytest
#dev
"""Tests if there is a log file"""
def test_log_file():
    assert os.path.exists("./app/logs/info.log")