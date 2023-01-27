number1=0
number2=0
count=0
do=0
number1=input( "Введите первое число:")
while (count<1):
    count=input( "Введите кол-во действий:")
    count=int(count)
    if count<1:print("Больше нуля, плиз")
for i in range(0,count):
    do=input("Выберете действие: +,-,/,*\nИли любое другое, для выхода из программы:")
    match do.split():
        case["+"]:
            number2=input(f"Введите второе число, {number1}+")
            number1=float(number1)+float(number2)
        case["-"]:
            number2=input(f"Введите второе число, {number1}-")
            number1=float(number1)-float(number2)
        case["/"]:
    
            number2=0
            while (int(number2)==0):
                number2=input(f"Введите второе число, {number1}/")
                if number2=="0":    
                     print("Не 0, плиз")
            number1=float(number1)/float(number2)
        case["*"]:
            number2=input(f"Введите второе число, {number1}*")
            number1=float(number1)*float(number2)
        case _:
            break
print(f"Ответ={number1}")
