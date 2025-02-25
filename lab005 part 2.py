
def decimal_to_binary(n):
    if n == 0: return 0
    if n == 1: return 1
    next,digit = divmod(n,2)
    return str(decimal_to_binary(next)) + str(digit)

# Test cases
print(decimal_to_binary(10))   # "1010"
print(decimal_to_binary(255))  # "11111111"
print(decimal_to_binary(1))    # "1"

for i in range(255 + 1):
    print(decimal_to_binary(i), i)