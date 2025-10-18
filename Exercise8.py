a = int(input("Enter start (a): "))
b = int(input("Enter end (b): "))

evens = []
odds = []
primes = []

for num in range(a, b + 1):
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)

print("Even numbers:", evens)
print("Odd numbers:", odds)
print("Prime numbers:", primes)
print(f"Counts: Even={len(evens)}, Odd={len(odds)}, Prime={len(primes)}")
