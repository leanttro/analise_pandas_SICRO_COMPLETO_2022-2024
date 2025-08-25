# Análise de Veículos Rodoferroviários (SICRO 2022-2024)

Este projeto foi desenvolvido durante o curso de **Python para Data Science** do SENAI e utiliza dados do sistema **SICRO (2022-2024)** para analisar os custos e preços de veículos rodoferroviários.  

O objetivo é explorar as variações de preço, entender os custos de posse e operação dos equipamentos e identificar padrões de mercado.

---

## ▶️ Como Executar no Google Colab

Você pode abrir e executar o projeto direto no Google Colab clicando no link abaixo:  

👉 [Abrir no Google Colab](https://colab.research.google.com/drive/1_IcdcP9mLREEp3wOduhzXz2OQHIm8VJ6?usp=sharing)

> Obs: é necessário fazer upload do arquivo `SICRO_COMPLETO_2022-2024.xlsx` para a área de arquivos do Colab.

---

## 📊 Visão Geral da Análise

A análise se concentra na família de veículos **VEÍCULO RODOFERROVIÁRIO**, dividida em duas categorias principais:

- **carro** → Carro controle ferroviário - 186 kW  
- **veiculo** → Veículo ferroviário para capina química com capacidade de 12.000 L - 115 kW  

O notebook explora estas áreas de dados:

### 🔹 Variação de Preços Semestrais
- Os preços finais médios (2022-2024) mostram:
  - **Queda acentuada** nos *carros controle ferroviários* no início de 2023.  
  - **Variação mais estável** nos *veículos para capina química*.  
  - **Aumento brusco** no preço médio final em todas as categorias entre 2022 e 2023, possivelmente relacionado a novos investimentos no setor.

### 🔹 Custos por Tipo de PEI
- A coluna **PEI** categoriza o estado operacional dos equipamentos.  
- A análise da soma total do preço final por PEI revelou:  
  - Equipamentos **parados (EST)** gastam **6 vezes mais** que os em produção (P) ou em movimento (DMT).  
- Histogramas de preços mostram:  
  - Maior concentração de veículos em faixas de preços mais baixas.  
  - **Outliers** com valores muito acima da média em todas as categorias.  

---

## 🛠️ Tecnologias Utilizadas

- **Python** → Linguagem de programação principal.  
- **Pandas** → Manipulação e análise de dados.  
- **Matplotlib & Seaborn** → Visualização dos dados.  
- **Google Colab** → Ambiente de desenvolvimento e apresentação da análise.  

---

## 📂 Estrutura do Projeto

- **SICRO_COMPLETO_2022-2024.xlsx** → Arquivo original com os dados do sistema SICRO.  
- **SICRO_COMPLETO_2022_2024_VEÍCULO_RODOFERROVIÁRIO.ipynb** → Google Colab com o código e as visualizações da análise.  
