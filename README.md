# 💧 Controle de Níveis de Água

Sistema simples de monitoramento de um reservatório de água, executado no terminal. O programa exibe mensagens de alerta com **cores diferentes** conforme o nível de água, usando a biblioteca externa [`colorama`](https://pypi.org/project/colorama/).

Atividade da **Agenda 11 – Bibliotecas** | Desenvolvimento de Sistemas I | Curso Técnico em Desenvolvimento de Sistemas (ETEC)

**Autora:** Thaina Rodrigues de Almeida

---

## 🎯 Objetivo

Simular um ambiente real de monitoramento, em que cada leitura do reservatório é associada a uma situação e a uma cor, seguindo a progressão de risco:

| Nível   | Situação              | Cor      |
|---------|-----------------------|----------|
| Nível 1 | Muito baixo (crítico) | Vermelho |
| Nível 2 | Baixo                 | Amarelo  |
| Nível 3 | Médio                 | Verde    |
| Nível 4 | Alto                  | Ciano    |
| Nível 5 | Muito alto (alerta)   | Azul     |

## 🧩 Como o programa funciona

- Uma **lista** (`mensagens`) armazena a mensagem de cada nível.
- A função `definir_cor(nivel)` retorna a cor correspondente ao nível informado.
- A função `exibir_situacao(nivel)` imprime a mensagem do nível com a cor definida.
- Um laço `for` percorre uma lista de leituras simuladas (`leituras`), definidas no próprio código. Não há entrada de dados do usuário.
- Ao final, `Style.RESET_ALL` restaura o estilo padrão do terminal.

## 📁 Estrutura do projeto

```
controle-nivel-agua/
├── monitoramento_reservatorio.py
├── requirements.txt
└── README.md
```

## ▶️ Como executar

**Pré-requisito:** Python 3 instalado.

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/controle-nivel-agua.git
   cd controle-nivel-agua
   ```

2. Instale a dependência:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o programa:
   ```bash
   python monitoramento_reservatorio.py
   ```

## 🖥️ Exemplo de saída

Cada linha aparece no terminal com a cor do respectivo nível:

```
=== MONITORAMENTO DO RESERVATÓRIO ===

Leitura 1: Nível 3 - Médio                    (verde)
Leitura 2: Nível 2 - Baixo                    (amarelo)
Leitura 3: Nível 1 - Muito baixo (CRÍTICO)    (vermelho)
Leitura 4: Nível 2 - Baixo                    (amarelo)
Leitura 5: Nível 3 - Médio                    (verde)
Leitura 6: Nível 4 - Alto                     (ciano)
Leitura 7: Nível 5 - Muito alto (ALERTA)      (azul)
```

> Os textos entre parênteses acima indicam a cor exibida no terminal; eles não são impressos pelo programa.

## 🛠️ Tecnologias e conceitos utilizados

- Python 3
- Biblioteca externa `colorama` (instalada com `pip`)
- Listas, funções, estruturas condicionais e estruturas de repetição