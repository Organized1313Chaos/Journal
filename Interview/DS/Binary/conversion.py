# Function to convert Decimal number
# to Binary number

def decimalToBinary(n):
	return bin(n).replace("0b","")

# Function to convert Binary number
# to Decimal number

def binaryToDecimal(n):
	return int(n,2)

# Driver code
if __name__ == '__main__':
	print(decimalToBinary(8))
	print(decimalToBinary(18))
	print(decimalToBinary(7))
