from collatz import collatz, collatz_seq


def collatz_practice():
    """Pede ao usuário para que insira um número e, assim, ilustra o processo da conjectura de Collatz por meio de
    um diagrama"""
    while True:
        try:
            num = int(input(f"Olá! Insira um número inteiro maior do que 1: "))
            if num < 1:
                print(f"O número precisa ser maior do que 1! Tente novamente.")
            else:
                print(f"\nIniciando o processo para {num}...")
                collatz(num)
                print(
                    f"Terminamos! Aqui está o procedimento da Conjectura de Collatz ilustrada para seu número {num}: ")
                collatz_seq(num)
                break
        except ValueError:
            print(f"Você precisa inserir um número inteiro válido! Tente novamente.")


collatz_practice()











