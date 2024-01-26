def Preparing (Text , Key) :
    Sub_Texts = [""] ; n=0
    for i in Text :
        if n == len(Key) :
            n=0
            Sub_Texts.append("")
        
        if i.isalpha() :
            n+=1
            Sub_Texts[-1] = Sub_Texts[-1] + i
        else :
            n=0
            Sub_Texts.append(i)
            Sub_Texts.append("")
    
    return Sub_Texts


def Encryption_Vigenere_Cipher (Text , Key) :
    Sub_Texts = Preparing(Text, Key) 
    
    Encryption = ""
    
    for char in Sub_Texts :
        if (not char.isalpha()) :
            Encryption += char
            continue
        for n in range(len(char)) :
            if ((ord(char[n]) + (ord(Key[n]) - 97)) > 122) :
                Encryption += chr( (ord(char[n]) + (ord(Key[n]) - 97)) - 26 )
            else :
                Encryption += chr(ord(char[n]) + (ord(Key[n]) - 97))
    
    print("\nThe Encryption of your Text ["+Text+"] using Vigenere Cipher Encryption is ["+Encryption+"]")



def Decryption_Vigenere_Cipher (Text , Key) :
    Sub_Texts = Preparing(Text, Key) 
    
    Decryption = ""
    
    for char in Sub_Texts :
        if (not char.isalpha()) :
            Decryption += char
            continue
        for n in range(len(char)) :
            if ((ord(char[n]) - (ord(Key[n]) - 97)) < 97) :
                Decryption += chr( (ord(char[n]) - (ord(Key[n]) - 97)) + 26 )
            else :
                Decryption += chr(ord(char[n]) - (ord(Key[n]) - 97))
    
    print("\nThe Decryption of your Text ["+Text+"] using Vigenere Cipher Decryption is ["+Decryption+"]")





print("\nPlease, Enter the number of the process which you need : ")
print("\n\t1) Encryption using Vigenere cipher \n\t2) Decryption using Vigenere Cipher ")
Choose = input("\nYour Choise : ")

Text = ""
Key = ""

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
    Text = input("\nPlease, Enter the Text to Encrypt it : ").lower()
    Key = input("Please, Enter the Key : ").lower()
    Encryption_Vigenere_Cipher(Text , Key)

else :
    Text = input("\nPlease, Enter the Text to Decrypt it : ").lower()
    Key = input("Please, Enter the Key : ").lower()
    Decryption_Vigenere_Cipher(Text , Key)