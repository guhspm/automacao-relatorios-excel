---

### 5. O Script Gerador de Dados Fictícios (`gerar_dados_teste.py`)
Esse é o "pulo do gato". Para quem visitar seu GitHub ver o código funcionando, você precisa criar arquivos falsos que tenham as mesmas colunas que seu código espera (`Empresa`, `Título Relac.`, etc.).

Crie o arquivo `gerar_dados_teste.py` na raiz do projeto e cole o código abaixo. Eu fiz ele compatível com o código limpo que te mandei antes.

```python
import pandas as pd
import os
import random
from datetime import datetime

# Configuração
ANO = 2023
MES = 10
MES_STR = "10"
PASTA_ANALITICO = "relatorios_analiticos"
OS_makedirs = os.makedirs
OS_makedirs(PASTA_ANALITICO, exist_ok=True)

# Lista de Empresas Fictícias baseadas no seu MAPA
EMPRESAS = ['PBH', 'PBHAT', 'PBHBL'] 
MAPA_REVERSO = {'PBH': 'PBH', 'PBHAT': 'ATIVOS', 'PBHBL': 'BELOTUR'}

print("--- Gerando Dados Fictícios para Teste ---")

# 1. Gerar Arquivo Principal: "Adimplentes e Inadimplentes.csv"
dados = []
for emp in EMPRESAS:
    for i in range(50): # 50 linhas por empresa
        situacao = random.choice(['LQ', 'LS', 'AB']) # Liquidado, Saldo, Aberto
        dados.append({
            'Empresa': emp,
            'Título Relac.': f"TR{random.randint(1000,9999)}",
            'Título': f"T{random.randint(10000,99999)}",
            'Vencimento': f"{random.randint(1,30):02d}/{MES_STR}/{ANO}",
            'Nº Nota': f"NF{random.randint(500,900)}",
            'Contrato': f"CTR{random.randint(1000,2000)}",
            'Competência': 'OUTUBRO',
            'Ano': ANO,
            'Tipo': 'MENSALIDADE',
            'Ident. Cliente': f"ID{random.randint(100,200)}",
            'CNPJ/CPF': f"{random.randint(10000000000, 99999999999)}",
            'Nome Cliente': f"Cliente Fictício {i}",
            'Valor': f"{random.uniform(100, 5000):.2f}".replace('.',','),
            'Sit.': situacao,
            'Matrícula': f"{random.randint(1000,9999)}/0"
        })

df_main = pd.DataFrame(dados)
df_main.to_csv(f"Adimplentes e Inadimplentes - Dummy.csv", sep=';', index=False, encoding='utf-8-sig')
print("-> Arquivo principal 'Adimplentes e Inadimplentes - Dummy.csv' gerado.")

# 2. Gerar Relatórios Analíticos (Excel) para cada empresa
# O código espera: SIGLA*Relatório Analítico*YYYY_MM.xlsx
for emp in EMPRESAS:
    sigla = MAPA_REVERSO.get(emp)
    if not sigla: continue
    
    nome_arquivo = f"{sigla} - Relatório Analítico - {ANO}_{MES_STR}.xlsx"
    caminho = os.path.join(PASTA_ANALITICO, nome_arquivo)
    
    # Criar dados compatíveis com o código principal
    analitico_data = []
    # Pegar algumas notas do arquivo principal para dar "match"
    subset = df_main[(df_main['Empresa'] == emp) & (df_main['Sit.'] == 'LQ')]
    
    for _, row in subset.iterrows():
        analitico_data.append({
            'CONTRATO': row['Contrato'],
            'Nº NOTA': row['Nº Nota'],
            'TITULO': row['Título Relac.'], # Para cruzar chave
            'VENCIMENTO': row['Vencimento'],
            'TIPO DE COBRANÇA': 'MENSALIDADE',
            'MNC': float(row['Valor'].replace(',','.')) + random.choice([0, 0.01, -0.01]), # Pequena variação
            'MNC < 20,00': 0
        })
    
    # Adicionar alguns aleatórios (que não existem na base principal)
    analitico_data.append({
        'CONTRATO': 'CTR9999', 'Nº NOTA': 'NF999', 'TITULO': 'TR9999', 
        'VENCIMENTO': f"15/{MES_STR}/{ANO}", 'TIPO DE COBRANÇA': 'EXTRA', 
        'MNC': 150.00, 'MNC < 20,00': 0
    })

    df_an = pd.DataFrame(analitico_data)
    
    # O código espera abas específicas para a parte de Resíduos (MENSALIDADES/COPART)
    # Vamos criar abas dummies também
    residuos_cols = {
        4: 'CARTAO_UNIMED', 6: 'MATRICULA_BENEF', 7: 'CONTRATO', 
        28: 'Retorno_Vl_NC', 40: 'CODIGO_VERBA', 42: 'CPF', 
        43: 'Vl_Minimo_MNC', 44: 'NOME_COMPLETO_TITULAR'
    }
    # Criar dataframe vazio com colunas suficientes (até índice 44)
    df_res = pd.DataFrame(columns=[i for i in range(50)])
    
    # Adicionar uma linha de resíduo
    linha = [None] * 50
    linha[4] = "00012345600012300" # Cartão
    linha[6] = "1234/0" # Matricula
    linha[7] = "CTR1001"
    linha[28] = 15.50 # Valor NC
    linha[40] = "21U1" # Verba
    linha[42] = "11122233344"
    linha[43] = "S" # Flag Minimo
    linha[44] = "TITULAR TESTE"
    df_res.loc[0] = linha
    
    # Salvar Excel com múltiplas abas e cabeçalho na linha 4 (skiprows=3 no código principal)
    with pd.ExcelWriter(caminho) as writer:
        # Aba Principal (Faturamento)
        df_an.to_excel(writer, index=False, startrow=3) 
        # Abas de Resíduos
        df_res.to_excel(writer, sheet_name='MENSALIDADES', index=False, header=False, startrow=4)
        df_res.to_excel(writer, sheet_name='COPART', index=False, header=False, startrow=4)

    print(f"-> Analítico gerado: {nome_arquivo}")

print("\nConcluído! Agora rode o 'src/main.py' para testar.")
