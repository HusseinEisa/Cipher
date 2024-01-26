
#	Input:               ||          Input:
#	9 3                  ||          66 1252332576
#	                     ||
#	Output:              ||          Output:
#	3 ^ 2 = 9            ||          66 ^ 5 = 1252332576


C=1   

while (True) :
    T=True
    print("\n______________________________ Method number",C,"______________________________\n")
    C = C + 1
    Test = False

    Test2 = True

    Num1 = int(input("\nPlease Enter First Number : "))

    Num2 = int(input("\nPlease Enter second Number : "))


    count = 0


    if (Num1 == Num2) :
        print("\n",Num1,"^ 1 =",Num2,"\n")
        continue

    elif (Num1 == 0 or Num2 == 0 or Num1 == 1 or Num2 == 1) :
        print("\nNot Found\n")
        continue

    elif (Num2 > Num1) :
        Num1 , Num2 = Num2 , Num1

    Save = Num1

    while (Num1 % Num2 == 0) :
        T=False
        if ((Num1 / Num2) % Num2 == 0 or Num1 == Num2) :
            count = count + 1
            Test = True
            Num1 = Num1 / Num2
    
        else :
            print("\nNot Found\n")
            Test2 = False
            break
    
    if (not Test2) :
        continue

    elif (Test) :
        print ("\n",Num2,"^",count,"=",Save,"\n")
        continue

    if (T) :
        print("\nNot Found\n")
        continue