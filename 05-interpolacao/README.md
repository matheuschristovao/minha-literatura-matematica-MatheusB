# 05 · Interpolação polinomial

**Autores:** Matheus Bueno Christovão (185302) e Vinicius Cruz Cuervo (185337)
**Aulas relacionadas:** Interpolação de Lagrange · Diferenças divididas de Newton · Tarefa de erros de interpolação

## Arquivos

| Arquivo | Tipo | Conteúdo |
|---|---|---|
| [`atividade-guiada_interpolacao-polinomial.ipynb`](atividade-guiada_interpolacao-polinomial.ipynb) | Atividade guiada | Conceitos de interpolação e extrapolação, comparação de ferramentas, fenômeno de Runge e regressão |
| [`tarefa-investigativa_erros-interpolacao-barra-aquecida.ipynb`](tarefa-investigativa_erros-interpolacao-barra-aquecida.ipynb) | Tarefa investigativa | Reconstrução do perfil de temperatura de uma barra aquecida a partir de sensores |

### Atividade guiada: interpolação polinomial

- Construção do polinômio interpolador com `numpy.polynomial.Polynomial.fit`
- Comparação NumPy × GeoGebra × WolframAlpha. As três ferramentas concordaram em $P(x) = x^2 - 2x + 1$
- Sensibilidade: alterar uma única medida muda **a curva inteira**, porque o polinômio é global
- Fenômeno de Runge com 15 nós igualmente espaçados

### Tarefa investigativa: barra aquecida ($L = 6$ m)

| Etapa | Pergunta | Métodos comparados |
|---|---|---|
| 1 | Qual método é mais preciso com 7 sensores ideais? | Lagrange (forma baricêntrica), splines linear, quadrática e cúbica natural |
| 2 | Como o número e a posição dos sensores afetam o erro? | Nós equiespaçados × nós de **Chebyshev** |
| 3 | O que acontece com N de 4 a 40? | Erro máximo, RMSE e tempo de execução |
| 4 | Qual método recomendar em campo? | Parecer técnico |
| Extras | Sensores com ruído e sensores longe das extremidades | Spline de suavização com validação cruzada |

**Conclusão do parecer:** com dados exatos, Lagrange com nós de Chebyshev ou spline cúbica. Com muitos nós
equiespaçados, o polinômio global fica instável. **Com ruído, interpolar deixa de ser adequado** e deve-se usar um
ajuste (spline de suavização ou mínimos quadrados).

Dependências: `numpy`, `pandas`, `matplotlib`, `scipy`.
