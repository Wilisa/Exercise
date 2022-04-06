stack =[]
begin = -1

def push(a: str):
    global begin
    begin += 1
    stack[begin] = a

def pop():
    global begin
    a = stack[begin]
    begin -= 1
    return a

def isapalindrome(word: str) -> bool:
    global stack
    width = len(word)
    stack = [0] * (width + 1)
    mid = width // 2
    i = 0
    while i < mid:
        push(word[i])
        i += 1
    if width % 2 != 0:
        i += 1
    while i < width:
        a = pop()
        if a != word[i]:
            return False
        i += 1
    return True


word = input("Enter a palindrome word: ")
isapalindrome(word)
if isapalindrome(word):
    print("This is a palindrome")
else:
    print("This is not a palindrome")
