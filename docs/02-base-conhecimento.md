# Base de Conhecimento

## Dados Utilizados


| Arquivo | Formato | Utilização no Finn |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores. Lembrar palavras chaves. |
| `perfil_investidor.json` | JSON | Personalizar a lógica usada nas respostas em dúvidas do usuário. |
| `produtos_financeiros.json` | JSON | Educar sobre os produtos adequados ao perfil do usuário. |
| `transacoes.csv` | CSV | Analisar padrão de gastos do usuário, utilizando-os de forma didática. |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

- Atualizei o produto financeiro de Multimercado para Imobiliários (FII)
- Modifiquei os detalhes do investimento mínimo e do público-alvo.
- Atualizei o perfil de investidor para 'Arrojado, com foco no longo prazo'

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existe a possibilidade de injetar os dados diretamente no prompt com Ctrl + c, Ctrl + v, ou carregar os arquivos via código, vide exemplo abaixo:

```pyhton
import pandas as pd
import json

# CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

# JSONs
with open('data/perfil_investidor.json', 'r', encoding= 'utf-8') as f:
    perfil = json.load(f)
with open('data/produtos_financeiros.json', 'r', encoding= 'utf-8') as f:
    produtos = json.load(f)
```
### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para uma solução simples, é possível "injetar" os dados em nosso prompt, garantindo assim, que o Finn tenho o contexto necessário. Porém em soluções robustas, a melhor maneira seria que esses daods fossem carregados por código dinamicamente, visando a flexibilidade do agente.

```Text
DADOS E PERFIL DO USUÁRIO (perfil_investidor.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "Arrojado, com foco no longo prazo",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

HISTORICO DE ATENDIMENTO DO USUÁRIO (historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

TRANSACOES DO USUÁRIO (transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

PRODUTOS DISPONIVEIS PARA ENSINO (produtos_financeiros.json):
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Imobiliários (FII)",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "7,81%",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil moderado que busca diversificação e renda recorrente mensal"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo abaixo, pega os dados originais, os sintetiza, e deixa apenas os dados mais relevantes para estudo de contexto, para assim otimizar o consumo de tokens.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Arrojado, visando longo prazo
- Objetivo: Construir reserva de emergência
- Reserva atual: R$ 10.000 (meta: R$ 15.000)

Resumo de Gastos:
- Moradia : R$ 1.380
- Alimentação : R$ 570
- Transporte : R$ 295
- Saúde : R$ 188
- Lazer : R$ 55,90
- Total de Despesas : R$ 2.488,90

Produtos Disponíveis Para Ensino:
- Tesouro Selic (baixo risco)
- CDB Liquidez Diária (baixo risco)
- LCI/LCA (baixo risco)
- Fundo Imobiliário - FII (baixo risco)
- Fundo de Ações (alto risco)
...
```
