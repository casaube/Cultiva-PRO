import gradio as gr

# --- Passo 1: Configuração da API Key do Google ---
# O código tentará buscar a chave dos "Secrets" do Hugging Face Spaces.
API_KEY = os.environ.get('GOOGLE_API_KEY')

if not API_KEY:
    raise ValueError("Chave API do Google (GOOGLE_API_KEY) não encontrada. Configure-a nos Secrets do seu Space no Hugging Face.")

try:
    genai.configure(api_key=API_KEY)
    print("API Key do Google configurada com sucesso.")
except Exception as e:
    print(f"Erro ao configurar a API Key do Google: {e}")
    raise

# --- Passo 2: Configuração do Modelo Generativo Gemini ---
try:
    model = genai.GenerativeModel('gemini-1.0-pro')
    print("Modelo Generativo Gemini carregado com sucesso.")
except Exception as e:
    print(f"Erro ao carregar o modelo GenerativeModel: {e}")
    raise

# --- Passo 3: Instrução do Sistema e Início do Chat ---
system_instruction = """Você é um assistente virtual de suporte rápido para pequenos produtores rurais.
Sua função é responder de forma clara, objetiva e prática a dúvidas comuns sobre:
- Plantio (geral)
- Pragas e doenças (identificação básica e controle inicial)
- Adubação (conceitos básicos)
- Coleta de amostras (solo, folha - princípios gerais)
- Interpretação básica de laudos simples (pH, N, P, K).
Baseie suas respostas em conhecimentos agronômicos gerais e recomende sempre buscar um profissional agrônomo para orientações, pois suas respostas são apenas para consulta.
Recomendações agronômicas e de manejo devem ser feitas por um profissional.
Se não souber a resposta ou a pergunta for muito complexa/específica, diga que a dúvida necessita de avaliação profissional no local.
Seja encorajador e use linguagem acessível."""

try:
    chat_global = model.start_chat(history=[
        {"role": "user", "parts": [system_instruction]},
        {"role": "model", "parts": ["Ok, compreendi. Estou pronto para ajudar os produtores rurais."]}
    ])
    print("Chat com o modelo iniciado com sucesso.")
except Exception as e:
    print(f"Erro ao iniciar o chat com o modelo: {e}")
    raise

# --- Passo 4: Função de Resposta para o Gradio ---
def chatbot_response(message, history):
    try:
        response = chat_global.send_message(message)
        return response.text
    except Exception as e:
        print(f"Erro ao enviar mensagem para o Gemini: {e}")
        error_text = str(e).lower()
        if "block_reason" in error_text:
            return "Sua pergunta não pôde ser processada devido às políticas de segurança de conteúdo. Por favor, reformule sua pergunta."
        return "Desculpe, ocorreu um erro inesperado ao processar sua pergunta. Verifique os logs para mais detalhes."

# --- Passo 5: Criação da Interface com Gradio ---
iface = gr.ChatInterface(
    fn=chatbot_response,
    title="Cultiva Pro (Chatbot para o Agro)",
    description="Assistente virtual para pequenos produtores rurais. Faça suas perguntas sobre plantio, pragas, adubação e mais.",
    chatbot=gr.Chatbot(height=500),
    textbox=gr.Textbox(placeholder="Digite sua pergunta aqui...", container=False, scale=7),
    examples=[
        ["Como faço para preparar o solo para o plantio de milho?"],
        ["Quais são os sinais de que minhas plantas estão com deficiência de nitrogênio?"],
        ["Como posso controlar pulgões de forma natural?"],
        ["Qual o pH ideal do solo para café?"]
    ],
    theme="soft",
    retry_btn="Tentar Novamente",
    undo_btn="Desfazer",
    clear_btn="Limpar"
)

# --- Passo 6: Lançar a Interface ---
iface.launch()