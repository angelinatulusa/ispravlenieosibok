print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a=abs(int(input("Введите целое число => ")))#dobavit ese )
        break
    except ValueError:
         print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Нет смысла ничего делать с нулём")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    b=0 #dobavit peremennie b i c
    c=0
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
    #b=a
    #c=a
    c==b==a
    paaris=0
    paaritu=0
    while b>0:#вместо ; надо использовать :
        if b%2==0: #if надо правильно подставить под while и дописать еще одно =
            paaris+=1#nado pravolno podstavit pod if
        else: #else nado pravilno podstavit pod while
            b=b%10
            paaritu+=1#nado pravolno podstavit pod else
    
    print("Чётных цифр:",paaris)#posle teksta postavit ,
    print("Нечётных цифр:",paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число")
    print()
    b=0
    while a > 0:#posle while nado ispolzovat :
        number = a % 10
        a = a // 10
        b = b * 10
        b =+ number#pravilno podstavit pod while
    print("*Перевёрнутое* число", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз")#lisnaja (
    print()
    if c % 2 == 0:#dobavit ese odno =
        print("с - чётное число. Делим на 2.")
    else:
        print("с - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c != 1:
        if c % 2 == 0:#dobavit ese odno =
            c == c / 2
        else:
            c == (3*c + 1) / 2
            print(c, end=" ")#zakrit "
    print()
    print("Гипотеза верна")#ne te " bili ispolzovani
