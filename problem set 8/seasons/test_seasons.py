from seasons import get_bd
import pytest
def main():
    test_dateofbirth()
    invaid()

def test_dateofbirth():
    assert get_bd("1999-01-01") == ("01", "01", "1999")
    assert get_bd("2022-01-01") == ("01", "01", "2022")
    assert get_bd("2024-05-01")==("05","01","2024")
def invaid():
    with pytest.raises(SystemExit):
        get_bd("January 1, 1999 ")
if __name__ == "__main__":
    main()