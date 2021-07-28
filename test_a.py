import a
import pytest


def test_f():
    assert a.f(1, 2) == 3
    assert a.f("1", "2") == "12"
    with pytest.raises(TypeError):
        a.f("1", 2)
