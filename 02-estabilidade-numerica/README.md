# 02 · Estabilidade numérica e overflow — Atividade II

**Arquivo:** [`atividade-2_estabilidade-overflow-couette.ipynb`](atividade-2_estabilidade-overflow-couette.ipynb)
**Autores:** Matheus Bueno Christovão (185302) e Luiz Ricardo Pereira Salles (187569)

## Do que se trata

Simulação do **escoamento de Couette transiente** pela equação da difusão de quantidade de movimento

$$\frac{\partial u}{\partial t} = \nu \frac{\partial^2 u}{\partial y^2}$$

discretizada por **Euler explícito no tempo e diferenças finitas centrais no espaço**:

$$u_i^{n+1} = u_i^{n} + r\,(u_{i+1}^{n} - 2u_i^{n} + u_{i-1}^{n}), \qquad r = \frac{\nu\,\Delta t}{\Delta y^2}$$

O objetivo é relacionar o passo de tempo com a estabilidade do método e com o *overflow* em `float32` e `float64`.

## Estrutura do notebook

0. Configuração do ambiente
1. Verificação analítica da estabilidade ($r \le 1/2$)
2. Detecção de *overflow* (`np.errstate(over="raise")`)
3. Interpretação física: velocidades acima de $U$ não têm sentido físico
4. Capacidade de representação: `float32` × `float64` e fator de amplificação $G_m$
5. Refinamento da malha (21 → 41 pontos)
6. Verificação contra o perfil estacionário $u(y) = U(1 - y/H)$
7. Conclusão

## Principais resultados

- Com $r = 0{,}80$ a solução sai do intervalo físico já no **passo 3**. O *overflow* só aparece no passo 121 (`float32`) ou 917 (`float64`).
- **Instabilidade e overflow são fenômenos diferentes:** trocar para `float64` não corrige nada, só adia o erro.
- Refinar a malha **piora** a restrição, porque $\Delta t_{max} = \Delta y^2/(2\nu)$ cai com o quadrado de $\Delta y$.
- Na configuração estável, o erro final contra a solução estacionária foi $E_\infty \approx 1{,}6\times10^{-9}$ m/s.

## Como executar

Dependências: `numpy`, `pandas`, `matplotlib`.
