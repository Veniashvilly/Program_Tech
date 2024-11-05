def f(x,y):
    return x + y
def test1():
    assert f(1, 4) == 5
def test2():
    assert f(-10, 3) == -7
def test3():
    assert f(5, 5) == 0