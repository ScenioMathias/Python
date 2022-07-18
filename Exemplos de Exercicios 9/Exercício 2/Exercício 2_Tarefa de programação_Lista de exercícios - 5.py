def main():
	width = int(input("Digite a largura: "))
	height = int(input("Digite a altura: "))
	height = height - 2
	character = "#"
	retangulo(width, height, character)
	

def retangulo(width, height, character):
	print(character * width)
	
	for i in range(height):
		espacos = (width - 2) * ' '
		print("%s%s%s" % (character, espacos, character))
		
	print(character * width)
	
	
main()

	
