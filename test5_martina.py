'''
2014314433
lee young suk
'''
x = input("Input a value for x : ") #Ask user input x value
y = input("Input a value for y : ") #Ask user input y value

while x.isdigit() !=True or y.isdigit() !=True:
    if x.isdigit() !=True and y.isdigit() !=True:
        print("ERROR; Both of them is non-numerical ")
        x = input("Input a value for x : ") #Ask user input x value
        y = input("Input a value for y : ") #Ask user input y value

    else:
        print("ERROR; Either of them is non-numerical ")
        x = input("Input a value for x : ") #Ask user input x value
        y = input("Input a value for y : ") #Ask user input y value



z=int(x)+int(y) #calculate z value by converting two strings above into int and adding them.
w=int(x)*int(y) #calculate w value by converting two strings above into int and adding them.
print(z) #print z
print(w) #print w
