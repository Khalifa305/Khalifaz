def forward():
    count = 0
    while count <= 10:
        print(count)
        count = count+1

def backward():
    count = 10
    while count >= 0:
        print(count)
        count = count-1

def skip():
    count = 0
    while count < 10: #When skipping number, do not use equal sign because it will add 1 more number if used.
        count = count+1
        if count == 5:
         continue
        print(count)

def skip_reverse():
    count = 10+1 #Use + 1 to include 10 in the counting.
    while count > 0:
        count = count-1
        if count == 5:
            continue
        print(count)

def index():
    count = 0
    word = "Khalifa"
    while count < len(word):
        print(word[count])
        count = count+1

def index_2():
    count = 0
    word = "Pno"
    while count < len(word):
        print(word[count])
        count = count+1


def skip_2():
    count = 0
    while count < 20: #When skipping number, do not use equal sign because it will add 1 more number if used.
        count = count+1
        if count == 2:
            continue
        print(count)

def skip_reverse2():
    count = 10+1 # Using +1 to include number ten in counting down
    while count > 0:
        count = count-1
        if count == 2:
            continue
        print(count)


def index_reverse():
    count = 1 #When spelling the letters in reverse, you should start from 1 instead of zero!
    word = "Khalifa"
    while count <= len(word): 
        print(word[-count]) #and make your variable as negative so it considers it as -1
        count = count+1

def even_numbers():
    count = 0
    while True:
        count = count+1
        if count % 2 ==1:
            continue
        elif count > 20:
            break
        print(count)

def odd_numbers():
    count = 0
    while True:
        count = count+1
        if count % 2==0:
            continue
        elif count > 20:
            break
        print(count)

def ranges(start,stop):
    count = 0
    r = range(start,stop+1) #Using +1 in the stop would print out +1 on the last number you are stopping on, if +1 is not mentioned, python wont count the number you decided to stop on.
    result = len(r) #using this would let the interpreter print out the numbers on 1 line, using the ranges you gave.

    while count < result: #You cannot use equal sign here since it will make the interpreter know that the number went out of the range you wanted that why we mentioned +1 on stop
        print(r[count], end = " ")
        count = count+1

def out():
    while True:
        exi = input("Press \"X\" to exit:")
        if exi != "x":
            continue
        elif exi == "x":
            break

def over(start,stop):
    count = 1
    r1 = range(start,stop+1)
    results = len(r1)
    while count < results:
        if count == 99:
            continue
        print(r1[count], end = " ")
        count = count+1


def main():
    forward()
    print("Now Let's count backward.")
    backward()
    print("Let's count forward and skip 5!")
    skip()
    print("Let's count backwards without 5!")
    skip_reverse()
    print("Let's count forward without 2!")
    skip_2()
    print("Now, let's count backwards without 2!")
    skip_reverse2()
    print("Now, let's print even numbers!")
    even_numbers()
    print("Now, let's print Odd numbers!")
    odd_numbers()
    print("Now let's enter the range from 0 to 10")
    ranges(1,30)
    print("Let's print my name using len")
    index()
    print("Let's print another word using len")
    index_2()
    print("Let's print my name \"Khalifa\" in reverse")
    index_reverse()
    print("Another counting in range on 1 line.")
    over(50,100)
    out()

main()