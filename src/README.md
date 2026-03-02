# Passo a Passo de Execução


## Setup do Ollama 

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull gpt-oss

# 3. Testar se funciona
ollama run gpt-oss "Olá!"
```

## Código Completo

Todo código-fonte está no arquivo `App.py`

## Como Rodar

```bash
# 1. Instalar dependências
pip install stramlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 3. Rodar a aplicação
streamlit run .\src\App.py
```
