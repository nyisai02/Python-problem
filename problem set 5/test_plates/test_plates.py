from plates import is_valid

def main():
    test_plates1_valid()
    test_plates2_valid()
    test_plates3_valid()
    test_plates4_valid()

def test_plates1_valid():
    assert is_valid("HH")==True
    assert is_valid("ABCDEF")==True
    assert is_valid("H")==False
    assert is_valid("Hello,World")==False

def test_plates2_valid():
    assert is_valid("AA")==True
    assert is_valid("2A")==False
    assert is_valid("22")==False

def test_plates3_valid():
    assert is_valid("CS50")==True
    assert is_valid("CS05")==False
def test_plates4_valid():
    assert is_valid("AAA222")==True
    assert is_valid("AAAAAA")==True
    assert is_valid("AAA22A")==False
    assert is_valid("AD./32")==False


if __name__ == "__main__":
    main()
