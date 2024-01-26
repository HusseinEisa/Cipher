
# function to encrypt a message
def Encryption_Rail_Fence(Text, Key):

	# create the matrix to cipher
	# plain text key = rows ,
	# length(text) = columns
	# filling the rail matrix
	# to distinguish filled
	# spaces from blank ones
	rail = [['\n' for i in range(len(Text))]
				for j in range(Key)]
	
	# to find the direction
	dir_down = False
	row, col = 0, 0
	
	for i in range(len(Text)):
		
		# check the direction of flow
		# reverse the direction if we've just
		# filled the top or bottom rail
		if (row == 0) or (row == Key - 1):
			dir_down = not dir_down
		
		# fill the corresponding alphabet
		rail[row][col] = Text[i]
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
	for i in range(Key):
		for j in range(len(Text)):
			if rail[i][j] != '\n':
				result.append(rail[i][j])
                
    
	return("" . join(result))
    
	
# This function receives cipher-text
# and key and returns the original
# text after decryption
def Decryption_Rail_Fence(Text, Key):

	# create the matrix to cipher
	# plain text key = rows ,
	# length(text) = columns
	# filling the rail matrix to
	# distinguish filled spaces
	# from blank ones
	rail = [['\n' for i in range(len(Text))]
				for j in range(Key)]
	
	# to find the direction
	dir_down = None
	row, col = 0, 0
	
	# mark the places with '*'
	for i in range(len(Text)):
		if row == 0:
			dir_down = True
		if row == Key - 1:
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
	for i in range(Key):
		for j in range(len(Text)):
			if ((rail[i][j] == '*') and
			(index < len(Text))):
				rail[i][j] = Text[index]
				index += 1
		
	# now read the matrix in
	# zig-zag manner to construct
	# the resultant text
	result = []
	row, col = 0, 0
	for i in range(len(Text)):
		
		# check the direction of flow
		if row == 0:
			dir_down = True
		if row == Key-1:
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
	return("".join(result))


print("\nPlease, Enter the number of the process which you need : ")
print("\n\t1) Encryption using Rail Fence cipher \n\t2) Decryption using Rail Fence cipher")
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
    Key = int(input("Please, Enter the Key : "))
    print("\nEncryption Text using Rail Fence cipher is: " + Encryption_Rail_Fence(Text.upper(),Key))
    
else :
    Text = input("\nPlease, Enter the Text to Decrypt it : ")
    Key = int(input("Please, Enter the Key : "))
    print("\nDecryption Text using Rail Fence cipher is: " + Decryption_Rail_Fence(Text.upper(),Key))
    

# attack at once             2          atc toctaka ne
# GeeksforGeeks              3          GsGsekfrek eoe
# defend the east wall       3          dnhaweedtees alf  tl

