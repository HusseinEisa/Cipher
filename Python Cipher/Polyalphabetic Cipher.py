def Preparing (Text) :
    Num = int(input("Please, Enter the number of keyes : "))
    Keyes = []
    for i in range(1, Num+1, 1) :
        print("Please, Enter the number of steps at Key number",i,"(1,2,3,...): ")
        step=int(input()) % 26
        print("Please, Enter the Direction at Key number",i,"(Right / Left): ")
        di=input().lower()
        key = [step , di]
        Keyes.append(key)
    
    Sub_Texts = [""] ; n=0
    for i in Text :
        if n == len(Keyes) :
            n=0
            Sub_Texts.append("")
        
        if i.isalpha() :
            n+=1
            Sub_Texts[-1] = Sub_Texts[-1] + i
        else :
            n=0
            Sub_Texts.append(i)
            Sub_Texts.append("")
    
    return Keyes , Sub_Texts


def Encryption_Polyalphabetic_Cipher (Text) :
    Keyes , Sub_Texts = Preparing (Text)
    
    Encryption = ""
    
    for i in Sub_Texts :
        if (not i.isalpha()) :
            Encryption += i
            continue
        
        for k in range(len(i)) :
            if (Keyes[k][1] == "r" or Keyes[k][1] == "right") :
                if ( ord(i[k]) + Keyes[k][0] > 122) :
                    Encryption += chr(ord(i[k]) - (26 - Keyes[k][0]))
                else :
                    Encryption += chr(ord(i[k]) + Keyes[k][0])
            
            elif (Keyes[k][1] == "l" or Keyes[k][1] == "left") :
                if ( ord(i[k]) - Keyes[k][0] < 97) :
                    Encryption += chr(ord(i[k]) + (26 - Keyes[k][0]))
                else :
                    Encryption += chr(ord(i[k]) - Keyes[k][0])
        
    
    print("\nThe Encryption of your Text ["+Text+"] using Polyalphabetic Cipher Encryption is ["+Encryption+"]")


def Decryption_Polyalphabetic_Cipher (Text) :
    Keyes , Sub_Texts = Preparing (Text)
    
    Decryption = ""
    
    for i in Sub_Texts :
        if (not i.isalpha()) :
            Decryption += i
            continue
        
        for k in range(len(i)) :
            if (Keyes[k][1] == "r" or Keyes[k][1] == "right") :
                if ( ord(i[k]) - Keyes[k][0] < 97) :
                    Decryption += chr(ord(i[k]) + (26 - Keyes[k][0]))
                else :
                    Decryption += chr(ord(i[k]) - Keyes[k][0])
            
            elif (Keyes[k][1] == "l" or Keyes[k][1] == "left") :
                if ( ord(i[k]) + Keyes[k][0] > 122) :
                    Decryption += chr(ord(i[k]) - (26 - Keyes[k][0]))
                else :
                    Decryption += chr(ord(i[k]) + Keyes[k][0])
        
    
    print("\nThe Decryption of your Text ["+Text+"] using Polyalphabetic Cipher Decryption is ["+Decryption+"]")



print("\nPlease, Enter the number of the process which you need : ")
print("\n\t1) Encryption using Polyalphabetic cipher \n\t2) Decryption using Polyalphabetic Cipher ")
Choose = input("\nYour Choise : ")

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
    Text = input("\nPlease, Enter the Text to encrypt it : ").lower()
    Encryption_Polyalphabetic_Cipher(Text)

else :
    Text = input("\nPlease, Enter the Text to decrypt it : ").lower()
    Decryption_Polyalphabetic_Cipher(Text)