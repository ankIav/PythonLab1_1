# Check variable on right input. urVariable str format contains name of variable from main
# проверка на корректный ввод. urVariable хранит название переменной, передданной из основного кода, в формате строки
def isValueRight(urVariable):
    # while cycle needed to infinity input, while checkVariable isn't become a correct
    # цикл while нужен для бесконечного ввода, пока checkVariable не станет корректным
    while True:
        try:
            checkVariable = float(input('enter a value of %s ' % urVariable))
            break
            # if input was correct and except doesnt worked than exit while cycle
            # если ввод был корректный и except не сработал, тогда выход из цикла while
        except ValueError:
            print("You entered a wrong value of %s, try again" % urVariable)
    return checkVariable


# Variables transport the names of variables in str format to def "isValueRight" and take right value "checkVariable"
# Переменные передают названия самих переменных в формате строки в функцию 'isValueRight'
# и получают значения правильного ввода из "checkVariable"
a = isValueRight('a')
b = isValueRight('b')
c = isValueRight('c')
d = isValueRight('d')
k = isValueRight('k')


try:
    var1 = abs((a ** 2 / b ** 2 + c ** 2 * a ** 2) / (a + b + c * (k - a / b ** 3)))
except ZeroDivisionError:
    print("In var1 was division by zero")
else:
    print('var1 = %.3f' % var1)


try:
    var2 = abs(((a ** 2 - b ** 3 - c ** 3 * a ** 2) *
                (b - c + c * (k - d / b ** 3)) - (k / b - k / a) * c) ** 2 - 20000)
except ZeroDivisionError:
    print("In var2 was division by zero")
else:
    print('var2 = %.3f\n' % var2)
