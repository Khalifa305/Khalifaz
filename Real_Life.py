
USD_to_EUR_rate = 0.90 #Global Variable

def convert(answer,USD_to_EUR_rate):
    Sol = float(answer) * USD_to_EUR_rate
    return Sol


def main():
    answer = float(input("Enter the amount of dollars you want to convert:" ))
    result = convert(answer,USD_to_EUR_rate)
    print(result, "Euros")

print("Welcome to the USD to EUR currency converter!")
main()


MARS_YEAR = 1.88
JUPITER_YEAR = 11.86

def MARS_age(age):
    return int(age / MARS_YEAR)

def Jupiter_age(age):
    return int(age / JUPITER_YEAR)

def main():
    age = int(input("Please enter your age:" ))
    mars_result = MARS_age(age)
    jupiter_result = Jupiter_age(age)
    print("Your age in Mars would be:", mars_result)
    print("Your age in Jupiter would be:", jupiter_result)

main()


Square_feet_to_square_meters = 10.764 #Global variable

def equation(length,width):
    total = length * width
    return total



def main():
    length = float(input("Provide us with the length of the room:"))
    width = float(input("Provide us with the width of the room: "))
    result1 = equation(length,width) 
    result2 = equation(length,width) / Square_feet_to_square_meters #We did not float this statement since there is already a division sign "/", which would automatically float.
    print("The area of your room in square feet would be:",result1,"ft^2.")
    print("The area of your room in square meters would be:",result2,"m^2.") 


print("NOTE: Make sure that you apply your information in foot measurement!")
main()


