def factors(value):
    new_val = value
    prime = 2
    divisors = []

    while new_val > 1:
        if new_val % prime == 0:
            divisors.append(prime)
            new_val = int(new_val / prime)
        else:
            prime+=1

    return divisors

print(factors(1257642))