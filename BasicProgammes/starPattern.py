'''

"3 4"

* * * *
*     *
* * * *

'''

def main():
    r, c = input("Enter two numbers: ").split()
    r, c = int(r), int(c)
    pattern(r, c)


def pattern(r, c):
    for i in range(1, r+1):
        if i == 1 or i == r:
            print("*" * r)
        else:
            print(f"* {" " * (w-2)}**")


# def pattern(r, c):
#     for i in range(0,r):
#         for j in range(0,c):
#             if i == 0 or i == r:
#                 print("* ", end = " ")
#             elif j == 0 or j == c:
#                 print("* ", end = " ")
#             else:
#                 print("  ", end = " ")
#         print()

if __name__ == "__main__":
    main()
