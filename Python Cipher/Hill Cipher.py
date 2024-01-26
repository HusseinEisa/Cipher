MOD = 26
key = []
txt_size = 0
row = 0
column = 0
txt = ""

def egcd(a, b, x, y):
    if not b:
        x = 1
        y = 0
        return a
    g = egcd(b, a % b, y, x)
    y -= (a // b) * x
    return g

def mod_inverse(a):
    x, y, g = egcd(a, MOD, 0, 0)
    if g > 1:
        return -1
    return (x + MOD) % MOD

def string_to_key(k):
    mat = [[0 for _ in range(column)] for _ in range(row)]
    l = 0
    for i in range(row):
        for j in range(column):
            if l < len(k):
                mat[i][j] = ord(k[l]) - ord('a')
                l += 1
    return mat

def hill_cipher_encrypt():
    global txt_size, txt, row, column, key
    encrypted_text = ""
    for _ in range(txt_size, row):
        txt += 'x'
    for i in range(0, txt_size, row):
        v = [ord(txt[i + j]) - ord('a') for j in range(row)]
        for j in range(row):
            total = sum(key[j][k] * v[k] for k in range(row))
            total %= MOD
            encrypted_text += chr(total + ord('A'))
    return encrypted_text

def hill_cipher_decrypt():
    global txt_size, txt, row, key
    plaintext = ""
    detrimine = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    det_inverse = mod_inverse(detrimine)

    inverse_key = [
        [key[1][1], -key[0][1]],
        [-key[1][0], key[0][0]]
    ]

    for i in range(row):
        for j in range(row):
            inverse_key[i][j] = ((inverse_key[i][j] * det_inverse) % MOD + MOD) % MOD

    for i in range(0, txt_size, row):
        v = [ord(txt[i + j]) - ord('A') for j in range(row)]
        for j in range(row):
            total = sum(inverse_key[j][k] * v[k] for k in range(row))
            total %= MOD
            plaintext += chr(total + ord('a'))
    return plaintext

def main():
    global txt_size, txt, row, column, key
    print("============================================================================================================= Welcome to the pecoden program! ========================================================================================================================")
    while True:
        print("Menu:")
        print("1. Encrypt")
        print("##=========================================##")
        print("2. Decrypt")
        print("##=========================================##")
        print("3. Exit")
        print("##=========================================##")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            txt_size = int(input("Enter the size of the text: "))
            txt = input("Enter the text: ")
            print("KEY represented as a string or matrix ? : ")
            choice1 = int(input("Menu:\n1. String\n##=========================================##\n2. Matrix\n##=========================================##\nEnter your choice: "))
            if choice1 == 1:
                s = input("Enter the Key string: ")
                row = int(input("Enter the number of rows of keys: "))
                column = int(input("Enter the number of columns of keys: "))
                key = string_to_key(s)
                encrypted_text = hill_cipher_encrypt()
                print("Encrypted text:", encrypted_text)
            elif choice1 == 2:
                row = int(input("Enter the number of rows of keys: "))
                column = int(input("Enter the number of columns of keys: "))
                print("Enter the key matrix:")
                key = [list(map(int, input().split())) for _ in range(row)]
                encrypted_text = hill_cipher_encrypt()
                print("Encrypted text:", encrypted_text)
            else:
                print("Invalid choice.")
        elif choice == 2:
            txt_size = int(input("Enter the size of the text: "))
            txt = input("Enter the text: ")
            print("KEY represented as a string or matrix ? : ")
            choice1 = int(input("Menu:\n1. String\n##=========================================##\n2. Matrix\n##=========================================##\nEnter your choice: "))
            if choice1 == 1:
                s = input("Enter the Key string: ")
                row = int(input("Enter the number of rows of keys: "))
                column = int(input("Enter the number of columns of keys: "))
                key = string_to_key(s)
                decrypted_text = hill_cipher_decrypt()
                print("Decrypted text:", decrypted_text)
            elif choice1 == 2:
                row = int(input("Enter the number of rows of keys: "))
                column = int(input("Enter the number of columns of keys: "))
                print("Enter the key matrix:")
                key = [list(map(int, input().split())) for _ in range(row)]
                decrypted_text = hill_cipher_decrypt()
                print("Decrypted text:", decrypted_text)
            else:
                print("Invalid choice.")
        elif choice == 3:
            return
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()