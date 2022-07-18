def main():
	width = int(input("Digite a largura: "))
	height = int(input("Digite a altura: "))
	character = "#"
	retângulo(width, height, character)

def retângulo(width, height, character):
	line = character * width
	for i in range(height):
		print(line)

main()
