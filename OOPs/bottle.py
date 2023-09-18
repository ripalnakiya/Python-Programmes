def main():
    b = Bottle()
    print(b.getQuantity(), b.getCapacity()) # 0ml , 1000ml
    b.fill(700)
    print(b.getQuantity(), b.getCapacity()) # 700ml , 1000ml
    b.pour(300)
    print(b.getQuantity(), b.getCapacity()) # 400ml , 1000ml


class Bottle():
    def __init__(self):
        self.quantity = 0
        self.capacity = 1000

    def fill(self,num):
        self.quantity += num

    def pour(self,num):
        self.quantity -= num

    def getQuantity(self):
        return self.quantity
    
    def getCapacity(self):
        return self.capacity


if __name__ == "__main__":
    main()
