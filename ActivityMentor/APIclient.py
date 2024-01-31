import openai
import os
from jproperties import Properties
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import HumanMessage, BaseOutputParser
from langchain.memory import ConversationBufferMemory
import json

os.environ["OPENAI_API_KEY"] = "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"

"""interfaccia langchain per creare un agent che impementa un LLM preaddestrato di OpenAI.
Riceve in input le richieste dell'utente e la tabella Activity convertita in stringa"""

def copilot_chat_prompt(prompt_user, activities_string):
    
    class OutputParser(BaseOutputParser):
        """Parses the output of an LLM call to a comma-separated list."""
        
        def parse(self, text: str):
            """Parses the output of an LLM call."""
            return text.replace("\n", "\n")
        
    # Create a chat prompt template with system and human messages
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", """sei un analizzatore di tabelle contententi attività ed un activities mentor."""),
        ("human", f"{prompt_user}\n{activities_string}")
    ])
    
    # Chain the chat prompt with an OpenAI model and the output parser
    chain = chat_prompt | ChatOpenAI(model_name="gpt-3.5-turbo") | OutputParser()
    
    # Invoke the chain to process the chat prompt and return the result
    return chain.invoke({})
    
    
    




