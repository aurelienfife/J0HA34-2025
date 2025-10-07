# Four functions for each operation
# Illustrating function writing
def add(a, b):
    c = a + b
    return c

def subtract(a, b):
    c = a - b
    return c

def multiply(a, b):
    c = a * b
    return c

def divide(a, b):
    if b != 0:
        c = a / b
        return c
    else:
        return None

# Main program, insulated from global scope
def main():
    # Some demo code...
    n = add(5, 6)
    print(n)

    print(add(n, 15))

# If this is the top-level file running, run main
# (otherwise just load the functions for use in other modules)
if __name__ == "__main__":
    main()
