mfunc= int(input("What Application You Want To Run? \n(1)Calculater \n(2)Weight Converter \n : "))
if mfunc==1:
    func = int(input("Hey There what task do you want to run? \n"
      "(1) Subtraction\n"
      " (2) Addition\n"
      " (3) Division\n"
      " (4) Multipication "))
    if func==1:
        val=int(input('Enter Number: '))
        valtwo=int(input("Enter Second Number: "))
        answer= val-valtwo
        print(f"Answer is {answer}")
    if func==2:
        val=int(input('Enter Number: '))
        valtwo=int(input("Enter Second Number: "))
        answer= val+valtwo
        print(f"Answer is {answer}")
    if func==3:
        val=int(input('Enter Number: '))
        valtwo=int(input("Enter Second Number" ))
        answer= val/valtwo
        print(f"Answer is {answer}")
    if func==4:
        val=int(input('Enter Number: '))
        valtwo=int(input("Enter Second Number: "))
        answer= val*valtwo
        print(f"Answer is {answer}")

    print("Thanks for using!")

elif mfunc==2:
    kind=input("Select kind Of Weight To Convert. \n(L)bs \n(K)g: ")
    weight=int(input("How Much Weight Is It? \n(Add Only Integers):  "))
    if kind.upper() == ('L'):
        converted_weight = weight * 0.45
        print(f"Converted Weight Is {converted_weight} Kg")
    else:
        converted_weight = weight/0.45
        print(f"Converted Weight is {converted_weight} Lbs")
    print("Thanks For Using!")






