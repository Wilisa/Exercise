fullname = input("Enter Full Name: ")


def initials(fullname):
    for i in range(1, len(fullname) - 1):
        if fullname[i] == " ":
            print(fullname[0].upper(), end=".")
            print(fullname[i + 1].upper(), end=".")


def main():
    name = fullname
    initials(name)


main()
