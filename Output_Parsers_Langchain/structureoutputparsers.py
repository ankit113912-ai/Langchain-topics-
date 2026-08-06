from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser




load_dotenv()

# Define the model

llm = HuggingFaceEndpoint(

    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text - generation"

)

model = ChatHuggingFace(llm = llm)

schema = [
    ResponseSchema(name ='fact_1',description = 'Fact 1 about the topic  '),
    ResponseSchema(name ='fact_2',description = 'Fact 1 about the topic  '),
    ResponseSchema(name ='fact_3',description = 'Fact 1 about the topic  '),

]

parser = StructuredOutParser.from_responsea-schemas(schema)

template = PromptTemplate(
    template ='Give 3 fact about {topic} \n {format_instruction}',
    input_variables = ['topic']
    partial_variables = { ' format_instruction': parse.get_format_instruction()}
    )

chain = template | model | parser
prompt = template.invoke({'topic':'black hole'})


print(result)





