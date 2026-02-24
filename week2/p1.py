def solution():
    a, b = map(int, input().split())

    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} // {b} =  {a // b}")
    print(f"{a} % {b} = {a % b}")
    print(f"{a}/{b} = {a / b:.2f}")


if __name__ == "__main__":
    solution() 