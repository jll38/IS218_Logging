import os.path

import pytest

def test_log_file():
    assert os.path.exists("./logs/info.log")