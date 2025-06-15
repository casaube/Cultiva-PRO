---
<<<<<<< HEAD
title: Cultiva Pro
emoji: 🌱
colorFrom: green
colorTo: blue
sdk: gradio
app_file: app.py
sdk_version: 5.34.0
---
# Cultiva-PRO

Chatbot para produtores rurais utilizando Google Gemini e Gradio, desenvolvido em Python.
Este projeto foi resultado da participação da imersão da Alura com o Google.

Link: https://c5ec38a044869c0a13.gradio.live/

# Chatbot Agro IA com Gemini e Gradio

Este é um chatbot de assistência para pequenos produtores rurais, construído com Python, a API Google Gemini e a interface Gradio.

## Descrição

O chatbot é capaz de responder a perguntas comuns sobre:
- Plantio (geral)
- Pragas e doenças (identificação básica e controle inicial)
- Adubação (conceitos básicos)
- Coleta de amostras (solo, folha - princípios gerais)
- Interpretação básica de laudos simples (pH, N, P, K).

## Como Usar

1.  **Clone ou Baixe este Repositório (ou apenas o arquivo .ipynb).**

2.  **Requisitos/Dependências:**
    Você precisará das seguintes bibliotecas Python. Você pode instalá-las usando pip:
    ```bash
    pip install google-generativeai gradio
    ```
    (Opcional: Se você quiser, pode criar um arquivo `requirements.txt` no seu repositório com estas duas linhas e instruir os usuários a usar `pip install -r requirements.txt`)

3.  **Configuração da Chave de API do Google Gemini:**
    * **IMPORTANTE:** Este projeto requer uma chave de API do Google Gemini.
    * **Se estiver rodando no Google Colab:**
        1.  Obtenha sua chave de API no [Google AI Studio](https://aistudio.google.com/app/apikey).
        2.  No Colab, clique no ícone de chave (Secrets) no menu à esquerda.
        3.  Adicione um novo secret com o nome `GOOGLE_API_KEY` e cole sua chave no campo "Value".
        4.  Certifique-se de que "Notebook access" está habilitado para este secret.
    * **Se estiver rodando localmente (fora do Colab):**
        Você precisará modificar o código para carregar a API Key de uma variável de ambiente ou de um arquivo de configuração seguro. Não coloque sua chave diretamente no código!
        Exemplo (usando variável de ambiente):
        ```python
        import os
        API_KEY = os.environ.get('GOOGLE_API_KEY')
        ```
        E então você precisaria definir a variável de ambiente `GOOGLE_API_KEY` no seu sistema.

4.  **Executando o Chatbot (no Google Colab):**
    * Abra o arquivo `.ipynb` no Google Colab.
    * Execute a célula que instala as bibliotecas (se houver).
    * Execute a célula principal do código do chatbot.
    * Um link público do Gradio (terminado em `.gradio.live`) aparecerá no output da célula. Clique nele para abrir a interface do chatbot no seu navegador.

## Exemplo de Interface
![Interface do Chatbot](images/Interface.png "Demonstração da Interface")


## Licença
Apache License
Version 2.0
=======
title: CultivaMaisPro
emoji: 😻
colorFrom: purple
colorTo: green
sdk: gradio
sdk_version: 5.34.0
app_file: app.py
pinned: false
license: mit
short_description: Cultiva Mais Pro chatbot que ajuda produtores rurais
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
>>>>>>> 858d64fe2cd4a3c9a0d3e76f4cc21496340d050f
