def collatz(num):
    """Função que exemplifica o que está acontecendo na Conjectura de Collatz"""
    while num > 1:
        if num % 2 == 0:
            return num // 2
        else:
            return 3 * num + 1


def collatz_seq(num):
    """Retorna a sequência da Conjectura de Collatz numa lista"""
    sequence = []  # Lista para armazenar a sequência
    while num > 1:
        sequence.append(num)  # Adiciona o número à sequência
        num = collatz(num)  # Calcula o próximo número na sequência
    sequence.append(1)  # Adiciona o último número (1) à sequência
    return sequence


def diagram_collatz_seq(num):
    """Imprime a sequência de Collatz no formato de diagrama"""
    sequence = collatz_seq(num)  # Obtém a sequência
    print(" ⟶ ".join(map(str, sequence)))  # Imprime no formato desejado
