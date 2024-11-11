def collatz(num):
    """Função que exemplifica o que está acontecendo na Conjectura de Collatz"""
    while num > 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
    return num

def collatz_seq(num):
    """Ilustra o processo da Conjectura de Collatz na forma de um diagrama"""
    while num > 1:
        print(f"{num} ⟶ ", end = "")
        num = collatz(num)
    print(num)
