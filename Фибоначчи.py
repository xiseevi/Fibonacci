# Fibonacci v0.5
# Made by Mahmduov A.V., group 4305, SPB GTI(TU).
print('Фибоаччи v0.5')

def isfib():
# def кастомная функция
# number - переменная которую мы вводим.
    while True:
    # While - это цикл. Выполняет тело цикла до тех пор пока условия цикла истина. в данном случае цикл проверки на фибоначи до тех пока не будет введен любой не численный символ.
        try:
            number = int(input("Введите число (или не число для выхода): "))
        except ValueError:
            print("Выход")
            break
        # break - оператор который досрочно прерывает цикл.

        num1 = 1
        num2 = 1
        while num2 <= number:
            if num2 == number:
                print('Фибоначчи')
                break
            else:
                tempnum = num2
                num2 += num1
                num1 = tempnum
        else:
            print('Не Фибоначчи')
        # Идет проверка на число фибонначи до тех пока оно не будет определенно как число фибонначи или нет.
isfib()
