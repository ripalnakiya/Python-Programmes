import stack as st

def main():
    text = input("String: ")

    s = st.Stack()

    for ch in text:
        s.push(ch)

    rtext = []

    while not s.isEmpty():
        rtext.append(s.pop())

    #Joins the list elements to a string and eventually creates a string of elements
    rev = "".join(rtext)

    print(rev)

main()

