
for curVal in range(1,101):
    if(curVal % 15 == 0):
        print("FizzBuzz")
    elif(curVal % 5 ==0):
        print("Buzz")
    elif(curVal%3 == 0):
        print("Fizz")
    else:
        print(curVal)