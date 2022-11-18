print("The formula is: X(k+1) = a * Xk + c mod m")
seed_num = int(input("Enter seed number: "))
multiplier = int(input("Enter the multiplier(a): "))
increment = int(input("Enter the increment(c): "))
modulus = int(input("Enter the modulus (m): "))
n = int(input("How many random numbers would you like to generate?\nInput: "))


def lcg():
    num_base = seed_num
    for i in range(n):
        rd = (multiplier * num_base + increment) % modulus
        print(rd)
        num_base = rd


lcg()