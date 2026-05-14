import pytest
from rag.chunker import clean_text

def test_clean_text_newlines():
    text = "hello\n\nworld\tthis  is   test"
    result = clean_text(text)
    assert result == "hello world this is test"

def test_clean_text_strip():
    text = "   hello world   "
    result = clean_text(text)
    assert result == "hello world"

def test_clean_text_empty():
    text = ""
    result = clean_text(text)
    assert result == ""