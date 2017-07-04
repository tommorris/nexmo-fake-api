from .utils import ErrorCollection
import pytest

def test_error_collection_empty():
    e = ErrorCollection()
    out = e.format()
    assert out['message-count'] == 0

def test_error_collection_item():
    e = ErrorCollection()
    e.append({"status": "2", "error-text": "Missing username"})
    out = e.format()
    assert out['messages'][0]['status'] == '2'
    assert out['message-count'] == 1

def test_error_collection_check():
    e = ErrorCollection()
    with pytest.raises(TypeError):
        e.append(True)
