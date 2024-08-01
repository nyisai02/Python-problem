import pytest
from fule import convert, gauge

def main():
    test_fule_convert()
    test_fule_gauge()

def test_fule_convert():
    assert convert("1/2")==50
    assert convert("1/4")==25
    assert convert("5/6")==83
    assert convert("0/5")==0
    assert convert("1/100")==1
    assert convert("99/100")==99
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("1 / 0")
def test_fule_gauge():
    assert gauge(50)=="50%"
    assert gauge(25)=="25%"
    assert gauge(83)=="83%"
    assert gauge(0)=="E"
    assert gauge(1)=="E"
    assert gauge(99)=="F"

if __name__ == "__main__":
    main()
