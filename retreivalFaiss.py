from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
# import google.generativeai as genai
from langchain.prompts import PromptTemplate
import os


def get_conversational_chain():
    # Define a prompt template for asking questions based on a given context
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details,
    if the answer is not in the provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    # Initialize a ChatGoogleGenerativeAI model for conversational AI
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

    # Create a prompt template with input variables "context" and "question"
    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Load a question-answering chain with the specified model and prompt
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question,key):

    os.environ["GOOGLE_API_KEY"]=key

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=key)
    new_db = FAISS.load_local("db_ayurveda", embeddings, allow_dangerous_deserialization=True)

    # Perform similarity search in the vector database based on the user question
    docs = new_db.similarity_search(user_question, k=3)

    # Obtain a conversational question-answering chain
    chain = get_conversational_chain()

    # Use the conversational chain to get a response based on the user question and retrieved documents
    response = chain(
        {"input_documents": docs, "question": user_question}, return_only_outputs=True
    )

    # Print the response to the console
    return response["output_text"]