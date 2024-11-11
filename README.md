# Ilustrador simples para a Conjectura de Collatz em Python

Neste simples e intuitivo projeto, ilustramos o procedimento por trás da famosa [*Conjectura de Collatz*](https://en.wikipedia.org/wiki/Collatz_conjecture), um famoso problema de *Teoria dos Números*, proposto pelo matemático alemão [*Lothar Collatz*](https://en.wikipedia.org/wiki/Lothar_Collatz), em 1937, que permanece sem solução desde então.   
Embora o enunciado da conjectura seja compreensível até para pessoas "leigas" em matemática, sua simplicidade esconde um interessantíssimo, e igualmente inquietante, enigma da matemática moderna.  
O enunciado da Conjectura de Collatz lê-se como:

(**Conjectura de Collatz**) Seja $n > 1$ um número inteiro positivo arbitrário, e consideremos a função $f \colon \mathbb{N} \longrightarrow \mathbb{N}$ tal que 
$$f(n) \coloneqq \begin{cases*}
3n + 1, \text{se $n \cong 1$ (mod 2)} \\ 2n, \text{se $n \cong 0$ (mod 2)
\end{cases*}$$  
Considerando a sequência $(a_k)$ tal que $a_1 = n$ e $a_k = f(a_{k\,-\,1})$, para $k > 1$, então existe algum índice $k$ para o qual $a_k = 1$.  
Ou seja, eventualmente a sequência iterativa $(a_k)$ cessa em 1.