N = int(input("Введите ЦЕЛОЕ число N (> 1): "))
K = 0
while 3**K <= N:
    K += 1
print(K)