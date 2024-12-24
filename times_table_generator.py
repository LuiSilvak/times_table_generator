# Gerador de Tabuada

def gerador_de_tabuada():
    print("=== Gerador de Tabuada ===")
    try:
        numero = int(input("Digite um número para gerar a tabuada: "))
        print(f"\nTabuada do {numero}:")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")


if __name__ == "__main__":
    gerador_de_tabuada()