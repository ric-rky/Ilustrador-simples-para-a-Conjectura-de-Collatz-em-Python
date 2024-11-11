# Ilustrador simples para a Conjectura de Collatz em Python

Neste simples e intuitivo projeto, ilustramos o procedimento por trás da famosa [*Conjectura de Collatz*](https://en.wikipedia.org/wiki/Collatz_conjecture), um famoso problema de *Teoria dos Números*, proposto pelo matemático alemão [*Lothar Collatz*](https://en.wikipedia.org/wiki/Lothar_Collatz), em 1937, que permanece sem solução desde então.   
Embora o enunciado da conjectura seja compreensível até para pessoas "leigas" em matemática, sua simplicidade esconde um interessantíssimo, e igualmente inquietante, enigma da matemática moderna.

## 1. Objetivo
Este projeto tem como objetivo ilustrar o processo da Conjectura de Collatz através de uma implementação simples em Python, utilizando gráficos para uma melhor compreensão do comportamento da sequência gerada a partir de um número inicial fornecido pelo usuário.

## 2. Pré-requisitos
Para rodar este projeto, você precisará ter uma instalação do Python, juntamente da biblioteca `matplotlib` para a plotagem do gráfico.

## 3. Instalação
Siga os passos abaixo para instalar o projeto e começar a utilizá-lo:
### Passo 1: Download do projeto
- Caso você já tenha o **Git** instalado, no terminal, digite o seguinte comando: 
```bash
     git clone https://github.com/ric-rky/collatz-illustrator.git
```
- Caso não tenha, ou prefira um método mais simples, você pode baixar o repositório do projeto diretamente do GitHub.  
Para tanto, vá até a página do repositório no GitHub e clique em **Code > Download ZIP**. Após o download, extraia o arquivo em seu computador. 
### Passo 2: Testando o código
1. **Abrir os arquivos**:

- Após baixar o repositório, abra a pasta do projeto num interpretador Python e localize os arquivos `.py` (por exemplo, `collatz.py` e `collatz_plot.py`).

2. **Rodar o código**:
   - Abra o terminal e navegue até a pasta onde os arquivos do projeto estão localizados.
   - Para testar as funções, você pode digitar o seguinte comando no terminal (supondo que você tenha o arquivo `collatz.py`):
    ```bash
    python collatz.py
    ```
   - Também pode testar a função de plotagem com o comando:
    ```bash
    python collatz_plot.py
    ```

## 4. Usando o Projeto

- **Função de sequência Collatz**: O código gera a sequência da Conjectura de Collatz para um número fornecido. Você pode chamar a função `collatz_seq(7)` para ver a sequência gerada a partir do número 7, por exemplo.
  
- **Função de plotagem**: Para visualizar o gráfico da sequência, basta chamar `collatz_plot(7)`. Isso criará um gráfico que ilustra como os números da sequência se comportam à medida que você aplica as regras da conjectura.

## 5. Como Contribuir

Se você tiver ideias para melhorias ou quiser corrigir bugs, fique à vontade para fazer contribuições. Você pode enviar um **Pull Request** ou abrir um **Issue** para discutir mudanças.

Obrigado! 

