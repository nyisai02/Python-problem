from numb3rs import validate
def main():
    test_num()
    test_ali()
def test_num():
    assert  validate(r"127.0.0.1")==True
    assert  validate(r"1.2.3")==False
    assert validate(r"1.2.3.1000")==False
    assert validate(r"255.255.255.255")==True
    assert validate(r"512.512.512.512")==False
    assert validate(r"255.3000.255")==False
    assert validate(r"1")==False
    
def test_ali():
    assert validate(r"cat")==False

if __name__ =="__main__":
    main()