import tkinter as tk
from tkinter import *

def preparing_key(key, alpha):
    mono_key = ""
    for x in key + alpha:
        if x in mono_key or (not x.isalpha()):
            continue
        else:
            mono_key = mono_key + x
    return mono_key

def encryption_mono(text, key, alpha):
    encryption_text = ""
    for x in range(len(text)):
        if not text[x].isalpha():
            encryption_text = encryption_text + text[x]
        else:
            index = alpha.index(text[x])
            encryption_text = encryption_text + key[index]

    result_label.config(text=f"Encryption Text using Mono Alphabetic cipher is: {encryption_text}")

def decryption_mono(text, key, alpha):
    decryption_text = ""
    for x in range(len(text)):
        if not text[x].isalpha():
            decryption_text = decryption_text + text[x]
        else:
            index = key.index(text[x])
            decryption_text = decryption_text + alpha[index]

    result_label.config(text=f"Decryption Text using Mono Alphabetic cipher is: {decryption_text}")

def process_choice():
    choice = choice_entry.get()

    key = ""
    text = ""

    try:
        g = int(choice) / 1
        choice = int(choice)
        if 0 < choice < 3:
            pass
        else:
            g = "n" + str(choice)
    except ValueError:
        result_label.config(text="Sorry!! Invalid input. Please, Try again")
        return
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if choice == 1:
        text = text_entry.get()
        key = key_entry.get()
        key = preparing_key(key.upper(), alpha)
        encryption_mono(text.upper(), key, alpha)
    else:
        text = text_entry.get()
        key = key_entry.get()
        key = preparing_key(key.upper(), alpha)
        decryption_mono(text.upper(), key, alpha)

# Create the main Tkinter window
root = tk.Tk()
#root.geometry("800x500")
root.title("Mono Alphabetic Cipher GUI")


# Create and place widgets in the window
text_label = tk.Label(root, text="Enter the Text:")
text_label.pack(pady=5)

text_entry = tk.Entry(root, width=30)
text_entry.pack(pady=5)

key_label = tk.Label(root, text="Enter the Key:")
key_label.pack(pady=5)

key_entry = tk.Entry(root, width=30)
key_entry.pack(pady=5)

choice_label = tk.Label(root, text="Enter the number of the process (1 for Encryption, 2 for Decryption):")
choice_label.pack(pady=5)

choice_entry = tk.Entry(root, width=30)
choice_entry.pack(pady=5)

process_button = tk.Button(root, text="Process", command=process_choice)
process_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
