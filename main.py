number = int(input("Enter a number: "))
factors = []
prime_fact = []
for i in range( number // 2, 1, -1):
    if (number % i == 0):
        factors.append(i)
        print(i)