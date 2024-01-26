import tkinter as tk

def encryption_rail_fence(text, key):
    # create the matrix to cipher
    # plain text key = rows ,
    # length(text) = columns
    # filling the rail matrix
    # to distinguish filled
    # spaces from blank ones
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    # to find the direction
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        # check the direction of flow
        # reverse the direction if we've just
        # filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        # fill the corresponding alphabet
        rail[row][col] = text[i]
        col += 1

        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher
    # using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])

    return "".join(result)

# This function receives cipher-text
# and key and returns the original
# text after decryption
def decryption_rail_fence(text, key):
    # create the matrix to cipher
    # plain text key = rows ,
    # length(text) = columns
    # filling the rail matrix to
    # distinguish filled spaces
    # from blank ones
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    # to find the direction
    dir_down = None
    row, col = 0, 0

    # mark the places with '*'
    for i in range(len(text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # place the marker
        rail[row][col] = '*'
        col += 1

        # find the next row
        # using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1

    # now we can construct the
    # fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(text)):
            if ((rail[i][j] == '*') and
                    (index < len(text))):
                rail[i][j] = text[index]
                index += 1

    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(text)):
        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False

        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1

        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)

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
        key = int(key_entry.get())
        result_label.config(text=f"Encryption Text using Rail Fence cipher is: {encryption_rail_fence(text.upper(), key)}")
    else:
        text = text_entry.get()
        key = int(key_entry.get())
        result_label.config(text=f"Decryption Text using Rail Fence cipher is: {decryption_rail_fence(text.upper(), key)}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Rail Fence Cipher GUI")

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
