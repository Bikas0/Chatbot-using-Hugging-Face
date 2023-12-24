from transformers import pipeline, Conversation
import gradio as gr

chatbot = pipeline(model="facebook/blenderbot-400M-distill")

message_list = []
response_list = []


def Chatbot(message, history):
    conversation = Conversation(text=message, past_user_inputs=message_list, generated_responses=response_list)
    conversation = chatbot(conversation)
    return conversation.generated_responses[-1]


bikasChatbot = gr.ChatInterface(Chatbot, title="Bikas Chatbot", description="Enter yout Text")
bikasChatbot.launch(share=True)
