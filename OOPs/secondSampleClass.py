def main():
    d = Door()  # Door object will be created in heap and its reference will be in d 
                # d = 0x115
    d.price = 2500
    d.set()     # Door.set(d)


class Door:                 # init function will be called by default
    def set (self):         # self will get reference of the object d
        self.name = "vimal"


if __name__ == "__main__":
    main()