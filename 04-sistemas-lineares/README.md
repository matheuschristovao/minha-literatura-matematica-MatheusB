# 04 · Sistemas lineares — Listas de exercícios

**Autor:** Matheus Bueno Christovão (185302)
**Aulas relacionadas:** Sistemas lineares — Gauss e LU · Cholesky e Jacobi · Método SOR

## Arquivos

| Arquivo | Método | Conteúdo |
|---|---|---|
| [`lista_gauss_eliminacao-e-balanco-termico.ipynb`](lista_gauss_eliminacao-e-balanco-termico.ipynb) | **Eliminação de Gauss** (direto) | Notebook com os 5 exercícios: resoluções manuais em texto e código executado |
| [`lista_gauss_eliminacao-e-balanco-termico.py`](lista_gauss_eliminacao-e-balanco-termico.py) | Eliminação de Gauss | Mesmo conteúdo em script Python (versão original entregue) |
| [`lista_gauss-seidel_resolucao.ipynb`](lista_gauss-seidel_resolucao.ipynb) | **Gauss–Seidel** (iterativo) | Notebook com Q1–Q4 transcritas e Q5–Q7 executadas (tabela e gráficos) |
| [`lista_gauss-seidel_resolucao.pdf`](lista_gauss-seidel_resolucao.pdf) | Gauss–Seidel | Resolução original entregue: folhas manuscritas (Q1–Q4), código e saídas (Q5–Q7) |

### Eliminação de Gauss (`.ipynb` / `.py`)

1. **Ex. 1:** forma matricial $A\mathbf{x} = \mathbf{b}$
2. **Ex. 2:** eliminação de Gauss passo a passo, com os multiplicadores $m_{ik}$ impressos
3. **Ex. 3:** classificação do número de soluções (única, infinitas ou nenhuma)
4. **Ex. 4:** implementação própria **sem pivoteamento**, comparada com `numpy.linalg.solve` (norma da diferença e resíduo)
5. **Ex. 5:** modelo de **balanço térmico** com matriz tridiagonal e diagonalmente dominante. Solução: $T_1 = T_2 = T_3 = 5$

```bash
pip install numpy
python lista_gauss_eliminacao-e-balanco-termico.py
```

### Gauss–Seidel (`.ipynb` / `.pdf`)

- Q1–Q3: forma matricial, verificação da **dominância diagonal estrita** e fórmulas iterativas
- Q4: três primeiras iterações à mão, a partir de $\mathbf{x}^{(0)} = (0,0,0)$
- Q5: função `gauss_seidel()` com critério $\lVert \mathbf{x}^{(k)} - \mathbf{x}^{(k-1)} \rVert_\infty < 10^{-5}$,
  e solução $(1{,}00000003;\ 1{,}99999998;\ -1{,}00000001)$ em 6 iterações
- Q6: tabela das iterações
- Q7: gráficos de $x^{(k)}, y^{(k)}, z^{(k)}$ e do erro em escala log, para o sistema com solução exata $(1, 2, -1)$
