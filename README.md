# 🧹 Limpeza e Tratamento de Dados de Clientes — Python + Pandas

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

Projeto de **tratamento, padronização e qualidade de dados** em uma base de clientes, cobrindo desde limpeza básica até tratamento de outliers e inconsistências.

---

## 📋 Sobre o Projeto

Este projeto aplica técnicas de **Data Cleaning** em uma base real de clientes, preparando os dados para análises confiáveis. O trabalho foi dividido em três frentes principais:

- **Limpeza e Padronização** — formatação de textos, valores nulos e duplicatas
- **Tratamento de Outliers** — identificação e correção de valores fora do padrão
- **Inconsistências** — detecção e resolução de dados contraditórios ou inválidos

---

## 🗂️ Estrutura do Projeto

```
📁 Limpeza-de-Dados-de-Clientes-Python-Pandas-
│
├── 📄 Limpeza de dados.py         → Limpeza e padronização geral
├── 📄 Outliers.py                 → Tratamento de outliers
├── 📄 Inconsistencias.py          → Correção de inconsistências
├── 📄 clientes_corrigidos.csv         → Base de dados tratada (output)
└── 📄 README.md
```

---

## 🔧 O que foi feito

### 🧽 Limpeza e Padronização
- Remoção de colunas desnecessárias e linhas específicas
- Padronização de textos:
  - `nome` → Title Case
  - `endereco` → minúsculo
  - `estado` → maiúsculo
- Tratamento de valores nulos:
  - Remoção de registros sem `cpf`
  - Preenchimento de `estado` e `endereco` ausentes
  - Correção de `idade` usando a média
- Conversão da coluna `data` para formato datetime (`dd/mm/aaaa`)
- Remoção de duplicatas com base em `cpf`

### 📊 Tratamento de Outliers
- Identificação de valores atípicos em colunas numéricas (como `idade` e `salario`)
- Uso do método IQR (Intervalo Interquartil) para detectar outliers
- Substituição dos valores extremos por limites ou média da distribuição

### ⚠️ Inconsistências
- Detecção de dados contraditórios (ex: datas inválidas, idades negativas)
- Correção de formatações incorretas em campos como CPF, telefone e e-mail
- Validação e padronização de categorias com variações de escrita

---

## 💡 Técnicas Utilizadas

| Técnica | Aplicação |
|---|---|
| `fillna()` / `dropna()` | Tratamento de nulos |
| `astype()` | Conversão de tipos |
| `str.title()`, `str.lower()`, `str.upper()` | Padronização de texto |
| `drop_duplicates()` | Remoção de duplicatas |
| `apply()` + `lambda` | Transformações customizadas |
| IQR (Q1, Q3) | Identificação de outliers |
| `pd.to_datetime()` | Conversão de datas |

---

## 🚀 Como Executar

**Pré-requisitos:**
- Python 3.x
- Biblioteca Pandas instalada

```bash
pip install pandas
```

**Executar os scripts:**
```bash
python "Limpeza de dados.py"
python Outliers.py
python Inconsistencias.py
```

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)

---

## 👩‍💻 Autora

**Paloma Marques**

[![GitHub](https://img.shields.io/badge/GitHub-Palomamars01-181717?logo=github)](https://github.com/Palomamars01)
