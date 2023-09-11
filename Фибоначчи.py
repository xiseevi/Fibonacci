# Fibonacci v0.1
# Made by Mahmduov A.V., group 4305, SPB GTI(TU).
print('Фибоаччи v0.1')

print('Введите любое число')
def isfib(number):
    num1 = 1
    num2 = 1
    while True:
        if num2 <= number:
            if num2 == number:
                return 'Фибоначчи'
            else:
                tempnum = num2
                num2 += num1
                num1 = tempnum
                
        else:
            return 'Не Фибоначчи'
                
print(isfib(int(input())))
g = int(input('<=== To be continued...'))
