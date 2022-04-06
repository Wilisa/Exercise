def inList(number, lst):
    if search(number, lst):
        return number, "Is in the list"
    return number, "Is not in the list"


def search(number, lst):
    lst.sort()
    if len(lst) == 0:
        return
    else:
        if lst[1] > number:
            return number, "Is not in the list"
        elif lst[1] == number:
            return number, "Is in the list"
        else:
            return search(number, lst[1:])


def main():
    print(search(3, [3, 4, 5, 14, 15, 5, 2]))


main()
