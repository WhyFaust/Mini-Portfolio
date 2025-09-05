import pytest
from Python.web.DataCAndP.db_scripts import get_quises, get_question_after

def test_get_quises():
    result = get_quises()
    assert isinstance(result, list)

def test_get_question_after():
    result = get_question_after(0, 1)
    assert result is None or isinstance(result, tuple)