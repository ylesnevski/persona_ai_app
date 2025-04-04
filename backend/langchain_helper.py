import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

template = """
INSTRUCTION:
You will be given a persona and a message.
Rewrite the text as if the persona is the one who is
writing or saying this.

EXAMPLE:

PERSONA: child
MESSAGE: i want milk
REWRITTEN TEXT: i wanna milk. give me.

PERSONA:
{persona}

MESSAGE:
{message}

REWRITTEN TEXT:
"""

prompt = PromptTemplate(
    input_variables=["persona", "message"],
    template=template
)
llm = ChatOpenAI(
    model="gpt-4o",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7,
    max_tokens=100
)

llm_chain = prompt | llm


def get_response(persona: str, message: str) -> str:
    return llm_chain.invoke({"persona": persona, "message": message}).content


# You can use the same file to test
if __name__ == "__main__":
    # Chat loop
    while True:
        persona = input("Persona (or exit, quit): ")
        if persona.lower() in ["exit", "quit"]:
            break
        message = input("Message: ")
        response = get_response(persona, message)
        print(f"{response}")
