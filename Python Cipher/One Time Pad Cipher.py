def Encryption_One_Time_Pad(Text, Key):
    # Initializing cipherText
    EncryptionText = ""
 
    # Initialize cipher array of key length
    # which stores the sum of corresponding no.'s
    # of plainText and key.
    Encryption = []
    for i in range(len(Key)):
        Encryption.append(ord(Text[i]) - ord('A') + ord(Key[i])-ord('A'))
 
    # If the sum is greater than 25
    # subtract 26 from it
    # and store that resulting value
    for i in range(len(Key)):
        if Encryption[i] > 25:
            Encryption[i] = Encryption[i] - 26
 
    # Converting the no.'s into integers
    # Convert these integers to corresponding
    # characters and add them up to cipherText
 
    for i in range(len(Key)):
        x = Encryption[i] + ord('A')
        EncryptionText += chr(x)
 
    # Print the cipherText
    print("\nEncryption Text using One-Time-Pad cipher is: " + EncryptionText)
 
 
# Method 2
# Returning plain text
def Decryption_One_Time_Pad(Text, Key):
 
    # Initializing plain text
    DecryptionText = ""
 
    # Initializing integer array of key length
    # which stores difference
    # of corresponding no.'s of
    # each character of cipherText and key
 
    Decryption = []
 
    # Running for loop for each character
    # subtracting and storing in the array
 
    for i in range(len(Key)):
        Decryption.append(ord(Text[i]) - ord('A') - (ord(Key[i]) - ord('A')))
 
    # If the difference is less than 0
    # add 26 and store it in the array.
    for i in range(len(Key)):
        if (Decryption[i] < 0):
            Decryption[i] = Decryption[i] + 26
 
    # Converting int to corresponding char
    # add them up to plainText
 
    for i in range(len(Key)):
        x = Decryption[i] + ord('A')
        DecryptionText += chr(x)
 
    # Print plainText
    print("\nDecryption Text using One-Time-Pad cipher is: " + DecryptionText)
 
 
 
print("\nPlease, Enter the number of the process which you need : ")
print("\n\t1) Encryption using One-Time-Pad cipher \n\t2) Decryption using One-Time-Pad cipher")
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
    Encryption_One_Time_Pad(Text.upper(),Key.upper())

else :
    Text = input("\nPlease, Enter the Text to Decrypt it : ")
    Key = input("Please, Enter the Key : ")
    Decryption_One_Time_Pad(Text.upper(),Key.upper())
 
 
 