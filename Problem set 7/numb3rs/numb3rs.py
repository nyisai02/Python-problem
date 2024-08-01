import re
def main():
    print(validate(input("IPv4 Address: ")))
def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",ip):
        numbers = ip.split(".")

        try:
            for num in numbers:
                if not int(num) in range(0, 256):
                    return False
        except ValueError:
            return False
        return True
    else:
        return False
if __name__ == "__main__":

    main()