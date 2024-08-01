from um import count
def main():
    count_um_upper()
    count_um_0()
    count_um_lower()

def count_um_upper():
    assert count("Um.....")==1
    assert count("Um, thanks, um...")==2
    assert count("Um, thanks for the album")==1
def count_um_0():
    assert count("yum")==0
    assert count("yummy")==0

def count_um_lower():
    assert count("um1")==1
    assert count("um?")==1
    assert count("hello, um, world ")== 1
    assert count("um, hello, um, world ")== 2

if __name__ == "__main__":
    main()