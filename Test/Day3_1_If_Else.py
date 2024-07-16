print("Welcome to the rollercoster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("you can ride the rollercoster!")
elif height < 80:
    print("Sorry, you have to grow taller before you can ride")
else:
    print("Haha")