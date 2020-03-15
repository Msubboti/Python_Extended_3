import math

aa = int(input('Enter the sum: '))


#крупные купюры

a = aa
val = [1000, 500, 200, 100, 50, 20, 10, 1]

while a > 0:
    for i in val:
        if a >= i:
            k = int(a/i)
            a = a - i*k
            print("Denomination: "+str(i)+', number of banknotes: '+str(int(k)))

########################################
print()

#мелкие купюры

a = aa
val =   [1000,  500,    200,    100,    50, 20, 10, 1]      #доступные номиналы
quant = [0,     0,      0,      0,      10, 10, 10, 10]     #количество номиналов (высоких номиналов беск. мн-во)


m_num = 0                                                   #максимальная сумма из мелких номиналов
i = 0
while i < len(val):
    m_num += val[i]*quant[i]
    i +=1


i = -1                                                      #последний индекс
while quant[i] != 0:                                        #ищем индекс для мелких по индексу кол-ва
        i -= 1
kk = val[i]                                                 #мелкие купюры

if a > m_num:
    k = math.ceil((a - m_num)/kk)                           #вывод старших купюр (достаточно и соток)
    #print(k)
    a -= k*kk
    print("Denomination: "+str(kk)+', number of banknotes: '+str(int(k)))

while a > 0:
    b = 0                                                   #сумма мелкими купюрами
    i = -1
    j = 0
    while a > b:
        for j in range(quant[i]):                           #количество купюр
            b += val[i]                                     #накапливаем мелкие купюры

            if b >= a:
                break
        i -= 1
    kk = val[i+1]
    k = j + 1
    #print("Denomination: " + str(kk) + ', number of banknotes: ' + str(int(k)))
    a -= k*kk
    print("Denomination: " + str(kk) + ', number of banknotes: ' + str(int(k)))


