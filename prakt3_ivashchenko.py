def proverka_chetnosti(a, b):
    return a % 2 == b % 2
A = int(input("Число A =  "))
B = int(input("Число B =  "))
if proverka_chetnosti(A, B):
    print("A и B c одинаковой чётностью")
else:
    print("A и B не имеют общую чётность")
