while"True":
    what = input("Выберите что будем делать:+,-,*,%:")
    a = int(input("Выберите первое число: "))
    b = int(input("Выберите второе число: "))
    if what == "+":
        c = a + b
        print("В результате:"+str(c))

    if what == "-":
        c = a - b
        print("В результате:" + str(c))

    if what == "*":
        c = a * b
        print("В результате:" + str(c))

    if what == "%":
        c = a % b
        print("В результате:" + str(c))
