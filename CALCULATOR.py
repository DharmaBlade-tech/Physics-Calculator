calc=input("Is it multiplication, division, addition or subtraction ?").lower()
if calc=="multiplication":
    num1=float(input("Enter first number"))
    num2=float(input("Enter Second NUMBER"))
    ans1= num1*num2
    print(f"Your answer is {ans1}")
    opt=input("Would you like to do something else with your answer?")
    if opt=="yes":
        while True:
            calc2=input("Is it multiplication, division, addition or subtraction ?").lower()
            if calc2=="multiplication":
                num12=float(input("Enter the number"))
                ans2= num12*ans1
                print(f"Your answer is {ans2}")
                opt=input("Would you like to do something else with your answer?").lower()
            elif calc2=="addition":
                num12=float(input("Enter the number"))
                ans2=num12+ans1
                print(f"Your answer is {ans2}")
                opt=input("Would you like to do something else with your answer?").lower()
            elif calc2=="division":
                num12=input("Do you want to divide your answer by the new number ?").lower()
                if num12=="yes":
                    num12=float(input("Enter the number."))
                    ans2=ans1/num12
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?").lower()
                else:
                    ans2=num12/ans1
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?")
            elif calc2=="subtraction":
                num12=input("Do you want to subtract your answer by the new number ?").lower()
                if num12=="yes":
                    num12=float(input("Enter the number."))
                    ans2=ans1-num12
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?")
                else:
                    ans2= num12-ans1
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?").lower()
        else:
            calc=input("Is it multiplication, division, addition or subtraction ?").lower()
    
elif calc=="addition":
    num1=float(input("Enter first number"))
    num2=float(input("Enter Second NUMBER"))
    ans1= num1+num2
    print(f"Your answer is {ans1}")
    opt=input("Would you like to do something else with your answer?").lower()
    if opt=="yes":
        while True:
            calc2=input("Is it multiplication, division, addition or subtraction ?").lower()
            if calc2=="multiplication":
                num12=float(input("Enter the number"))
                ans2= num12*ans1
                print(f"Your answer is {ans2}")
                opt=input("Would you like to do something else with your answer?").lower()
            elif calc2=="addition":
                num12=float(input("Enter the number"))
                ans2=num12+ans1
                print(f"Your answer is {ans2}")
                opt=input("Would you like to do something else with your answer?").lower()
            elif calc2=="division":
                num12=input("Do you want to divide your answer by the new number ?").lower()
                if num12=="yes":
                    num12=float(input("Enter the number."))
                    ans2=ans1/num12
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?").lower()
                else:
                    num12=float(input("Enter the number."))
                    ans2=num12/ans1
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?")
            elif calc2=="subtraction":
                num12=input("Do you want to subtract your answer by the new number ?").lower()
                if num12=="yes":
                    num12=float(input("Enter the number."))
                    ans2=ans1-num12
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?")
                else:
                    num12=float(input("Enter the number."))
                    ans2= num12-ans1
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?").lower()
        else:
            exit()
elif calc=="division":
    num1=float(input("Enter first number"))
    num2=float(input("Enter Second NUMBER"))
    ans1= num1/num2
    print(f"Your answer is {ans1}")
    opt=input("Would you like to do something else with your answer?").lower()
    if opt=="yes":
        while True:
            calc2=input("Is it multiplication, division, addition or subtraction ?").lower()
            if calc2=="multiplication":
                num12=float(input("Enter the number"))
                ans2= num12*ans1
                print(f"Your answer is {ans2}")
                opt=input("Would you like to do something else with your answer?").lower()
            elif calc2=="addition":
                num12=float(input("Enter the number"))
                ans2=num12+ans1
                print(f"Your answer is {ans2}")
                opt=input("Would you like to do something else with your answer?").lower()
            elif calc2=="division":
                num12=input("Do you want to divide your answer by the new number ?").lower()
                if num12=="yes":
                    num12=float(input("Enter the number."))
                    ans2=ans1/num12
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?").lower()
                else:
                    num12=float(input("Enter the number."))
                    ans2=num12/ans1
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?")
            elif calc2=="subtraction":
                num12=input("Do you want to subtract your answer by the new number ?").lower()
                if num12=="yes":
                    num12=float(input("Enter the number."))
                    ans2=ans1-num12
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?")
                else:
                    num12=float(input("Enter the number."))
                    ans2= num12-ans1
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?").lower()
        else:
            exit()
elif calc=="subtraction":
    num1=float(input("Enter first number"))
    num2=float(input("Enter Second NUMBER"))
    ans1= num1-num2
    print(f"Your answer is {ans1}")
    opt=input("Would you like to do something else with your answer?").lower()
    if opt=="yes":
        while True:
            calc2=input("Is it multiplication, division, addition or subtraction ?").lower()
            if calc2=="multiplication":
                num12=float(input("Enter the number"))
                ans2= num12*ans1
                print(f"Your answer is {ans2}")
                opt=input("Would you like to do something else with your answer?").lower()
            elif calc2=="addition":
                num12=float(input("Enter the number"))
                ans2=num12+ans1
                print(f"Your answer is {ans2}")
                opt=input("Would you like to do something else with your answer?").lower()
            elif calc2=="division":
                num12=input("Do you want to divide your answer by the new number ?").lower()
                if num12=="yes":
                    num12=float(input("Enter the number."))
                    ans2=ans1/num12
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?").lower()
                else:
                    num12=float(input("Enter the number."))
                    ans2=num12/ans1
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?")
            elif calc2=="subtraction":
                num12=input("Do you want to subtract your answer by the new number ?").lower()
                if num12=="yes":
                    num12=float(input("Enter the number."))
                    ans2=ans1-num12
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?")
                else:
                    num12=float(input("Enter the number."))
                    ans2= num12-ans1
                    print(f"Your answer is {ans2}")
                    opt=input("Would you like to do something else with your answer?").lower()
        else:
            exit()
else:
    calc=input("New Calculation. Is it multiplication, division, addition or subtraction ?").lower()


    
           


    



