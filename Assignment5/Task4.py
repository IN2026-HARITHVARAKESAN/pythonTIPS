"""Demonstrate that strings and integers are immutable in Python."""

if __name__ == "__main__":
	
	text = "Python"
	number = 12345

	print("Original string:", text)
	try:
		text[0] = "J"
	except TypeError as error:
		print("Changing a string character failed:", error)

	print("Original integer:", number)
	try:
		number[0] = 9
	except TypeError as error:
		print("Changing an integer digit failed:", error)

	text = "J" + text[1:]
	number = 92345
	print("New string after reassignment:", text)
	print("New integer after reassignment:", number)