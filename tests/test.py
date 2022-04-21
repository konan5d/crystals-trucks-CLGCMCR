def addition(a, b):
    return a + b


def test_addition_true():
    assert addition(1, 2) == 3


def test_addition_false():
    assert addition(1, 2) == 4
