from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import OpenAI
from langchain_community.callbacks import get_openai_callback
# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="yourusername",
#     password="yourpassword",
#     database="yourdatabase"
# )

# mycursor = mydb.cursor()

# sql = "SELECT * FROM customers"
# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for row in myresult:
#     print(row)

# mycursor.close()
# mydb.close()

# Load environment variables
os.environ ["OPENAI_API_KEY"] = "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"
load_dotenv()
def process_text(text):
    # Split the text into chunks using Langchain's CharacterTextSplitter
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    # Convert the chunks of text into embeddings to form a knowledge base
    embeddings = OpenAIEmbeddings()
    knowledgeBase = FAISS.from_texts(chunks, embeddings)
    
    return knowledgeBase
def main():
    st.title("EMADADGAR Query Desk 💬")
    
    pdf = st.file_uploader('Upload your PDF Document', type='pdf')
    # pdf = '/home/ubuntu/Desktop/CITS Prospectus Session 2023-24.pdf'
    
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        # Text variable will store the pdf text
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # Create the knowledge base object
        knowledgeBase = process_text(text)
        # query = input('Query:\n')
        
        query = st.text_input('Ask a question to the PDF')
        cancel_button = st.button('Cancel')
        
        if cancel_button:
            st.stop()
        
        if query:
            docs = knowledgeBase.similarity_search(query)
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type='stuff')
            
            with get_openai_callback() as cost:
                response = chain.run(input_documents=docs, question=query)
                # print(cost)
                # print(response)
                
            st.write(response)
            
            
if __name__ == "__main__":
    main()