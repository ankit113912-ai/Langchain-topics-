from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser


load_dotenv ()

prompt1 = PromptTemplate(
    template = 'Generate a detailed report on {topic}',
    input_variables = ['text']

)

prompt2 = PromptTemplate (

    template = ' Generate a 5 pointer summary from the following text \n {text}',
    input_variables = ['text']


)

model1 = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1 | model1 | parser | prompt2 | model1 | parser 

result = chain.invoke({ 'topic ' :'Unemployment in India '})

print(result )

chain.getgraph().print_ascii()












