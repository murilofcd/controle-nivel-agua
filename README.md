# Sistema de Controle de Níveis de Água

Projeto desenvolvido para a disciplina de **Desenvolvimento de Sistemas I (DSI)** - **Agenda 11**.

O sistema simula o monitoramento em tempo real do nível de água de um reservatório, exibindo alertas visuais no terminal com cores personalizadas baseadas no grau de risco da situação.

---

## 📌 Funcionalidades

- **Monitoramento por Níveis:** Avalia 5 níveis distintos de capacidade do reservatório.
- **Alertas Coloridos:** Utiliza a biblioteca `colorama` para indicar visualmente a gravidade da situação.
- **Reset de Estilo:** Restaura as configurações padrão do terminal após a execução para evitar alterações no ambiente do usuário.

---

## 🎨 Tabela de Alertas e Cores

| Nível | Situação | Cor do Alerta |
| :---: | :--- | :---: |
| **1** | Muito baixo (crítico) | 🔴 Vermelho |
| **2** | Baixo | 🟡 Amarelo |
| **3** | Médio | 🟢 Verde |
| **4** | Alto | 🔵 Ciano |
| **5** | Muito alto (alerta) | 🟦 Azul |

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Biblioteca Externa:** [Colorama](https://pypi.org/project/colorama/) (para estilização de texto no terminal)

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina.

### 2. Instalar a biblioteca Colorama
No terminal ou prompt de comando, execute:
```bash
pip install colorama
