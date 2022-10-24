try:
    arquivo = open("arquivo_exception.txt", "r")
except OSError:
    print("arquivo inexistente")
else:
    print("arquivo manipulado e fechado com sucesso")
    arquivo.close()
finally:
    print("Tentativa de abrir arquivo")