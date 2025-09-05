import pytest
from Python.web.SDB.A3 import get_question_after

def test_get_question_after_empty():
    result = get_question_after(0, 1)
    assert result is None or isinstance(result, tuple)