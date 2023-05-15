def main():
    print(f"5 squared is {square(5)}")
    print(f"-3 squared is {square(-3)}")
    print(f"2 squared is {square(2)}")


def square(n):
    return n**2


# Now the main function is called only when the square.py has to be exected.
if __name__ == "__main__":
    main()
# if the python file is directly executed then if condition will be true
# if the python file is imported then the file will get executed but if condition will be false