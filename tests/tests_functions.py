import pytest
import hype.hype as hh

def test_square():
    assert hh.square(2) == 4, 'square no work'
    assert hh.square(-2) == 4, 'neg should result pos'

def test_sum():
    assert hh.square(4, 4) == 8, 'sum no work'

def test_root():
    assert hh.squareroot(4) == 2, 'root no work'
    assert hh.squareroot(-4) == 'UNDEFINED', 'negative root no define'

def test_hype():
    assert hh.hypotenuse(3, 4) == 5, 'hype no work'