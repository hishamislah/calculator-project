def multiply(a, b):
    return a * b
 
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
 
def main():
    print("Simple Calculator")
    print("Multiplication: 5 * 3 =", multiply(5, 3))
    print("Division: 10 / 2 =", divide(10, 2))
 
if __name__ == "__main__":
    main()