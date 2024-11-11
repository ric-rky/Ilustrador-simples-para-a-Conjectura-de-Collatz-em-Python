from collatz import collatz, collatz_seq
import matplotlib.pyplot as plt

def collatz_plot(num):
    """Plota o gráfico da sequência de Collatz"""
    sequence = collatz_seq(num)
    plt.figure(figsize=(10, 6))

    # Plota a sequência de Collatz
    plt.plot(range(len(sequence)), sequence, marker='o', linestyle='-', color='b')

    # Títulos do gráfico e marcadores
    plt.title(f"Sequência de Collatz para o número {num}")
    plt.xlabel("Passos")
    plt.ylabel("Valor da sequência")

    # Exibe o gráfico
    plt.grid(True)  # Grade
    plt.show()

collatz_plot(10)