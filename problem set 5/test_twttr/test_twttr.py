from twttr import shorten

def main():
    test_twttr()
def test_twttr():
    assert shorten("NYINYI")=="NYNY"
    assert shorten("nyinyi")=="nyny"
    assert shorten("NYInyi")=="NYny"
    assert shorten("666")=="666"
    assert shorten("Cs50")=="Cs50"
    assert shorten("Hello World")=="Hll Wrld"
    assert shorten("-.,/")=="-.,/"
    

if __name__ == "__main__":
    main()
