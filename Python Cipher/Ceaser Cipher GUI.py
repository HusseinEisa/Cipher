import tkinter as tk

def str_to_int(key):
    if key.isalpha() and key.isupper():
        key = chr(ord(key) - 65)
        key = int(ord(key))
    elif key.isalpha():
        key = chr(ord(key) - 97)
        key = int(ord(key))

    key = int(key) % 26

    return key

def encryption_ceaser_cipher(text, key):
    encryption = ""

    key = str_to_int(key)

    for char in text:
        if (ord(char) < 65 or ord(char) > 122) or (ord(char) < 97 and ord(char) > 90):
            encryption += char
        elif char.isupper() and (ord(char) + key) > 90:
            encryption += chr(ord(char) - (26 - key))
        elif char.islower() and (ord(char) + key) > 122:
            encryption += chr(ord(char) - (26 - key))
        else:
            encryption += chr(ord(char) + key)

    result_label.config(text=f"The Encryption of your Text [{text}] using Ceaser Cipher Encryption is [{encryption}]")

def decryption_ceaser_cipher(text, key):
    decryption = ""

    key = str_to_int(key)

    for char in text:
        if (ord(char) < 65 or ord(char) > 122) or (ord(char) < 97 and ord(char) > 90):
            decryption += char
        elif char.isupper() and (ord(char) - key) < 65:
            decryption += chr(ord(char) + (26 - key))
        elif char.islower() and (ord(char) - key) < 97:
            decryption += chr(ord(char) + (26 - key))
        else:
            decryption += chr(ord(char) - key)

    result_label.config(text=f"The Decryption of your Text [{text}] using Ceaser Cipher Decryption is [{decryption}]")

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

    if choice == 1:
        text = text_entry.get()
        key = key_entry.get()
        encryption_ceaser_cipher(text, key)
    else:
        text = text_entry.get()
        key = key_entry.get()
        decryption_ceaser_cipher(text, key)

# Create the main Tkinter window
root = tk.Tk()
root.title("Ceaser Cipher GUI")

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
