prime = []
n = 1000000000000

num = 1
# Negative numbers, 0 and 1 are not primes
for i in range(1000000):
    if num > 1:
    
        # Iterate from 2 to n // 2
        for i in range(2, (num//2)+1):
        
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                num += 1
                break
        else:
            num += 1
            prime.append(num)
    else:
        num += 1

print(str(len(prime)))
