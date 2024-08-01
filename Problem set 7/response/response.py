from validator_collection import validators
def main():
    email = input("Email: ")
    try:
        if validators.email(email):
            print("Valid")
        else:
            raise validator_collection.errors.InvalidEmailError
    except:
        print("Invalid")
if __name__ == "__main__":
    main()