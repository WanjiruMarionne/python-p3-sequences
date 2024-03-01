#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print("[]")
        return
    
    fibonacci_sequence = [0, 1]  
    
    if length == 1:
        print("[0]")
    elif length == 2:
        print("[0, 1]")
    else:
        sequence = [0, 1]
        for _ in range(2, length):
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)
            sequence.append(next_number)
        print(sequence)
