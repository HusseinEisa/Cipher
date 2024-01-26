import tkinter as tk
from tkinter import messagebox

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

def on_encrypt_button_click():
    global txt_size, txt, row, column, key
    txt_size = int(txt_size_entry.get())
    txt = txt_entry.get()

    key_input = key_entry.get()
    choice1 = key_choice_var.get()

    if choice1 == 1:
        row = int(row_entry.get())
        column = int(column_entry.get())
        key = string_to_key(key_input)
    elif choice1 == 2:
        row = int(row_entry.get())
        column = int(column_entry.get())
        key = [list(map(int, key_input.split())) for _ in range(row)]

    encrypted_text = hill_cipher_encrypt()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Encrypted text: " + encrypted_text)

def on_decrypt_button_click():
    global txt_size, txt, row, key
    txt_size = int(txt_size_entry.get())
    txt = txt_entry.get()

    key_input = key_entry.get()
    choice1 = key_choice_var.get()

    if choice1 == 1:
        row = int(row_entry.get())
        column = int(column_entry.get())
        key = string_to_key(key_input)
    elif choice1 == 2:
        row = int(row_entry.get())
        column = int(column_entry.get())
        key = [list(map(int, key_input.split())) for _ in range(row)]

    decrypted_text = hill_cipher_decrypt()
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Decrypted text: " + decrypted_text)

def on_exit_button_click():
    root.destroy()

root = tk.Tk()
root.title("Hill Cipher GUI")

# GUI components
txt_size_label = tk.Label(root, text="Enter the size of the text:")
txt_size_entry = tk.Entry(root)

txt_label = tk.Label(root, text="Enter the text:")
txt_entry = tk.Entry(root)

key_label = tk.Label(root, text="Enter the Key:")
key_entry = tk.Entry(root)

key_choice_var = tk.IntVar()
key_choice_var.set(1)

key_choice_label = tk.Label(root, text="KEY represented as a string or matrix? :")

key_string_rb = tk.Radiobutton(root, text="String", variable=key_choice_var, value=1)
key_matrix_rb = tk.Radiobutton(root, text="Matrix", variable=key_choice_var, value=2)

row_label = tk.Label(root, text="Enter the number of rows of keys:")
row_entry = tk.Entry(root)

column_label = tk.Label(root, text="Enter the number of columns of keys:")
column_entry = tk.Entry(root)

encrypt_button = tk.Button(root, text="Encrypt", command=on_encrypt_button_click)
decrypt_button = tk.Button(root, text="Decrypt", command=on_decrypt_button_click)
exit_button = tk.Button(root, text="Exit", command=on_exit_button_click)

result_text = tk.Text(root, height=5, width=50)

# GUI layout
txt_size_label.grid(row=0, column=0, padx=5, pady=5)
txt_size_entry.grid(row=0, column=1, padx=5, pady=5)
txt_label.grid(row=1, column=0, padx=5, pady=5)
txt_entry.grid(row=1, column=1, padx=5, pady=5)
key_label.grid(row=2, column=0, padx=5, pady=5)
key_entry.grid(row=2, column=1, padx=5, pady=5)
key_choice_label.grid(row=3, column=0, padx=5, pady=5)
key_string_rb.grid(row=3, column=1, padx=5, pady=5)
key_matrix_rb.grid(row=3, column=2, padx=5, pady=5)
row_label.grid(row=4, column=0, padx=5, pady=5)
row_entry.grid(row=4, column=1, padx=5, pady=5)
column_label.grid(row=4, column=2, padx=5, pady=5)
column_entry.grid(row=4, column=3, padx=5, pady=5)
encrypt_button.grid(row=5, column=0, padx=5, pady=5)
decrypt_button.grid(row=5, column=1, padx=5, pady=5)
exit_button.grid(row=5, column=2, padx=5, pady=5)
result_text.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
