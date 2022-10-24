file = open("arquivo_teste.txt", mode="w")

file.write("nome idade\n")
file.write("Maria 45\n")
file.write("Miguel 33\n")

print("Tulio 23", file=file)

LINES = ["Alberto 35\n", "Betina 23\n", "Joao 42\n", "Victor 19\n"]
file.writelines(LINES)

file.close()
