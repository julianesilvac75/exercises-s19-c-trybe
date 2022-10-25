file = open("arquivo_teste_read.txt", mode="w")
file.write("Trybe S2")
file.close()

file = open("arquivo_teste_read.txt", mode="r")
content = file.read()
print(content)
file.close()