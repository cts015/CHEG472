import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import base64
import os

# Load environment variables
load_dotenv()

# Function to convert an image file to a base64 encoded string
def encode_image_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Defining paths for image assets
bot_avatar_path = os.path.join('images', 'bot.png')
user_avatar_path = os.path.join('images', 'user.png')
app_icon_path = os.path.join('images', 'page_icon.png')

# Encoding images to base64 for HTML embedding
bot_avatar_base64 = encode_image_to_base64(bot_avatar_path)
user_avatar_base64 = encode_image_to_base64(user_avatar_path)
app_icon_base64 = encode_image_to_base64(app_icon_path)

# Configure Streamlit page settings
st.set_page_config(page_title="Scientific Text Mining", page_icon=f"data:image/png;base64,{app_icon_base64}", layout="wide")

# Function to read and concatenate text from PDF files
def extract_text_from_pdfs(pdf_list):
    combined_text = ""
    for pdf_file in pdf_list:
        reader = PdfReader(pdf_file)
        extracted_texts = [page.extract_text() for page in reader.pages]
        if not any(extracted_texts):  # Check if no text was extracted from any page
            st.warning(f"No text could be extracted from {pdf_file.name}. Consider using OCR.")
        combined_text += "".join(extracted_texts)
    return combined_text

# Split a large text into manageable chunks
def split_text_into_chunks(text, chunk_size=1000, overlap=200):
    if not text.strip():  # Check if text is empty or whitespace
        return []
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap, separator="\n")
    return text_splitter.split_text(text)

# Generate a vector store from text chunks
def create_vector_store_from_chunks(text_chunks):
    if not text_chunks:  # Check if the list is empty
        st.error("No text found in the PDFs or text is not extractable.")
        return None
    text_embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(text_chunks, text_embeddings)

# Setup the conversational retrieval chain
def initialize_conversational_chain(vector_store):
    if vector_store is None:  # Check if the vector store creation was unsuccessful
        return None
    llm = ChatOpenAI()
    memory_storage = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    return ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(), memory=memory_storage)

# Display the chat history in a visually appealing format
def render_chat_history(chat_history):
    if not chat_history:
        st.warning("No chat history to display.")
        return
    chat_css = """
    <style>
        .chat-container {
            display: flex;
            width: 100%;
            align-items: center;
            margin-bottom: 0.5rem;
        }
        .chat-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-size: cover;
            margin: 0 10px;
        }
        .chat-message {
            padding: 0.5rem 1rem;
            border-radius: 25px;
            border: 1px solid #eee;
            max-width: 60%;
        }
        .user-container {
            justify-content: flex-end;
        }
        .user-message {
            background-color: #FFDE59;
        }
        .bot-container {
            justify-content: flex-start;
        }
        .bot-message {
            background-color: #0CC0DF;
        }
    </style>
    """
    st.markdown(chat_css, unsafe_allow_html=True)

    for index, message in enumerate(reversed(chat_history)):
        if index % 2 == 0:
            st.markdown(
                f'<div class="chat-container user-container">'
                f'<div class="chat-message user-message">{message.content}</div>'
                f'<img src="data:image/png;base64,{user_avatar_base64}" class="chat-avatar">'
                f'</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="chat-container bot-container">'
                f'<img src="data:image/png;base64,{bot_avatar_base64}" class="chat-avatar">'
                f'<div class="chat-message bot-message">{message.content}</div>'
                f'</div>',
                unsafe_allow_html=True
            )


# Main layout and interaction containers
with st.container():
    st.markdown("""
    <style>
    .container {
        padding: 20px;
        background-color: #f8d7da;
        border: 2px solid black;
    }
    h1 {
        font-family: 'Caslon', serif; /* Fallback: Times New Roman or similar serif */
        font-size: 60px; /* Increased font size for the title */
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(f'<h1 style="display: inline-block; vertical-align: middle;"><img src="data:image/png;base64,{app_icon_base64}" style="width: 200px; height: 200px; border-radius: 25px; margin-right: 10px; vertical-align: middle;"> Scientific Text Mining</h1>', unsafe_allow_html=True)
    

with st.container():
    col2, col1 = st.columns([1.2, 5])

    with col1:
        st.subheader("Ask Questions")
        user_query = st.text_input("Your Prompt...", key="query_input")
        
        def process_user_query():
            if "conversation_chain" in st.session_state:
                chat_response = st.session_state['conversation_chain']({'question': user_query})
                st.session_state['query_response'] = chat_response

        send_query_button = st.button("Send", on_click=process_user_query)
        
        if "query_response" in st.session_state and send_query_button:
            render_chat_history(st.session_state['query_response']['chat_history'])

    with col2:
        st.subheader("Upload PDFs")
        uploaded_pdfs = st.file_uploader("", accept_multiple_files=True)
        process_pdfs_button = st.button("Process PDFs")

        if process_pdfs_button and uploaded_pdfs:
            with st.spinner("Processing PDFs..."):
                extracted_text = extract_text_from_pdfs(uploaded_pdfs)
                text_segments = split_text_into_chunks(extracted_text)
                text_vector_store = create_vector_store_from_chunks(text_segments)
                if text_vector_store:
                    st.session_state['conversation_chain'] = initialize_conversational_chain(text_vector_store)
