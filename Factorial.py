def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

if __name__ == '__main__':
    n = int(input("Enter a number : ").rstrip())
    result = fact(n)
    print(f'Factorial of {n} = {result}')