def PreparingKey (Key,Alpha):
    MonoKey = ""
    for X in Key+Alpha:
        if X in MonoKey or (not X.isalpha()):
            continue
        else:
            MonoKey = MonoKey + X
    return MonoKey

def Encryption_Mono (Text, Key, Alpha):
    EncryptionText = ""
    for X in range(len(Text)):
        if (not Text[X].isalpha()):
            EncryptionText = EncryptionText + Text[X]
        else:
            Index = Alpha.index(Text[X])
            EncryptionText = EncryptionText + Key[Index]
    
    print("\nEncryption Text using Mono Alphabetic cipher is: " + EncryptionText)

def Decryption_Mono (Text, Key, Alpha):
    DecryptionText = ""
    for X in range(len(Text)):
        if (not Text[X].isalpha()):
            DecryptionText = DecryptionText + Text[X]
        else:
            Index = Key.index(Text[X])
            DecryptionText = DecryptionText + Alpha[Index]
    
    print("\nDecryption Text using Mono Alphabetic cipher is: " + DecryptionText)


print("\nPlease, Enter the number of the process which you need : ")
print("\n\t1) Encryption using Mono Alphabetic cipher \n\t2) Decryption using Mono Alphabetic Cipher ")
Choose = input("\nYour Choise : ")

Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
    Key = PreparingKey(Key.upper(), Alpha)
    Encryption_Mono(Text.upper(), Key, Alpha)

else :
    Text = input("\nPlease, Enter the Text to Decrypt it : ")
    Key = input("Please, Enter the Key : ")
    Key = PreparingKey(Key.upper(), Alpha)
    Decryption_Mono(Text.upper(), Key, Alpha)

