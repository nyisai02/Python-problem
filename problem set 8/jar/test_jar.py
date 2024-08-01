from jar import Jar
def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()
def test_init():
    jar=Jar()
    assert jar.capacity=12
    jar =Jar(10)
    assert jar.capacity=10


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar=Jar()
    jar.deposit(5)
    assert jar._size==5
    jar.deposit(2)
    assert jar._size==7



def test_withdraw():
    jar=Jar()
    jar.deposit(12)
    jar.withdraw(6)
    assert jar._size==6
    jar.withdraw(2)
    assert jar._size==4