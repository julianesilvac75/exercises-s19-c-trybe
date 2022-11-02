from fabrica import ComboFeliz, ComboGelado, ComboTudo, ComboFritas


if __name__ == "__main__":
    combo_escolhido = input(
        "Ola, qual seu pedido? [ComboTudo, ComboFeliz, ComboGelado, ComboFritas]:"
    )

    #Para transformar uma string em código executável basta usar o método eval()
    # Equivalente a chamar ComboTudo(), ComboFeliz(), ComboGelado()

    combo = eval(combo_escolhido)()

    print(f"\nCriando o combo {type(combo).__name__}.")
    print(f"Combo fabricado com os seguintes itens: {combo.exibe_itens()}")