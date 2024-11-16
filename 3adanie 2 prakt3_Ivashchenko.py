n = int(input("Введите число: "))
if n < 1 or n > 999:
    print ("Число должно быть в рамках 1-999")
if n % 2 == 0:
    chetnost = "четное"
else:
    chetnost = "нечетное"
if n < 10:
    kolichestvo_cifr = "однозначное"
elif n < 100:
    kolichestvo_cifr = "двузначное"
else:
    kolichestvo_cifr = "трехзначное"
    print (f"{n} {chetnost} {kolichestvo_cifr} число")
