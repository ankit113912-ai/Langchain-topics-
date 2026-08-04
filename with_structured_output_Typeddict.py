from langchain_openai import  ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated,Optional,Literal

load_dotenv

model = ChatOpenAI()

#Schema
class Review(TypedDict):


    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list "]
    summary :Annotated[str, "A brief summary of the review"]
    sentiment : Annotated[Literal["pos","neg"], " Return sentiement of the reciew either negative , positive or neutral "]
    pros : Annotated [Optional[list[str]], "write down  all the pros inside a list " ]
    cons : Annotated [Optional[list[str]], "write down  all the cons inside a list " ]

structured_model = model.with_structured_output(Review)



result = model.invoke( """ ...................................................""")


print (result['name'])









