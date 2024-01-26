def Preparing_Text (Text , Key) :
    
    Alpha = "abcdefghiklmnopqrstuvwxyz"
    Matrix = []
    Key = Key.lower()
    Text = Text.lower()

    Key = Key.replace("j", "i")
    Text = Text.replace("j", "i")

    for Char in Key + Alpha :
        if Char not in Matrix :
            Matrix.append(Char)
    
    n=0
    Sub_Texts = []
    while (n < len(Text)) :
        Sub_Texts.append(Text[n:n+2])
        
        if ( not Sub_Texts[-1][0].isalpha()) :
            n += 1
            Sub_Texts[-1] = Sub_Texts[-1][0]
            continue
        elif (len(Sub_Texts[-1]) > 1 and not Sub_Texts[-1][1].isalpha()) :
            Sub_Texts.append(Sub_Texts[-1][1])
            Sub_Texts[-2] = Sub_Texts[-2][0] + "x"
            n += 2
            continue
        
        if (len(Sub_Texts[-1]) == 1) :
            Sub_Texts[-1] = Sub_Texts[-1]+"x"
            #n = n + 1
        elif (Sub_Texts[-1][0] == Sub_Texts[-1][1]) :
            Sub_Texts[-1] = Text[n:n+1]+"x"
            n-=1
        n += 2
        
    return Sub_Texts , Text , Matrix


def Encryption_Playfair_Cipher (Text , Key) :
    Encryption = ""
    Sub_Text , Text , Matrix = Preparing_Text(Text, Key)
    
    for i in Sub_Text :
        
        if (not i.isalpha()) :
            Encryption += i
            continue
        
        Row1, Col1 = divmod(Matrix.index(i[0]), 5)
        Row2, Col2 = divmod(Matrix.index(i[1]), 5)
        
        if (Row1 == Row2) :
            Col1 = (Col1 + 1) % 5
            Col2 = (Col2 + 1) % 5
        
        elif (Col1 == Col2):
            Row1 = (Row1 + 1) % 5
            Row2 = (Row2 + 1) % 5
        
        else :
            Col1 , Col2 = Col2 , Col1
        
        Encryption += Matrix[(Row1 * 5) + Col1] + Matrix[(Row2 * 5) + Col2]
    
    print("\nThe Encryption of your Text ["+Text+"] using Playfair Cipher Encryption is ["+Encryption+"]")


def Decryption_Playfair_Cipher (Text , Key) :
    Decryption = ""
    Sub_Text , Text , Matrix = Preparing_Text(Text, Key)
    n=0
    for i in Sub_Text :
        
        if (not i.isalpha()) :
            Decryption += i
            continue
        
        n+=2
        Row1, Col1 = divmod(Matrix.index(i[0]), 5)
        Row2, Col2 = divmod(Matrix.index(i[1]), 5)
        
        if (Row1 == Row2) :
            Col1 = (Col1 - 1) % 5
            Col2 = (Col2 - 1) % 5
        
        elif (Col1 == Col2):
            Row1 = (Row1 - 1) % 5
            Row2 = (Row2 - 1) % 5
        
        else :
            Col1 , Col2 = Col2 , Col1
        
        Decryption += Matrix[(Row1 * 5) + Col1] + Matrix[(Row2 * 5) + Col2]
        
        if (n > 3 and Decryption[-2] == Decryption[-4] and Decryption[-3] == "x") :
            Decryption = Decryption.replace(Decryption[-3], "")
    
    print("\nThe Decryption of your Text ["+Text+"] using Playfair Cipher Decryption is ["+Decryption+"]")



print("\nPlease, Enter the number of the process which you need : ")
print("\n\t1) Encryption using Playfair cipher \n\t2) Decryption using Playfair Cipher ")
Choose = input("\nYour Choise : ")

Key = ""
Text = ""

while (True) :
    try :
        G = int(Choose) / 1
        Choose = int(Choose)
        if (Choose > 0 and Choose < 3) :
            break
        else :
            G = "n" + Choose
    except :
        print("\nSorry!! Invalid input. Please, Try again")
        Choose = input("Please, Enter Your choice again : ")

if (Choose == 1) :
    Text = input("\nPlease, Enter the Text to Encrypt it : ")
    Key = input("Please, Enter the Key : ")
    Encryption_Playfair_Cipher(Text,Key)

else :
    Text = input("\nPlease, Enter the Text to Decrypt it : ")
    Key = input("Please, Enter the Key : ")
    Decryption_Playfair_Cipher(Text,Key)







