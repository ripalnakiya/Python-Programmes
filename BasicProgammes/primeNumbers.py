def main():
    n = int(input("Enter the number: "))
    count = count_prime(1,n-1)
    print(f"count = {count}")


# Finds number of divisors
def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n%i == 0:
            count += 1    
    return count


# Checks if the given number is prime
def is_prime(n):
    return count_divisors(n) == 2   # This is relationsal operator '==' So by default it 
                                    # returns True or False
    # if count_divisors(n) == 2:
    #     return True
    # else:
    #     return False


# Finds the prime number in a range of two numbers (a,b)
def count_prime(a,b):
    count = 0
    for i in range(a, b+1):
        if is_prime(i): #If the number is prime , count++
            count += 1
    return count


main()