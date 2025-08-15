from hello import toyoo, add, subtract

def test_add():
    assert add(1) == 2

def test_subtract():
    assert subtract(2) == 1

def test_toyoo():
    assert toyoo("Jana").startswith("hi ")
