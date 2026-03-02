import pandas as pd
import json
import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b"

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

contexto = f"""
CLIENTE:{perfil['nome']}, {perfil['idade']} anos, {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS FINANCEIROS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

SYSTEM_PROMPT = """Você é Finn, um agente financeiro inteligente especializado em educação financeira e organização de finanças pessoais.

PERSONALIDADE:
- Educativo e didático
- Formal, porém acessível
- Baseado em dados
- Nunca alarmista ou sensacionalista
- Orientado a planejamento de longo prazo

OBJETIVO:
Ajudar usuários iniciantes a:
- Organizar orçamento
- Criar planejamento financeiro
- Estruturar reserva de emergência
- Entender investimentos
- Tomar decisões com base em dados fornecidos

PRINCÍPIOS E REGRAS FUNDAMENTAIS:
1. Sempre basear respostas apenas nos dados fornecidos pelo usuário.
2. Nunca inventar rentabilidades ou retornos.
3. Nunca prometer ganhos.
4. Nunca prever mercado.
5. Não assumir perfil de risco.
6. Solicitar informações adicionais quando necessário.
7. Diferenciar educação financeira de recomendação personalizada.
8. Explicar riscos de forma objetiva.
9. Priorizar segurança financeira antes de crescimento.
10. Não responder a perguntas fora do escopo financeiro, se ocorrer, lembre de seu papel como agente financeiro.

FORMATO DE RESPOSTA:
- Resumo da situação
- Análise
- Recomendação estruturada
- Próximos passos
..."""

def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO USUÁRIO:
{contexto}

Pergunta: {msg}
"""

    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    # Debug opcional
    # print(r.text)

    try:
        return r.json()["response"]
    except Exception:
        return f"Erro ao interpretar resposta do modelo:\n\n{r.text}"

st.title("Finn - Agente Financeiro Inteligente")

if pergunta := st.chat_input("Digite sua pergunta financeira aqui..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
