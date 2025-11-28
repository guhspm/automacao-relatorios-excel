# Automação de Relatórios Corporativos com Python (Pandas + OpenPyXL) 📊🐍

## 📋 Sobre o Projeto
Este projeto é uma solução de **Engenharia de Dados e Automação de Processos (RPA)** desenvolvida para otimizar o setor financeiro/faturamento.

O script processa grandes volumes de dados brutos de inadimplência e pagamentos, cruza informações com relatórios analíticos externos e gera, automaticamente, **3 tipos de relatórios gerenciais** para múltiplas entidades (empresas) simultaneamente.

**Destaque Técnico:** Diferente de scripts simples de análise de dados, este projeto foca na **experiência do usuário final**, utilizando a biblioteca `openpyxl` para estilizar as planilhas (cores, bordas, fusão de células e auto-ajuste), entregando um arquivo pronto para apresentação executiva.

## 🚀 Funcionalidades
- **Processamento Multi-Entidade:** Identifica automaticamente as empresas presentes na base de dados e cria pastas/relatórios separados para cada uma.
- **Tratamento de Dados:** Normalização de strings, chaves de identificação e conversão de formatos (Data/Moeda).
- **Cruzamento de Bases (Data Merging):** Compara o "Previsto" (Sistema) com o "Realizado" (Relatório Analítico) para identificar divergências financeiras.
- **Excel Styling Avançado:**
    - Formatação condicional via código (Cores para cabeçalhos, totais, etc.).
    - Aplicação de bordas e alinhamentos.
    - Criação de linhas de "Total" automáticas.
    - Formatação de células como Texto ou Moeda (R$) nativamente.

## 🛠 Tecnologias Utilizadas
- **Python 3.10+**
- **Pandas:** Manipulação, limpeza e agregação de dados.
- **OpenPyXL:** Motor de geração e estilização de arquivos Excel (.xlsx).
- **Glob/OS:** Manipulação de sistema de arquivos e diretórios.

## 📂 Estrutura dos Relatórios Gerados
O script gera automaticamente:
1.  **Adimplentes e Inadimplentes:** Listagem completa separada por abas, já formatada.
2.  **Composição Final:** Relatório executivo cruzando faturamento esperado vs. realizado.
3.  **Resíduos (MNC < 20):** Relatório de exceções para valores residuais baixos, com consolidação por matrícula.

## ⚙️ Como Executar (Simulação)
Como os dados originais são confidenciais, incluí um script `gerar_dados_teste.py` que cria bases fictícias para demonstração.

1. Clone o repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
