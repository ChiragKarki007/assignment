mxn = int(input("Enter the max number: "))


fibonacci_sequence = [0, 1]


while True:
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]

    if next_number > mxn:
        break

    fibonacci_sequence.append(next_number)

print("Fibonacci sequence up to", mxn, ":", fibonacci_sequence)