from person import User
def main():
    print("Hello,world!")
    name = input("what is your name?")
    person = User(name)
    person.greet()

if __name__ == "__main__":
    main()