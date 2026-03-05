# Limpeza de Dados de Clientes (Python + Pandas)

Projeto de **tratamento e padronização de dados** em uma base de clientes, com foco em qualidade de dados para análise.

##  O que esse projeto faz
- Remove coluna desnecessária e linha específica
- Padroniza textos:
  - `nome` em Title Case
  - `endereco` em minúsculo
  - `estado` em maiúsculo
- Trata valores nulos:
  - remove registros sem `cpf`
  - preenche `estado` e `endereco` quando ausentes
  - corrige `idade` usando a média quando necessário
- Converte `data` para formato datetime (`dd/mm/aaaa`)
- Remove duplicidades com base em `cpf`
- Exporta base tratada para CSV

##  Estrutura do projeto
🧰 Tecnologias

Python

Pandas

👩‍💻 Autora

Paloma Marques
