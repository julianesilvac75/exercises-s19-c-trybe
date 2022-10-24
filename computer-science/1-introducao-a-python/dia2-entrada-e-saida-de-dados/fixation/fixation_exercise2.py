numbers = input("Digite seus números (separados por espaço): ")
splitted_numbers = numbers.split(" ")
sum = 0

for number in splitted_numbers:
    if number.isdigit():
        sum += int(number)
    else:
        print(
            f"Erro ao somar valores, {number} é um valor inválido")

print("Soma:", sum)