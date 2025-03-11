from shit_hash import *


def test_shit_hash_string():
    assert shit_hash("foo") == 42


def test_shit_hash_int():
    a = 1
    assert shit_hash(a) == 42


def test_shit_hash_func():
    def foo():
        pass
    assert shit_hash(foo) == 42


def test_shit_hash_optional():
    assert shit_hash() == 42  # shit hash works even if you don't tell it what you're hashing


def test_shit_hash_bytes():
    assert shit_hash_bytes(b"foo") == 42
    assert shit_hash_bytes(b"\x01") == 42


def test_shit_hash_bytes_func():
    def foo():
        pass
    assert shit_hash_bytes(foo) == 42


def test_shit_hash_bytes_optional():
    assert shit_hash_bytes() == 42
