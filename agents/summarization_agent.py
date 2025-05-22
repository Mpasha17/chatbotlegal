"""
Summarization Agent Module

This module is responsible for extracting key explanations from complex legal topics
and converting them into plain, easy-to-understand language while preserving accuracy.
"""

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_mistralai import ChatMistralAI
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_summarizer_chain():
    """
    Create a chain for summarizing legal information into simple language.
    
    Returns:
        A LLMChain object configured for legal summarization
    """
    try:
        # Initialize the LLM
        llm = ChatMistralAI(
            model="mistral-large-latest",
            temperature=0,
            max_retries=2,   
              )
        
        # Create the prompt template
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
                    You are a legal assistant chatbot helping users understand Indian legal procedures and corporate laws. 
                    Your task is to read complex legal information and summarize it in a clear and concise way, suitable for a non-lawyer.

                    Instructions:
                    - Use plain, everyday language without legal jargon.
                    - Keep the response brief (under 150-200 words or 4 bullet points).
                    - Focus only on what's relevant to the user's question.
                    - Ensure accuracy — do not oversimplify or invent information.
                    - If the answer involves steps or procedures, present them in numbered or bulleted format.

                    Example:
                    Context: Legal procedures for filing a lawsuit in India
                    Question: What are the steps involved in filing a lawsuit in India?
                    Answer:
                    - Prepare the necessary documents and evidence.
                    - File a petition in the appropriate court.
                    - Send a legal notice to the opposing party.
                    - Attend court hearings and follow the process.

                    Now summarize the following:.

            
            Context:
            {context}
            
            Question:
            {question}
            
            Simplified Answer:"""
        )
        
        # Create and return the chain
        summarizer_chain = LLMChain(llm=llm, prompt=prompt)
        logger.info("Summarizer chain created successfully")
        return summarizer_chain
    
    except Exception as e:
        logger.error(f"Error in create_summarizer_chain: {str(e)}")
        raise

def summarize_answer(docs, question):
    """
    Summarize legal information into a simple, understandable answer.
    
    Args:
        docs: List of document chunks retrieved by the Query Agent
        question: The user's original question
        
    Returns:
        A simplified answer to the user's question
    """
    try:
        logger.info(f"Summarizing answer for question: {question}")
        
        # Combine the context from all documents
        combined_context = "\n\n".join(doc.page_content for doc in docs)
        logger.info(f"Combined context length: {len(combined_context)} characters")
        
        # Create the summarizer chain
        summarizer_chain = create_summarizer_chain()
        
        # Generate the response
        response = summarizer_chain.run(context=combined_context, question=question)
        logger.info("Answer summarization completed")
        
        return response
    
    except Exception as e:
        logger.error(f"Error in summarize_answer: {str(e)}")
        raise