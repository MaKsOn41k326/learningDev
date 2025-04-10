def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Testing calculator functions:")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 1 = {subtract(5, 1)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    try:
        print(f"8 / 2 = {divide(8, 2)}")
        print(f"5 / 0 = {divide(5, 0)}")
    except ValueError as e:
        print(f"Error: {e}")

