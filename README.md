# Pipeline ETL com Python - Santander Dev Week 2023

## 🎯 Objetivo
Este projeto simula um pipeline de dados para um banco. O objetivo é ler uma base de clientes, processar ofertas personalizadas baseadas no limite de crédito e exportar os resultados, contornando a indisponibilidade da API original através de arquivos CSV.

## 🔄 O Fluxo ETL Aplicado
- **Extract (Extração)**: Leitura de arquivo CSV com dados cadastrais e financeiros.
- **Transform (Transformação)**: Lógica de negócio em Python para segmentação de marketing baseada em limite de crédito.
- **Load (Carga)**: Geração de um novo arquivo consolidado pronto para uso em ferramentas de BI.

## 🛠️ Tecnologias
- **Python**
- **Pandas**
