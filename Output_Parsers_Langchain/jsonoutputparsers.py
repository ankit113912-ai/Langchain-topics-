
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm = HuggingFaceEndpoint(

    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text - generation"
)

model = ChatHuggingFace(llm = llm)

template = PromptTemplate (
    template = 'Give me the name , age and of a fictional person \n {format_instuction}',
    input_varibales = [], 
    partial_variables= {'format_instruction':parser.get_format_instructions()}
)


chain = template | model | parser

result = chain.invoke ()

print (result)






