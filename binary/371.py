def getSum(a: int, b: int) -> int:
    MAX = 0x7FFFFFFF  # Maximum positive int (32-bit)
    MASK = 0xFFFFFFFF  # Mask to get last 32 bits
    
    
    while b != 0:
        tmp = (a & b) << 1  # carry calculation
        print(bin(tmp))
        a = (a ^ b) & MASK  # sum without carry (limit to 32 bits)
        b = tmp & MASK  # carry shifted left (limit to 32 bits)
    
    # If a is greater than MAX, it's a negative number in 32-bit representation

    print(bin(a))
    return a if a <= MAX else ~(a ^ MASK)


print(5 ^ 7)
print(getSum(39, 59))