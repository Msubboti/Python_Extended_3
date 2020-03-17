def hz(max):
    import random
    random.seed()
    z=random.randint(1, max)
    return z
def deal(n):
    if n==1:
        print("Да")
    elif n==2:
        print("Духи говорят да")
    elif n==3:
        print("Безусловно")
    elif n==4:
        print("Без сомнений")
    elif n == 5:
        print("Абсолютно точно")
    elif n==6:
        print("Очень вероятно")
    elif n==7:
        print("Похоже что да")
    elif n==8:
        print("Мне кажется да")
    elif n==9:
        print("Должно быть так")
    elif n==10:
        print("Ответ не ясен")
    elif n==11:
        print("Спросите позже")
    elif n==12:
        print("Не могу сказать")
    elif n==13:
        print("Спросите снова")
    elif n==14:
        print("Нет")
    elif n==15:
        print("Вряд ли")
    elif n==16:
        print("Ответ нет")
    elif n==17:
        print("Звезды говорят нет")
    elif n==18:
        print("Не надейтесь")
    elif n==19:
        print("Не похоже")
    else:
        print("Мало шансов")
t=True
while t:
    print("Нужен ответ на вопрос? \n 1) Да \n 2) Нет")
    b=int(input())
    t2=False
    while not t2:
        if b==1:
            n=hz(20)
            print("Вот:")
            deal(n)
            t2=True
        elif b==2:
            t2=True
            t=False
        else:
            print("Зая, нужно ввести циферку, попробуй ещё раз")
            t2=True