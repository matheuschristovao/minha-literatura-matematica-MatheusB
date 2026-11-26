# -*- coding: utf-8 -*-
"""
Cálculo Numérico — Lista de Exercícios
Sistemas lineares e implementação numérica

Matheus Bueno Christovão 185302

Requisitos: Python 3 + NumPy  (pip install numpy)
Execução:   python lista_sistemas_lineares.py
"""

import numpy as np

np.set_printoptions(precision=4, suppress=True)


def titulo(texto):
    print("\n" + "=" * 70)
    print(texto)
    print("=" * 70)


# =============================================================================
# FUNÇÃO PRINCIPAL — ELIMINAÇÃO DE GAUSS SEM PIVOTEAMENTO (usada nos Ex. 2, 4, 5)
# =============================================================================
def eliminacao_gauss(A, b, verbose=True, tol=1e-12):
    """
    Resolve Ax = b por eliminação de Gauss SEM pivoteamento.

    Parâmetros
    ----------
    A : matriz n x n dos coeficientes
    b : vetor independente (n)
    verbose : se True, imprime a matriz aumentada a cada etapa
    tol : tolerância para considerar um pivô como nulo

    Retorna
    -------
    x : vetor solução
    M : matriz aumentada triangular superior final [U | c]
    """
    # Conversão para float (evita divisão inteira e não altera os dados originais)
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)

    if A.shape != (n, n):
        raise ValueError("A deve ser quadrada e compatível com o tamanho de b.")

    # 1) Formação da matriz aumentada [A | b]
    M = np.hstack([A, b.reshape(-1, 1)])
    if verbose:
        print("Matriz aumentada inicial [A | b]:")
        print(M)

    # 2) Eliminação progressiva: zera os elementos abaixo de cada pivô M[k, k]
    for k in range(n - 1):
        # Sem pivoteamento, um pivô nulo interrompe o método
        if abs(M[k, k]) < tol:
            raise ZeroDivisionError(
                f"Pivô nulo na posição ({k+1},{k+1}). "
                "Sem pivoteamento, o método não pode prosseguir."
            )
        for i in range(k + 1, n):
            m = M[i, k] / M[k, k]           # multiplicador m_ik
            M[i, k:] = M[i, k:] - m * M[k, k:]  # L_i <- L_i - m_ik * L_k
            if verbose:
                print(f"  L{i+1} <- L{i+1} - ({m:.4g}) * L{k+1}")
        if verbose:
            print(f"Matriz após zerar a coluna {k+1}:")
            print(M)

    if abs(M[n - 1, n - 1]) < tol:
        raise ZeroDivisionError("Último pivô nulo: matriz singular (sem solução única).")

    # 3) Substituição regressiva: resolve Ux = c de baixo para cima
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        soma = M[i, i + 1:n] @ x[i + 1:n]   # soma dos termos já conhecidos
        x[i] = (M[i, n] - soma) / M[i, i]

    # 4) Exibição da solução
    if verbose:
        print("Solução por substituição regressiva:")
        for i, xi in enumerate(x):
            print(f"  x{i+1} = {xi:.6f}")

    return x, M


def comparar_com_numpy(A, b, x_gauss):
    """Compara a solução própria com numpy.linalg.solve e mostra o resíduo."""
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x_np = np.linalg.solve(A, b)
    print("numpy.linalg.solve      :", x_np)
    print("Eliminação de Gauss     :", x_gauss)
    print("||x_gauss - x_numpy||   :", np.linalg.norm(x_gauss - x_np))
    print("Resíduo ||A x - b||     :", np.linalg.norm(A @ x_gauss - b))
    print("Soluções coincidem?     :", np.allclose(x_gauss, x_np))


# =============================================================================
# EXERCÍCIO 1 — Sistemas lineares na forma matricial
# =============================================================================
#
# a)  2x +  y =  7
#      x - 3y = -5
#
#     A = | 2   1 |      x = | x |      b = |  7 |
#         | 1  -3 |          | y |          | -5 |
#
#   
#
# b)   x + 2y -  z = 2
#     3x -  y + 2z = 9
#     2x +  y +  z = 7
#
#     A = | 1   2  -1 |      x = | x |      b = | 2 |
#         | 3  -1   2 |          | y |          | 9 |
#         | 2   1   1 |          | z |          | 7 |
#
# =============================================================================
def exercicio_1():
    titulo("EXERCÍCIO 1 — Forma matricial Ax = b")

    print("a) A =\n", np.array([[2, 1], [1, -3]]))
    print("   x = [x, y]^T")
    print("   b =", np.array([7, -5]))
    print("   Solução (verificação):", np.linalg.solve([[2, 1], [1, -3]], [7, -5]))

    print("\nb) A =\n", np.array([[1, 2, -1], [3, -1, 2], [2, 1, 1]]))
    print("   x = [x, y, z]^T")
    print("   b =", np.array([2, 9, 7]))
    print("   det(A) =", round(np.linalg.det([[1, 2, -1], [3, -1, 2], [2, 1, 1]]), 6))
    print("   Solução (verificação):",
          np.linalg.solve([[1, 2, -1], [3, -1, 2], [2, 1, 1]], [2, 9, 7]))


# =============================================================================
# EXERCÍCIO 2 — Eliminação de Gauss (resolução manual)
# =============================================================================
#
#    2x +  y -  z =   8
#   -3x -  y + 2z = -11
#   -2x +  y + 2z =  -3
#
# Matriz aumentada inicial:
#
#   |  2   1  -1 |   8 |
#   | -3  -1   2 | -11 |
#   | -2   1   2 |  -3 |
#
# --- Etapa 1: pivô a11 = 2 (zerar a coluna 1 abaixo dele) ---
#   m21 = -3/2 = -1,5   ->  L2 <- L2 - (-1,5)L1 = L2 + 1,5 L1
#        (-3 + 3 ; -1 + 1,5 ; 2 - 1,5 ; -11 + 12) = (0 ; 0,5 ; 0,5 ; 1)
#   m31 = -2/2 = -1     ->  L3 <- L3 - (-1)L1 = L3 + L1
#        (-2 + 2 ; 1 + 1 ; 2 - 1 ; -3 + 8)       = (0 ; 2 ; 1 ; 5)
#
#   |  2   1    -1   |  8 |
#   |  0   0,5   0,5 |  1 |
#   |  0   2     1   |  5 |
#
# --- Etapa 2: pivô a22 = 0,5 (zerar a coluna 2 abaixo dele) ---
#   m32 = 2/0,5 = 4     ->  L3 <- L3 - 4 L2
#        (0 ; 2 - 2 ; 1 - 2 ; 5 - 4)              = (0 ; 0 ; -1 ; 1)
#
#   |  2   1    -1   |  8 |
#   |  0   0,5   0,5 |  1 |      <- forma triangular superior
#   |  0   0    -1   |  1 |
#
# --- Substituição regressiva ---
#   L3:  -z = 1                 ->  z = -1
#   L2:  0,5y + 0,5(-1) = 1     ->  0,5y = 1,5   ->  y = 3
#   L1:  2x + 3 - (-1) = 8      ->  2x = 4       ->  x = 2
#
#   Solução: (x, y, z) = (2, 3, -1)
# =============================================================================
A2 = [[2, 1, -1],
      [-3, -1, 2],
      [-2, 1, 2]]
b2 = [8, -11, -3]


def exercicio_2():
    titulo("EXERCÍCIO 2 — Eliminação de Gauss (passos reproduzidos no código)")
    x, _ = eliminacao_gauss(A2, b2, verbose=True)
    print("\nResultado esperado (manual): x = 2, y = 3, z = -1")
    return x


# =============================================================================
# EXERCÍCIO 3 — Número de soluções (redução da matriz aumentada)
# =============================================================================
# Critério (Teorema de Rouché–Capelli), com n = número de incógnitas:
#   posto(A) = posto([A|b]) = n  -> solução única (SPD)
#   posto(A) = posto([A|b]) < n  -> infinitas soluções (SPI)
#   posto(A) < posto([A|b])      -> nenhuma solução (SI)
#
# a)  | 1  1 | 3 |   L2 <- L2 - 2L1   | 1  1 | 3 |
#     | 2  2 | 6 |   ------------->   | 0  0 | 0 |
#     A linha 0 = 0 é sempre verdadeira; sobra uma equação para duas incógnitas.
#     posto(A) = posto([A|b]) = 1 < 2  ->  INFINITAS SOLUÇÕES
#     Solução geral: y = t,  x = 3 - t  (t ∈ R). Retas coincidentes.
#
# b)  | 1  1 | 3 |   L2 <- L2 - 2L1   | 1  1 | 3 |
#     | 2  2 | 7 |   ------------->   | 0  0 | 1 |
#     A linha diz 0 = 1, o que é absurdo.
#     posto(A) = 1 < posto([A|b]) = 2  ->  NENHUMA SOLUÇÃO
#     Retas paralelas distintas.
#
# c)  | 1   1 | 3 |   L2 <- L2 - 2L1   | 1   1 |  3 |
#     | 2  -1 | 0 |   ------------->   | 0  -3 | -6 |
#     -3y = -6  ->  y = 2 ;  x + 2 = 3  ->  x = 1
#     posto(A) = posto([A|b]) = 2  ->  SOLUÇÃO ÚNICA: (x, y) = (1, 2)
#     Retas concorrentes.
#
# =============================================================================
def classificar_sistema(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)
    n = A.shape[1]
    posto_A = np.linalg.matrix_rank(A)
    posto_Ab = np.linalg.matrix_rank(np.hstack([A, b]))
    if posto_A < posto_Ab:
        tipo = "nenhuma solução (sistema impossível)"
    elif posto_A < n:
        tipo = "infinitas soluções (sistema possível e indeterminado)"
    else:
        tipo = "solução única (sistema possível e determinado)"
    return posto_A, posto_Ab, tipo


def exercicio_3():
    titulo("EXERCÍCIO 3 — Número de soluções")
    sistemas = {
        "a": ([[1, 1], [2, 2]], [3, 6]),
        "b": ([[1, 1], [2, 2]], [3, 7]),
        "c": ([[1, 1], [2, -1]], [3, 0]),
    }
    for item, (A, b) in sistemas.items():
        pA, pAb, tipo = classificar_sistema(A, b)
        print(f"{item}) posto(A) = {pA}, posto([A|b]) = {pAb}  ->  {tipo}")
        if pA == pAb == len(b):
            print("   Solução:", np.linalg.solve(A, b))


# =============================================================================
# EXERCÍCIO 4 — Implementação da eliminação de Gauss + comparação com NumPy
# =============================================================================
# A implementação é a função `eliminacao_gauss` definida no início do arquivo:
#   • recebe A e b;
#   • forma a matriz aumentada [A | b];
#   • elimina os elementos abaixo dos pivôs (L_i <- L_i - m_ik L_k);
#   • aplica substituição regressiva;
#   • exibe a solução.
#
# Conclusão: as duas soluções devem coincidir até a precisão de
# máquina (diferença da ordem de 1e-15 ou zero) e o resíduo ||Ax - b|| deve ser
# praticamente nulo. Sem pivoteamento o método funciona aqui porque nenhum pivô
# se anula (2 e 0,5 e -1). Em geral, pivôs nulos ou muito pequenos causam falha
# ou amplificação de erros de arredondamento — daí o pivoteamento parcial,
# usado internamente por numpy.linalg.solve (via LAPACK, fatoração LU).
# =============================================================================
def exercicio_4():
    titulo("EXERCÍCIO 4 — Gauss sem pivoteamento vs numpy.linalg.solve")
    x, _ = eliminacao_gauss(A2, b2, verbose=False)
    comparar_com_numpy(A2, b2, x)


# =============================================================================
# EXERCÍCIO 5 — Modelo de balanço térmico
# =============================================================================
#
#   |  4  -1   0 | |T1|   | 15 |
#   | -1   4  -1 | |T2| = | 10 |
#   |  0  -1   3 | |T3|   | 10 |
#
# a) Resolução manual (eliminação de Gauss)
#
#   |  4  -1   0 | 15 |
#   | -1   4  -1 | 10 |
#   |  0  -1   3 | 10 |
#
# --- Etapa 1: pivô a11 = 4 ---
#   m21 = -1/4  ->  L2 <- L2 + (1/4)L1
#       (-1 + 1 ; 4 - 1/4 ; -1 + 0 ; 10 + 15/4) = (0 ; 15/4 ; -1 ; 55/4)
#   m31 = 0/4 = 0  ->  L3 inalterada
#
#   |  4  -1     0 | 15   |
#   |  0  15/4  -1 | 55/4 |      (15/4 = 3,75 ; 55/4 = 13,75)
#   |  0  -1     3 | 10   |
#
# --- Etapa 2: pivô a22 = 15/4 ---
#   m32 = (-1)/(15/4) = -4/15  ->  L3 <- L3 + (4/15)L2
#       a33: 3 + (4/15)(-1)     = 3 - 4/15  = 41/15  (≈ 2,7333)
#       b3 : 10 + (4/15)(55/4)  = 10 + 11/3 = 41/3   (≈ 13,6667)
#
#   |  4  -1      0    | 15   |
#   |  0  15/4   -1    | 55/4 |
#   |  0   0     41/15 | 41/3 |
#
# --- Substituição regressiva ---
#   T3 = (41/3) / (41/15) = 15/3 = 5
#   (15/4)T2 - 5 = 55/4   ->  (15/4)T2 = 75/4  ->  T2 = 5
#   4T1 - 5 = 15          ->  T1 = 5
#
#   Solução: T1 = T2 = T3 = 5
#
# Interpretação: a rede entra em equilíbrio com as três temperaturas iguais
# (5 unidades). A matriz é tridiagonal, simétrica e diagonalmente dominante
# (|4| > |-1|+|0|, |4| > |-1|+|-1|, |3| > |-1|+|0|), o que garante pivôs não
# nulos na eliminação sem pivoteamento e boa estabilidade numérica.
# A estrutura é a mesma de uma análise nodal em circuitos resistivos
# (condutâncias na matriz, "fontes" no vetor independente).
#
# b) Implementação em Python: 
# =============================================================================
A5 = [[4, -1, 0],
      [-1, 4, -1],
      [0, -1, 3]]
b5 = [15, 10, 10]


def exercicio_5():
    titulo("EXERCÍCIO 5 — Modelo de balanço térmico")
    T, _ = eliminacao_gauss(A5, b5, verbose=True)
    print()
    comparar_com_numpy(A5, b5, T)
    print(f"\nTemperaturas: T1 = {T[0]:.4f}, T2 = {T[1]:.4f}, T3 = {T[2]:.4f}")
    print("Resultado esperado (manual): T1 = T2 = T3 = 5")


# =============================================================================
if __name__ == "__main__":
    exercicio_1()
    exercicio_2()
    exercicio_3()
    exercicio_4()
    exercicio_5()
