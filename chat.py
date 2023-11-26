from langchain.llms import OpenAI
import gradio as gr
import rag

openai_api_key='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'
llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

def proccess(_input):
   return llm(_input)

with gr.Blocks() as demo:
    chain = rag.createChain();
    print("Bem-vindo ao Chatbot! (Digite 'sair' para sair)")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="message")
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message =  chain.stream(msg)
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

def main():
    demo.launch()


if __name__ == "__main__":
    main()