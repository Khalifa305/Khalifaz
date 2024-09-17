def asser(number):
    assert number > 0, 'Number should be positive!'
    print("That's great, your number",number,"is positive!")

def names(name):
    assert name== "khalifa" , 'Sorry, your not the owner of the account'
    print("Welcome Khalifa to our website!")

def main():
    number = float(input("Enter your number:" ))
    asser(number)
    name = input("Let's know who you are before entering:")
    names(name)

main()