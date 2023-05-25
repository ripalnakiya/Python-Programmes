import stack

def main():
    expression = "(()))"
    print(isBalanced(expression))


def isBalanced(expression):
    brackets = {'(': ')', '[': ']', '{': '}',}
    stack = stack()

          

main()