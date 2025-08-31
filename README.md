# AskLAI - Agente de Despesa Pública [Transparência]  

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)  
![IBM Watson Orchestrate](https://img.shields.io/badge/IBM-Watson%20Orchestrate-054ADA?style=for-the-badge&logo=ibm&logoColor=white)  

Agente criado utilizando **IBM Watson Orchestrate** e consumido via **API REST em Python**.  
> ⚠️ **Aviso**  
> *Todo o projeto foi desenvolvido com dados públicos fornecidos pela transparência municipal, em conformidade com a **Lei de Acesso à Informação (LAI)**.*  
> *O Front-end é apenas um protótipo para exemplo de consumo da API em chatbot.*
---

## Tecnologias Utilizadas

- Python
- FastAPI
- IBM Watsonx Orchestrate

---

## Imagens

<img width="1336" height="858" alt="image" src="https://github.com/user-attachments/assets/5a29cdb0-0fb9-4f90-851b-f9766bfe5d92" />



---

## Endpoints

### 1. **GET `/api/chat/`** - Status da API
- **Resumo:** Verifica se a API está funcionando.
- **Resposta 200:** Retorna um JSON vazio `{}` indicando que o serviço está OK.

---

### 2. **POST `/api/chat/`** - Processa mensagem do agente
- **Resumo:** Envia mensagens para o agente especialista em transparência e recebe resposta estruturada.
- **Request Body:** `ChatRequestSchema`

```json
{
  "messages": "Qual o gasto da prefeitura em 2024?",
  "thread_id": "",
  "stream": false
}
```

## Schemas

### ChatRequestSchema
| Campo      | Tipo     | Obrigatório | Descrição                          |
|-----------|---------|------------|------------------------------------|
| messages  | string  | sim        | Mensagem a ser enviada ao agente  |
| stream    | boolean | não        | Se deve habilitar streaming       |
| thread_id | string  | não        | Identificador de thread (opcional)|

### ChatResponseSchema
| Campo       | Tipo     | Obrigatório | Descrição                  |
|------------|---------|------------|----------------------------|
| message    | string  | sim        | Resposta do agente         |
| thread_id  | string  | sim        | Identificador da thread    |
| status_msg | string  | sim        | Status da resposta (`OK`)  |
