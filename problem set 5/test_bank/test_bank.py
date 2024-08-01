from bank import value

def main():
    test_bank1()
    test_bank2()
    test_bank3()

def test_bank1():
    assert value("Hello") == 0
    assert value("HELLO ") == 0
    assert value("hello G.. ") == 0
def test_bank2():
        assert value("Hi") == 20
        assert value("hey") == 20
        assert value("hay!") == 20
def test_bank3():
        assert value("Cs50 ")==100
        assert value("Good morning")==100
        assert value ("What's up")==100


if __name__ == "__main__":
    main()
