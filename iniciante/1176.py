
t = int(input())

def fib(numero):
    a = 0
    b = 1
    for i in range(numero):
        temp = a
        a = b 
        b = temp + b
    return a

for i in range(t):
    valor = int(input())
    res = fib(valor)
    print(f"Fib({valor}) = {res}")

