import pytest
from src import app

def test_add_positive_case1():
    assert app.add(2, 3) == 5

def test_add_positive_case2():
    assert app.add(-1, 1) == 0

def test_is_palindrome_positive():
    # deux exemples positifs possibles
    assert app.is_palindrome("radar") is True
    assert app.is_palindrome("A man, a plan, a canal: Panama") is True

def test_is_palindrome_negative():
    assert app.is_palindrome("hello") is False