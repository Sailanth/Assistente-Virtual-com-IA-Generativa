# Avaliação e Métricas




**Testes estruturados:** Você define perguntas e respostas esperadas;


---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |



---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** R$ 570,00 (Valor baseado no `transacoes.csv`)
- **Resultado:** [x] Correto  [ ] Incorreto
  
<img width="1234" height="830" alt="image" src="https://github.com/user-attachments/assets/905993a8-6e16-40d2-ae7d-116407dd5a98" />

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [x] Correto  [ ] Incorreto

<img width="1234" height="830" alt="image" src="https://github.com/user-attachments/assets/bf988717-2bf8-41b5-9cf6-122ae352c6c1" />
<img width="1234" height="830" alt="image" src="https://github.com/user-attachments/assets/99eb50ca-098d-4d91-9ca0-7ba75e6f7f21" />
<img width="1234" height="315" alt="image" src="https://github.com/user-attachments/assets/d1b2cd3c-dfb7-495d-8537-c2fd6ba2ea9d" />

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que não pode responder a pergunta fora de escopo financeiro
- **Resultado:** [x] Correto  [ ] Incorreto

<img width="1234" height="830" alt="image" src="https://github.com/user-attachments/assets/5632fdb6-3b1a-46ea-8e65-a0dd0e0b2ad8" />


### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação em sua fonte de dados
- **Resultado:** [x] Correto  [ ] Incorreto


<img width="1234" height="830" alt="image" src="https://github.com/user-attachments/assets/a61bbda5-1e84-4857-8526-40309f8630a4" />

---
## Formulário de Feedback
**Quantitativo:**

| Métrica | Pergunta | Nota (1-5) |
|---------|----------|------------|
| Assertividade | "A resposta respondeu sua pergunta?" | 5 |
| Segurança | "O agente evitou inventar informações?" | 5 |
| Coerência | "A resposta faz sentido para o perfil do cliente?" | 5 |


## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O agente agiu conforme sua lista de principios e regras, logo, teve o resultado esperado em todas as questões.


**O que pode melhorar:**
- Tempo de resposta
- Ser mais flexivel em suas respostas, "menos engessado".
- Informar melhor ao usuário que isso não é uma recomendação direta de investimento, tendo mais um perfil didático sobre as sugestões.

---
