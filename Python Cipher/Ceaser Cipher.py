def Str_To_Int (Key) :
    if (Key.isalpha() and Key.isupper()) :
        Key = chr(ord(Key) - 65)
        Key = int(ord(Key))
    elif (Key.isalpha()) :
        Key = chr(ord(Key) - 97)
        Key = int(ord(Key))
    
    Key = int(Key) % 26
    
    return (Key)
    
    
def Encryption_Ceaser_Cipher (Text , Key) :
    Encryption = ""
    
    Key = Str_To_Int(Key)
    
    for Char in Text :
        if (ord(Char)<65 or ord(Char)>122) or (ord(Char)<97 and ord(Char)>90) :
            Encryption += Char
        elif (Char.isupper() and (ord(Char) + Key) > 90) :
            Encryption += chr(ord(Char) - (26 - Key))
        elif (Char.islower() and (ord(Char) + Key) > 122) :
            Encryption += chr(ord(Char) - (26 - Key))
        else :
            Encryption += chr(ord(Char) + Key)
        
    print("\nThe Encryption of your Text ["+Text+"] using Ceaser Cipher Encryption is ["+Encryption+"]")


def Decryption_Ceaser_Cipher (Text , Key) :
    Decryption = ""
    
    Key = Str_To_Int(Key)
    
    for Char in Text :
        if (ord(Char)<65 or ord(Char)>122) or (ord(Char)<97 and ord(Char)>90) :
            Decryption += Char
        elif (Char.isupper() and (ord(Char) - Key) < 65) :
            Decryption += chr(ord(Char) + (26 - Key))
        elif (Char.islower() and (ord(Char) - Key) < 97) :
            Decryption += chr(ord(Char) + (26 - Key))
        else :
            Decryption += chr(ord(Char) - Key)
        
    print("\nThe Decryption of your Text ["+Text+"] using Ceaser Cipher Decryption is ["+Decryption+"]")



print("\nPlease, Enter the number of the process which you need : ")
print("\n\t1) Encryption using Ceaser cipher \n\t2) Decryption using Ceaser Cipher ")
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
    Encryption_Ceaser_Cipher(Text, Key)

else :
    Text = input("\nPlease, Enter the Text to Decrypt it : ")
    Key = input("Please, Enter the Key : ")
    Decryption_Ceaser_Cipher(Text, Key)

