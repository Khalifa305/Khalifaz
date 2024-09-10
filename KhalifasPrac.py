
def adds(number1,number2):
    Addz = number1 + number2
    return Addz

def subs(number1,number2):
    Subz = number1 - number2
    return Subz

def Mults(number1,number2):
    Multz = number1 * number2
    return Multz

def Divs(number1,number2):
    Divz = number1 / number2
    return Divz

def Expo(number1,number2):
    Exp = number1 ** number2
    return Exp

def Mods(number1,number2):
    Modz = number1 % number2
    return Modz
    


def main():
    number1 = int(input("Write you first number here: "))
    number2 = int(input("Write your second number here: "))

    result1 = adds(number1,number2)
    print("The Addition of the numbers you've entered is:",result1)

    result2 = subs(number1,number2)
    print("The Subtraction of the numbers you've entered is:",result2)

    result3 = Mults(number1,number2)
    print("The multiplication of the numbers you've entered is:",result3)

    result4 = Divs(number1,number2)
    print("The Division of the numbers you've entered is:",result4)
    result5 = Expo(number1,number2)
    print("The Power of your first number to your second number is:",result5)

    result6 = Mods(number1,number2)
    print("The Mod of the numbers you've entered is:",result6)

main()
