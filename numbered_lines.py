# numbered_lines

##############################################################################

def numbered_lines():
	with open("small.txt", 'rb') as f:
		text = f.read().splitlines()
		# for item in text:
		# 	text.append
		# return text
		return text

def write_file(text):
	"""write a function that writes lines with numbers and appends each line
	with the item from the list I'm sending (from numbered_lines)"""
	with open("new.txt", "a") as fwrite:
		for i in range(len(text)):
			fwrite.write (str(i+1) + " " + text[i] + '\n')




##############################################################################
def main():  # CALL YOUR FUNCTION BELOW

	print write_file(numbered_lines())
	# print numbered_lines()


if __name__ == '__main__':
    main()