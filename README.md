# Minha Literatura Matemática — Matheus Bueno

**Cálculo Numérico · UNIFESP — Instituto de Ciência e Tecnologia · Engenharia Biomédica**
**Profa. Raquel Jahara Lobosco · 2º semestre de 2026**
**Aluno:** Matheus Bueno Christovão — RA 185302

Este repositório reúne tudo o que produzi em Cálculo Numérico. Ele abre com a obra que escolhi como
"literatura matemática" e segue com um relato, em primeira pessoa, do que estudei no curso.

---

## Sumário

1. [A literatura selecionada: o potencial de ação de Hodgkin e Huxley (1952)](#1-a-literatura-selecionada-o-potencial-de-ação-de-hodgkin-e-huxley-1952)
2. [Sobre o que vimos no curso](#2-sobre-o-que-vimos-no-curso)
3. [Mapa do repositório](#3-mapa-do-repositório)
4. [Como executar](#4-como-executar)
5. [Definições e noções obtidas com o curso](#5-definições-e-noções-obtidas-com-o-curso)
6. [Referências](#6-referências)

---

## 1. A literatura selecionada: o potencial de ação de Hodgkin e Huxley (1952)

> A. L. Hodgkin e A. F. Huxley. **"A quantitative description of membrane current and its application to
> conduction and excitation in nerve."** *The Journal of Physiology*, 117(4), 500–544, 1952.

### 1.1 O que é

Esse artigo é o quinto e último de uma série que Alan Hodgkin e Andrew Huxley publicaram em 1952 sobre o
axônio gigante da lula. Nos quatro primeiros, eles mediram com *voltage clamp* as correntes de sódio e de
potássio que atravessam a membrana. No quinto, transformaram essas medidas num **modelo matemático** e
mostraram que o modelo reproduz o potencial de ação: a forma, o limiar, o período refratário e a
velocidade de propagação. O trabalho rendeu aos dois o Nobel de Fisiologia ou Medicina de 1963 e é, até
hoje, a base da neurociência computacional.

O modelo trata a membrana como um circuito elétrico: um capacitor em paralelo com três condutâncias
(sódio, potássio e uma corrente de fuga):

$$C_m \frac{dV}{dt} = I_{ext} - \bar g_{Na}\, m^3 h\,(V - E_{Na}) - \bar g_K\, n^4\,(V - E_K) - \bar g_L\,(V - E_L)$$

As variáveis $m$, $h$ e $n$ representam a abertura e o fechamento dos canais iônicos. Cada uma segue uma
equação diferencial com taxas que dependem da voltagem:

$$\frac{dx}{dt} = \alpha_x(V)\,(1 - x) - \beta_x(V)\,x, \qquad x \in \{m, h, n\}$$

Juntando tudo, temos **quatro equações diferenciais não lineares e acopladas**, com
$\bar g_{Na} = 120$, $\bar g_K = 36$ e $\bar g_L = 0{,}3$ mS/cm² e $C_m = 1\ \mu$F/cm². Esse sistema
**não tem solução analítica**. A única forma de saber se o modelo estava certo era resolver numericamente.

### 1.2 O cálculo numérico envolvido

Em 1951, quando as equações ficaram prontas, Huxley não
tinha um computador: segundo o relato de Hodgkin, o EDSAC de Cambridge estava parado para
modificações. Então Huxley integrou as equações **à mão, numa calculadora mecânica Brunsviga de
manivela**. Ele usou um método de integração passo a passo publicado por D. R. Hartree em 1932, que o
próprio artigo cita. Alguns números dessa tarefa:

- Segundo a Physiological Society, foram **mais de um milhão de operações com 6 casas decimais**. Isso
  ajuda a explicar os três anos entre os últimos experimentos e a publicação.
- Hodgkin contou que **só o potencial de ação propagado levou cerca de três semanas** de cálculo.
- Anos depois, o computador SEAC, nos EUA, levou cerca de 30 minutos para calcular o mesmo potencial de
  ação que tinha custado 8 horas a Huxley. Kenneth Cole brincou que a máquina valia **"16 Huxleys"**.

O cálculo da **velocidade de condução** é o que mais conversa com a disciplina. Para uma onda que se
propaga com velocidade constante $\theta$, a equação do cabo vira uma EDO de segunda ordem no tempo:

$$\frac{d^2V}{dt^2} = K\left(\frac{dV}{dt} + \frac{I_{ion}}{C_m}\right), \qquad K = \frac{2R_2\,\theta^2 C_m}{a}$$

O problema é que $\theta$ é desconhecida. Huxley **chutava um valor de $\theta$** e integrava a equação.
Se o chute fosse pequeno demais, $V$ disparava para $+\infty$; se fosse grande demais, para $-\infty$.
Com isso ele ia **encurralando o valor correto entre um chute "baixo" e um "alto"**, que é exatamente a
lógica da **bisseção** que implementei na Atividade III. O resultado foi uma velocidade de
**18,8 m/s**, próxima dos cerca de 21 m/s medidos no experimento.

### 1.3 Motivo de escolha

Primeiro, porque é a obra que mais tem a ver com o meu curso. Na engenharia biomédica, quase todo modelo
de tecido excitável (neurônio, músculo cardíaco, marcapasso) é descendente direto das equações de
Hodgkin–Huxley. Na minha iniciação científica, sobre modelagem de atividade epiléptica com integração ao
núcleo reticular talâmico, os modelos de neurônio que estudo usam esse mesmo formalismo de condutâncias.

### 1.4 O que da disciplina aparece nesta obra

| Tema do curso | Onde aparece em Hodgkin–Huxley | Onde aparece no meu repositório |
|---|---|---|
| Erros, arredondamento, algarismos significativos | Contas feitas à mão com 6 casas decimais: cada arredondamento se propagava por milhares de passos | [`01-erros-numericos`](01-erros-numericos/) |
| Estabilidade e escolha do passo de tempo | A integração passo a passo só funciona com $\Delta t$ pequeno. Com Euler explícito e passo grande, o modelo diverge | [`02-estabilidade-numerica`](02-estabilidade-numerica/) |
| Zeros de funções | Chute da velocidade $\theta$ com divergência para $\pm\infty$ (lógica da bisseção). O potencial de repouso é a raiz da corrente iônica total, $I_{ion}(V) = 0$ | [`03-zeros-de-funcoes`](03-zeros-de-funcoes/) |
| Sistemas lineares | Ao discretizar a equação do cabo de forma implícita, cada passo de tempo exige resolver um sistema **tridiagonal**, como o balanço térmico da minha lista de Gauss | [`04-sistemas-lineares`](04-sistemas-lineares/) |
| Interpolação × ajuste | As funções $\alpha(V)$ e $\beta(V)$ foram **ajustadas** a dados ruidosos de *voltage clamp*, não interpoladas: a mesma conclusão a que cheguei na tarefa da barra aquecida | [`05-interpolacao`](05-interpolacao/) |
| Integração numérica | O potencial de ação é, literalmente, a integral numérica das correntes iônicas ao longo do tempo | Vista em aula |

---

## 2. Sobre o que vimos no curso

### 2.1 Erros e representação numérica

O curso começou com perguntas como: por que `0.1 + 0.2` não dá exatamente `0.3` no Python? Para
responder, a gente estudou **bases numéricas** (binário, octal, hexadecimal, conversão por divisões
sucessivas) e viu que 0,1 tem dízima infinita em base 2. O computador guarda uma aproximação, no padrão
de **ponto flutuante**, com precisão limitada pelo *epsilon* de máquina
($\varepsilon \approx 2{,}2\times10^{-16}$ em `float64` e $\approx 1{,}2\times10^{-7}$ em `float32`).

A partir disso aprendemos a medir o erro de três formas: **absoluto** $E_a = |x - \tilde x|$, **relativo**
$E_r = E_a/|x|$ e **percentual**. Também vi a diferença entre **truncar** e **arredondar** e um dos
fenômenos que mais me marcou: a **perda de significância por cancelamento**. Subtrair dois números muito
próximos apaga os algarismos que eles têm em comum, e o resultado fica dominado pelo erro.

Na **Atividade I**, feita com o Luiz Ricardo, aplicamos tudo isso aos problemas da atividade.
Mostramos que o arredondamento sempre erra menos que o truncamento ($E_a \le 10^{-n}/2$) e que o
truncamento é enviesado. Vimos também que,
na lei de Hagen–Poiseuille, como $Q \propto r^4$, **um erro no raio é multiplicado por quatro na vazão**:
$\Delta Q/Q \approx 4\,\Delta r/r$. No nanocateter, reescrever a expressão na **forma de Horner**,
$t(4 + t(6 + t(4 + t)))$, eliminou a subtração problemática e recuperou a precisão que a forma direta
perdia.

### 2.2 Estabilidade numérica

Na atividade 2 vimos que um método pode estar "certo" e mesmo assim dar uma resposta
absurda. Simulamos o escoamento de Couette com **Euler explícito e diferenças finitas centrais**:

$$u_i^{n+1} = u_i^n + r\,(u_{i+1}^n - 2u_i^n + u_{i-1}^n), \qquad r = \frac{\nu\,\Delta t}{\Delta y^2}$$

O esquema só é estável para $r \le 1/2$. Acima disso, o coeficiente central $(1 - 2r)$ fica negativo e
o modo de maior frequência da malha é amplificado a cada passo. Com $r = 0{,}8$, a velocidade passou do
valor físico máximo **já no terceiro passo**, mas o *overflow* só apareceu no passo 121 (`float32`) ou 917
(`float64`). A lição: **instabilidade e overflow são coisas diferentes**, e trocar para `float64` não
corrige o método, só adia o erro. Também vi que refinar a malha **piora** a restrição, porque
$\Delta t_{max} = \Delta y^2/(2\nu)$ cai com o quadrado de $\Delta y$.

### 2.3 Zeros de funções

Depois estudamos como achar $r$ tal que $f(r) = 0$ quando não existe fórmula fechada.

- **Teorema do Valor Intermediário (Bolzano)** e **bisseção:** se $f(a)f(b) < 0$, existe raiz em
  $[a, b]$, e basta ir dividindo o intervalo ao meio. É lento (convergência linear), mas não falha.
- **Ponto fixo e método babilônico:** reescrever o problema como $x = g(x)$ e iterar. A convergência
  depende de $|g'(x^*)| < 1$. O método babilônico para $\sqrt{a}$, $x_{k+1} = \tfrac12(x_k + a/x_k)$, é
  um caso particular de Newton e já era usado na Babilônia há quase 4000 anos.
- **Newton:** $x_{k+1} = x_k - f(x_k)/f'(x_k)$. Usa a reta tangente e converge **quadraticamente**: o
  número de casas corretas praticamente dobra a cada iteração.
- **Secante:** troca a derivada pela inclinação entre os dois últimos pontos. Converge com ordem
  $\approx 1{,}618$ (a razão áurea) e não precisa de $f'$.

Na **Atividade III**, em grupo, implementamos os três métodos para quatro funções e fizemos um dashboard
com animações. A bisseção levou sempre 20 iterações (porque $1/2^{20} < 10^{-6}$), Newton levou de 2 a 4
e a secante de 4 a 6. Ver os gráficos do resíduo caindo em escala log deixou muito claro o que
"ordem de convergência" significa na prática.

### 2.4 Sistemas lineares

Essa parte foi a mais extensa. Começamos pelos **métodos diretos**:

- **Eliminação de Gauss:** operações elementares para triangularizar $[A \mid b]$, seguidas de
  substituição regressiva. Aprendi por que o **pivoteamento parcial** é necessário: um pivô nulo, ou
  muito pequeno, quebra o método ou amplifica erros.
- **Fatoração LU (Doolittle):** $A = LU$. A vantagem é fatorar uma vez e resolver para vários vetores
  $b$ com duas substituições triangulares.
- **Cholesky:** $A = LL^T$, válida só para matrizes **simétricas definidas positivas**. Aprendi a
  verificar isso pelos autovalores e pelos menores principais.

E depois os **métodos iterativos**, que fazem sentido para sistemas grandes e esparsos:

- **Jacobi**, que atualiza todas as variáveis com os valores da iteração anterior;
- **Gauss–Seidel**, que já usa os valores recém-calculados e por isso costuma convergir mais rápido;
- **SOR**, que acrescenta um fator de relaxação $\omega$ ao Gauss–Seidel. Com $\omega$ bem escolhido o
  número de iterações cai bastante, e com $\omega$ ruim o método pode divergir.

Para os iterativos, a **dominância diagonal estrita** é uma condição suficiente de convergência, e o
**resíduo** $r = b - A\hat x$ é a forma de conferir a solução. Nas listas implementei a eliminação de
Gauss sem pivoteamento, comparei com `numpy.linalg.solve`, resolvi um **balanço térmico** tridiagonal
($T_1 = T_2 = T_3 = 5$) e fiz o Gauss–Seidel à mão e em Python, com critério de parada
$\lVert x^{(k)} - x^{(k-1)} \rVert_\infty < 10^{-5}$.

### 2.5 Interpolação polinomial

O problema aqui é estimar valores **entre** medições. Vimos que $n + 1$ pontos distintos determinam um
único polinômio de grau no máximo $n$, que pode ser escrito de várias formas:

- **Lagrange:** $P(x) = \sum_i y_i\,L_i(x)$. É elegante, e a **forma baricêntrica** é a mais estável
  numericamente.
- **Newton (diferenças divididas):** permite acrescentar pontos sem refazer tudo.

E vimos o **erro de interpolação**, que depende de $f^{(n+1)}$ e do produto $\prod (x - x_i)$. Daí vem
o **fenômeno de Runge**: com muitos nós igualmente espaçados, o polinômio oscila perto das extremidades.

Na tarefa da **barra aquecida**, eu e o Vinicius comparamos Lagrange, splines (linear, quadrática e
cúbica) e **nós de Chebyshev**. Com sensores perfeitos, Lagrange com Chebyshev chegou a erro de
$10^{-14}$ °C, o limite do `float64`. Com nós equiespaçados, o erro passou a **crescer** a partir de
cerca de 15 sensores, por instabilidade. A conclusão mais importante veio de um experimento extra: com
**ruído** de 0,1 °C, nenhum interpolador ficou abaixo do próprio ruído, e o polinômio global chegou a
amplificá-lo para centenas de graus. **Com dados reais, o certo é ajustar (mínimos quadrados, spline
de suavização), não interpolar.** Foi a mesma decisão que Hodgkin e Huxley tomaram ao modelar as taxas
$\alpha(V)$ e $\beta(V)$.

### 2.6 Integração numérica

Por fim, vimos como aproximar $\int_a^b f(x)\,dx$ quando não dá para integrar analiticamente ou quando só
temos dados tabelados. Estudamos a **regra do ponto médio**, a **regra dos trapézios** e a
**regra de Simpson 1/3**, nas versões simples e compostas. Ficou claro como o erro cai com o número de
subintervalos e por que Simpson exige um número par deles. Simpson é exato para polinômios de até
terceiro grau, o que o torna bem mais preciso que os trapézios para funções suaves.

---

## 3. Mapa do repositório

```
├── 01-erros-numericos/         Atividade I: truncamento, arredondamento, Hagen–Poiseuille, nanocateter
├── 02-estabilidade-numerica/   Atividade II: Couette transiente, Euler explícito, overflow
├── 03-zeros-de-funcoes/        Atividade III: bisseção, Newton e secante (notebook, dashboard e 12 animações)
├── 04-sistemas-lineares/       Listas: eliminação de Gauss e Gauss–Seidel (notebooks + originais .py/.pdf)
├── 05-interpolacao/            Lagrange guiado e tarefa investigativa da barra aquecida
├── material-de-apoio/          Colinha de Python para a disciplina
└── requirements.txt
```

| Pasta | Arquivo principal | Tema | Autoria |
|---|---|---|---|
| [`01-erros-numericos`](01-erros-numericos/) | [`atividade-1_erros-numericos-biofluidodinamica.ipynb`](01-erros-numericos/atividade-1_erros-numericos-biofluidodinamica.ipynb) | Erros e precisão | Matheus e Luiz Ricardo |
| [`02-estabilidade-numerica`](02-estabilidade-numerica/) | [`atividade-2_estabilidade-overflow-couette.ipynb`](02-estabilidade-numerica/atividade-2_estabilidade-overflow-couette.ipynb) | Estabilidade e overflow | Matheus e Luiz Ricardo |
| [`03-zeros-de-funcoes`](03-zeros-de-funcoes/) | [`atividade-3_bissecao-newton-secante.ipynb`](03-zeros-de-funcoes/atividade-3_bissecao-newton-secante.ipynb) | Bisseção, Newton e secante | Matheus, Luiz Ricardo, Murilo e Vinicius |
| [`04-sistemas-lineares`](04-sistemas-lineares/) | [`lista_gauss_eliminacao-e-balanco-termico.ipynb`](04-sistemas-lineares/lista_gauss_eliminacao-e-balanco-termico.ipynb) e [`lista_gauss-seidel_resolucao.ipynb`](04-sistemas-lineares/lista_gauss-seidel_resolucao.ipynb) | Gauss e Gauss–Seidel | Matheus |
| [`05-interpolacao`](05-interpolacao/) | [`tarefa-investigativa_erros-interpolacao-barra-aquecida.ipynb`](05-interpolacao/tarefa-investigativa_erros-interpolacao-barra-aquecida.ipynb) | Lagrange, splines e Chebyshev | Matheus e Vinicius |
| [`material-de-apoio`](material-de-apoio/) | [`colinha-python_calculo-numerico.pdf`](material-de-apoio/colinha-python_calculo-numerico.pdf) | Consulta rápida de Python | Matheus |

Cada pasta tem um `README.md` próprio, com o objetivo, a estrutura e os principais resultados do trabalho.

---

## 4. Como executar

Todas as atividades estão em notebooks Jupyter (`.ipynb`), que abrem no **Google Colab** ou no Jupyter. Para rodar localmente:

```bash
git clone <url-deste-repositorio>
cd <pasta-do-repositorio>
pip install -r requirements.txt
jupyter notebook
```

O script de sistemas lineares roda direto no terminal:

```bash
python 04-sistemas-lineares/lista_gauss_eliminacao-e-balanco-termico.py
```

O dashboard da Atividade III é uma página HTML: basta abrir `03-zeros-de-funcoes/dashboard-html/index.html`
no navegador.

---

## 5. Definições e noções obtidas com o curso

Cada parte do curso me deu uma ferramenta para avaliar se um resultado numérico é confiável:

- a análise de **erro** para saber quantos algarismos são confiáveis;
- a análise de **estabilidade** para saber se o método está amplificando o erro;
- a **ordem de convergência** para escolher entre um método seguro e lento e um rápido e exigente;
- o **resíduo** e a comparação com uma referência para validar a resposta;
- a diferença entre **interpolar e ajustar** para lidar com dados reais, que sempre têm ruído.

A história de Hodgkin e Huxley junta tudo isso. Dois fisiologistas, uma calculadora de manivela e um
método numérico bem escolhido produziram um modelo que ainda hoje é usado para simular neurônios e
células cardíacas. Para mim, que quero trabalhar com modelagem em engenharia biomédica, foi a melhor
forma de enxergar que o cálculo numérico não é uma disciplina à parte: é o que transforma equações em
previsões.

---

## 6. Referências

**Declaração de uso de IA**
Para busca extensa por artigos, organização e formatação do arquivo README, assim como consulta para elaboração de um repositório adequado no GitHub, foram feitas consultas e solicitações de complemento de código e demarcação à inteligência artificial Claude. O projeto foi guiado dentro de um ambiente em meu notebook pessoal, com atividades realizadas por mim e meus colegas ao longo da disciplina. Para melhor fluxo de legibilidade, em algumas passagens a IA também foi utilizada para reescrever e adequar a minha escrita principal à solicitação em formato de relato a respeito do curso.

**Literatura selecionada**

- HODGKIN, A. L.; HUXLEY, A. F. A quantitative description of membrane current and its application to
  conduction and excitation in nerve. *The Journal of Physiology*, v. 117, n. 4, p. 500–544, 1952.
  DOI: [10.1113/jphysiol.1952.sp004764](https://doi.org/10.1113/jphysiol.1952.sp004764)

**Sobre a história do cálculo**

- HARTREE, D. R. A practical method for the numerical solution of differential equations.
  *Memoirs of the Manchester Literary and Philosophical Society*, v. 77, p. 91–107, 1932/33.
- THE PHYSIOLOGICAL SOCIETY. *Hodgkin and Huxley's modelling of the action potential*.
  [physoc.org](https://www.physoc.org/about-us/history-archives/historicalhighlights/hodgkin-and-huxleys-modelling-of-the-action-potential/)
- HUXLEY, A. F. The quantitative analysis of excitation and conduction in nerve. Nobel Lecture, 1963.
  [nobelprize.org](https://www.nobelprize.org/uploads/2018/06/huxley-lecture.pdf)
- University of Pennsylvania, Neurolab. *H&H Calculations* (com depoimento de A. L. Hodgkin).
  [sas.upenn.edu](https://www.sas.upenn.edu/LabManuals/BBB251/NIA/NEUROLAB/APPENDIX/EQUAT.HH/CALCULAT.HTM)
- MOORE, J. W. A personal view of the early development of computational neuroscience in the USA.
  *Frontiers in Computational Neuroscience*, v. 4, 2010.
  [frontiersin.org](https://www.frontiersin.org/articles/10.3389/fncom.2010.00020/pdf)
- BROWN, A. M. *A Companion Guide to the Hodgkin–Huxley Papers*. The Physiological Society.

**Material do curso**

- LOBOSCO, R. J. Notebooks de aula de Cálculo Numérico (UNIFESP).
  [github.com/rjlobosco/unifesp](https://github.com/rjlobosco/unifesp)
