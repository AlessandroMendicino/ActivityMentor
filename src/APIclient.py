import openai
import os
from rich.console import Console
from jproperties import Properties
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import HumanMessage, BaseOutputParser
from langchain.memory import ConversationBufferMemory
 
os.environ["OPENAI_API_KEY"] = "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"


def simple_chat_prompt(text):
    
    class CommaSeparatedListOutputParser(BaseOutputParser):
        """Parse the output of an LLM call to a comma-separated list."""
        def parse(self, text: str):
            """Parse the output of an LLM call."""
            return text.strip().split(", ")
    human_template = "{text}"
   
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", """sei un assistente virtuale che analizza e descrive le attività svolte nei mesi di studio e lavoro di un utente stagista 
                    e poi fornisce suggerimenti per continuare l'attività di stage. 
                    Riceverai dall'utente un filejson convertito in stringa, 
                    c'è una colonna mese ed una colonna attività, dalle tuple puoi ricavare a seconda del mese quali attività sono state svolte
                    il tuo compito è quello di analizzare tutte le attività e poi fornire una brevissima descrizione ed in modo molto sintetico
                    cosa ha svolto l'utente a seconda del mese.
                    Successivamente in base all'analisi fornisci un consiglio di roadmap d'apprendimento in base agli argomenti studiati nei mesi 
                    oppure dei tool alternativi a quelli già studiati ed utili al lavoro analizzando sempre le attività. 
                    Sottolinando anche quali nuovi argomenti possono essere più utili da studiare e quali no, e come perfezionare le skill personali e con quali esercitazioni."""),
        ("human", human_template),
    ])
    chain = chat_prompt | ChatOpenAI(model_name="gpt-4", temperature=0.3) | CommaSeparatedListOutputParser()
    return (chain.invoke({"text":text}))