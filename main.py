# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

#function that takes in two arguments
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

#function that takes text
def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        print(i)
        if next in "([{":
           
            opening_brackets_stack.append(Bracket(next, i + 1))
            pass

        if next in ")]}":
            
            if not opening_brackets_stack or not are_matching(opening_brackets_stack.pop().char,next):
                return i+1
    if opening_brackets_stack:
            return opening_brackets_stack[0].position
    return "Success"

def main():
    text = input()
    print(text)
    if text[0] == "I":
        text
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
