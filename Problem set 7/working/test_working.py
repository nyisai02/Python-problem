from working import convert
import pytest
def main():
    test_1()
    test_2()
    test_3()
    test_4()

def test_1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") =="09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") =="09:00 to 17:30"

def test_2():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("9 PM to 5 AM") =="21:00 to 05:00"
    assert convert("8:00 PM to 4:00 AM") =="20:00 to 04:00"
    assert convert("10:30 PM to 8:50 AM")=="22:30 to 08:50"
    assert convert("10 PM to 8 AM")=="22:00 to 08:00"

def test_3():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_4():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM ")
        convert("09:00 AM - 17:00 PM ")

if __name__ == "__main__":
    main()