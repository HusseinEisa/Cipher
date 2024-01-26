import tkinter as tk

def encryption_one_time_pad(text, key):
    # Initializing cipherText
    encryption_text = ""

    # Initialize cipher array of key length
    # which stores the sum of corresponding no.'s
    # of plainText and key.
    encryption = []
    for i in range(len(key)):
        encryption.append(ord(text[i]) - ord('A') + ord(key[i]) - ord('A'))

    # If the sum is greater than 25
    # subtract 26 from it
    # and store that resulting value
    for i in range(len(key)):
        if encryption[i] > 25:
            encryption[i] = encryption[i] - 26

    # Converting the no.'s into integers
    # Convert these integers to corresponding
    # characters and add them up to cipherText

    for i in range(len(key)):
        x = encryption[i] + ord('A')
        encryption_text += chr(x)

    result_label.config(text=f"Encryption Text using One-Time-Pad cipher is: {encryption_text}")

# Method 2
# Returning plain text
def decryption_one_time_pad(text, key):
    # Initializing plain text
    decryption_text = ""

    # Initializing integer array of key length
    # which stores difference
    # of corresponding no.'s of
    # each character of cipherText and key

    decryption = []

    # Running for loop for each character
    # subtracting and storing in the array

    for i in range(len(key)):
        decryption.append(ord(text[i]) - ord('A') - (ord(key[i]) - ord('A')))

    # If the difference is less than 0
    # add 26 and store it in the array.
    for i in range(len(key)):
        if decryption[i] < 0:
            decryption[i] = decryption[i] + 26

    # Converting int to corresponding char
    # add them up to plainText

    for i in range(len(key)):
        x = decryption[i] + ord('A')
        decryption_text += chr(x)

    result_label.config(text=f"Decryption Text using One-Time-Pad cipher is: {decryption_text}")

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
        encryption_one_time_pad(text.upper(), key.upper())
    else:
        text = text_entry.get()
        key = key_entry.get()
        decryption_one_time_pad(text.upper(), key.upper())

# Create the main Tkinter window
root = tk.Tk()
root.title("One-Time Pad Cipher GUI")

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
