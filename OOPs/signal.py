import time
import os

def main():
    s = Signal()
    while True:
        os.system("cls")

        print(s.get())  # red
        time.sleep(4)
        s.next()

        print(s.get())  # green
        time.sleep(8)
        s.next()

        print(s.get())  # yellow
        time.sleep(2)
        s.next()

class Signal:
    def __init__(self):
        self.value = 0

    def get(self):
        colors = ("red", "green", "yellow")
        return colors[self.value%3]

    def next(self):
        self.value += 1

if __name__ == "__main__":
    main()