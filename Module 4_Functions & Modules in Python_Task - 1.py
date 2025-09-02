def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
n = int(input('Enter a number: '))
results = factorial(n)
if n<0:
    print('Enter a whole number')
elif n<=1:
    print('The factorial of ' + str(n) + ' is: 1')
else:
    print('The factorial of ' + str(n) + ' is: ' + str(results))
