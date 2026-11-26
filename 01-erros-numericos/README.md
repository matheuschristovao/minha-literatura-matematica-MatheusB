# 01 · Erros numéricos — Atividade I

**Arquivo:** [`atividade-1_erros-numericos-biofluidodinamica.ipynb`](atividade-1_erros-numericos-biofluidodinamica.ipynb)
**Autores:** Matheus Bueno Christovão (185302) e Luiz Ricardo Pereira Salles (187569)
**Aulas relacionadas (repositório da professora):** Aula 2/3 — Erros computacionais · Aula 4 — Bases numéricas

## Do que se trata

Estudo de como **truncamento, arredondamento e precisão de máquina** afetam resultados em
problemas simples de biofluidodinâmica. O notebook está dividido em cinco partes:

| Parte | Tema | O que é feito |
|---|---|---|
| A | Truncamento × arredondamento | 3 valores, 0 a 4 casas decimais, cálculo de $E_a$, $E_r$ e $E_\%$ |
| B | Pressão arterial | 10 medidas de PA sistólica: efeito da representação inteira sobre média e desvio-padrão |
| C | Hagen–Poiseuille | Sensibilidade da vazão $Q = \pi r^4 \Delta p / (8 \mu L)$ ao raio do tubo |
| D | Nanocateter | Erro geométrico, `float32` × `float64` e perda de significância por cancelamento (forma de Horner) |
| E | Síntese | Quadro-resumo em PNG e GIF animado variando o raio do nanocateter |

## Principais resultados

- O arredondamento gera erro sempre menor ou igual ao do truncamento ($E_a \le 10^{-n}/2$), e o truncamento é **enviesado**.
- Como $Q \propto r^4$, o erro relativo no raio aparece **multiplicado por 4** na vazão ($\Delta Q/Q \approx 4\,\Delta r/r$).
- Subtrair duas vazões quase iguais destrói algarismos significativos. A forma de Horner $t(4+t(6+t(4+t)))$ elimina a subtração crítica.

## Como executar

Abra no Google Colab ou no Jupyter e execute as células em ordem.
Dependências: `numpy`, `pandas`, `matplotlib`, `Pillow`.
