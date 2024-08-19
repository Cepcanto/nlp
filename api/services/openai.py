# open AI library
import openai

# Enviroment Variables libraries
import os
from dotenv import load_dotenv

# load enviroment variables from the .env file
load_dotenv()

# configure the OPENAI API Key 
openai.api_key = os.getenv("OPENAI_API_KEY")
 
# Call OPENAI Chat Completion API and returns a summary of the content of a Web Page
def getSummary(content):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um especialista em resumo de texto. Responda em português."},
                {"role": "user", "content": content}
            ]
        )
        print(f"Resposta da API: {response}")
        return response['choices'][0]['message']['content']

    except openai.error.OpenAIError as e:
        # Captura erros específicos da API
        print(f"Erro na API do OpenAI: {e}")
        return None
    
    except Exception as e:
        # Captura qualquer outro tipo de erro
        print(f"Ocorreu um erro inesperado: {e}")
        return None


# Call OPENAI Chat Completion API and returns an answer for a question, based on the content of a Web Page
def getAnswer(content, question):    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um especialista que sabe responder perguntas com base no texto. Responda em português."},
            {"role": "assistant", "content": f'Com base no texto: "{content}". Responda as perguntas.'},
            {"role": "user", "content": question}
        ]
    )
    
    return response['choices'][0]['message']['content']    
