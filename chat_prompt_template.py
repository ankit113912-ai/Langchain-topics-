from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_prompt = ChatPromptTemplate  ([

    SystemMessage(content='you are a helpful{domain} expert'),
    HumanMessage(content='Explain in simple terms, what is {topic}')
  ])

prompt = chat_prompt.invoke({'domain': 'cricket', 'topic': 'Dusra'})

print (prompt)

