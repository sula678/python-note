def lambda_demo(n):
    return lambda x: x ** n + x * 2 + 1
 
i = 1
f = lambda_demo(2)
while i <= 10:
    print(f(i))
    i += 1
