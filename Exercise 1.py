numbers = input("Enter numbers: ").split()
print()

n = len(numbers)

def AscendingOrNot(arr, n):
    if n == 1:
        return True
    return (arr[n - 1] >= arr[n - 2] and
        AscendingOrNot(arr, n - 1))

if AscendingOrNot(numbers, n):
    print("Ascending Order")
else:
    print("Not Ascending")