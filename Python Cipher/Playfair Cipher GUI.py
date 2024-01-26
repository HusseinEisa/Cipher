import tkinter as tk

def preparing_text(text, key):
    alpha = "abcdefghiklmnopqrstuvwxyz"
    matrix = []
    key = key.lower()
    text = text.lower()

    key = key.replace("j", "i")
    text = text.replace("j", "i")

    for char in key + alpha:
        if char not in matrix:
            matrix.append(char)

    n = 0
    sub_texts = []
    while n < len(text):
        sub_texts.append(text[n:n + 2])

        if not sub_texts[-1][0].isalpha():
            n += 1
            sub_texts[-1] = sub_texts[-1][0]
            continue
        elif len(sub_texts[-1]) > 1 and not sub_texts[-1][1].isalpha():
            sub_texts.append(sub_texts[-1][1])
            sub_texts[-2] = sub_texts[-2][0] + "x"
            n += 2
            continue

        if len(sub_texts[-1]) == 1:
            sub_texts[-1] = sub_texts[-1] + "x"
        elif sub_texts[-1][0] == sub_texts[-1][1]:
            sub_texts[-1] = text[n:n + 1] + "x"
            n -= 1
        n += 2

    return sub_texts, text, matrix


def encryption_playfair_cipher(text, key):
    encryption = ""
    sub_text, text, matrix = preparing_text(text, key)

    for i in sub_text:

        if not i.isalpha():
            encryption += i
            continue

        row1, col1 = divmod(matrix.index(i[0]), 5)
        row2, col2 = divmod(matrix.index(i[1]), 5)

        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5

        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5

        else:
            col1, col2 = col2, col1

        encryption += matrix[(row1 * 5) + col1] + matrix[(row2 * 5) + col2]

    result_label.config(text=f"The Encryption of your Text [{text}] using Playfair Cipher Encryption is [{encryption}]")

def decryption_playfair_cipher(text, key):
    decryption = ""
    sub_text, text, matrix = preparing_text(text, key)
    n = 0
    for i in sub_text:

        if not i.isalpha():
            decryption += i
            continue

        n += 2
        row1, col1 = divmod(matrix.index(i[0]), 5)
        row2, col2 = divmod(matrix.index(i[1]), 5)

        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5

        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5

        else:
            col1, col2 = col2, col1

        decryption += matrix[(row1 * 5) + col1] + matrix[(row2 * 5) + col2]

        if n > 3 and decryption[-2] == decryption[-4] and decryption[-3] == "x":
            decryption = decryption.replace(decryption[-3], "")

    result_label.config(text=f"The Decryption of your Text [{text}] using Playfair Cipher Decryption is [{decryption}]")

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
        encryption_playfair_cipher(text, key)
    else:
        text = text_entry.get()
        key = key_entry.get()
        decryption_playfair_cipher(text, key)

# Create the main Tkinter window
root = tk.Tk()
root.title("Playfair Cipher GUI")

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
