
n = int(input())
a, b = 0, 1
while True:
    if n == a:
        print("Pertence")
        break
    elif n < a:
        print("Nao Pertence")
        break
    a, b = b, a + b
10
