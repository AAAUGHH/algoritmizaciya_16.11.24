N = int(input("Введите целое число N (>0): "))
num = 1.0
for i in range(1, N+1):
    num *= (1.0 + i/10.0)
print(format(num, ".2f"))
