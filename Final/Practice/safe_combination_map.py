LETTER_MAP = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J'}

def main():
	code = input("Code: ")
	combo = ""
	for num in code:
		combo += LETTER_MAP[int(num)]
	print(combo)

if __name__ == "__main__":
	main()