from calculator import add,subtract,divide
def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(0,0)==0

def test_subtract():
    assert subtract(5,3)==2
    assert subtract(0,0)==0
    
def test_divide():
    assert divide(6,3)==2
    assert divide(5,2)==2.5
    
def test_divide_by_zero():
    try:
        divide(5,0)
    except ValueError as e:
        assert str(e)=="Cannot divide by zero"