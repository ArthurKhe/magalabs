

def f(n):
    if n <=1:
        return n
    elif n % 2 == 0:
        return n // 2
    else:
        return f(n//2) + f(n//2 + 1)


print(f(int(input("Input n: "))))