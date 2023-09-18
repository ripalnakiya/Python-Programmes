<<<<<<< HEAD
def main():
    c = Collector()
    c.add(10)
    c.add(20)
    c.add(30)
    print(c.get()) # 60


class Collector:
    def __init__(self):
        self.num = 0

    def add(self,a):
        self.num += a

    def get(self):
        return self.num
    

if __name__ == "__main__":
=======
def main():
    c = Collector()
    c.add(10)
    c.add(20)
    c.add(30)
    print(c.get()) # 60


class Collector:
    def __init__(self):
        self.num = 0

    def add(self,a):
        self.num += a

    def get(self):
        return self.num
    

if __name__ == "__main__":
>>>>>>> 69a79bbc7ebf13241089edb722e487619ff6f61f
    main()