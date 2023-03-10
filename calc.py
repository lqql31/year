a=1
a=float(input("Введите первое число: "))
b=1
b=float(input("Введите второе число: "))
number=1
number=float(input("Введите количество операций: "))
c=input("Введите операцию: \n + Сложение, \n - Вычитание, \n / Деление, \n * Умножение, \n ^ Возведение в степень \n")
r=0.0
if c=="+":
    r=a+b
if c=="-":
    r=a-b
elif c=="/" and b==0:
      print("Error")
if c=="/" and b!=0:
    r=a/b
if c=="*":
    r=a*b
if c=="&":
    r=a**b
i=1
while i<number:
   b=float(input("Введите второе число: "))
   c=input("Введите знак операции: ")
   if c=="+":
        r=r+b
        i+=1
   if c=="-":
        r=r-b
        i+=1
   if c=="/":
        if b==0:
            b=float(input("Error"))
            r=r/b
            i+=1
        elif b!=0:
            r=r/b
            i+=1 
   if c=="*":
        r=r*b
        i+=1
   if c=="&":
        r=r**b
        i+=1
print(r)




