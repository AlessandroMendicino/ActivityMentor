import openai
import os
from jproperties import Properties
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
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
    
    
    






"""
def simple_chat_prompt():
    
    
    def json_to_string():
        with open('storage.json' , 'r') as file:
            contenuto_json = json.load(file)
            stringa_json = json.dumps(contenuto_json, indent=2) 
        return stringa_json
    
    text = json_to_string()
    
    #class CommaSeparatedListOutputParser(BaseOutputParser):
        #Parse the output of an LLM call to a comma-separated list.
        #def parse(self, text: str):
            #Parse the output of an LLM call.
            #return text.strip().split(", ")
    human_template = "{text}"

    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", sei un assistente virtuale che analizza e descrive le attività svolte nei mesi di studio e lavoro di un utente stagista 
                    e poi fornisce suggerimenti per continuare l'attività di stage. 
                    Riceverai dall'utente un filejson convertito in stringa, 
                    c'è una colonna data ed una colonna attività, dalle tuple puoi ricavare a seconda del mese quali attività sono state svolte
                    il tuo compito è quello di analizzare tutte le attività e poi fornire una brevissima descrizione ed in modo molto sintetico
                    cosa ha svolto l'utente a seconda del mese.
                    Successivamente in base all'analisi fornisci un consiglio di roadmap d'apprendimento in base agli argomenti studiati nei mesi 
                    oppure dei tool alternativi a quelli già studiati ed utili al lavoro analizzando sempre le attività. 
                    Sottolinando anche quali nuovi argomenti possono essere più utili da studiare e quali no, e come perfezionare le skill personali e con quali esercitazioni.),
        ("human", human_template),
    ])
    chain = chat_prompt | ChatOpenAI(model_name="gpt-3.5-turbo") #| CommaSeparatedListOutputParser()
    return (chain.invoke({"text":text})) """