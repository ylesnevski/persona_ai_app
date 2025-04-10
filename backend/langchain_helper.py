import os
from typing import Tuple

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import ValidationError

template = """
INSTRUCTION:
You will be given a persona and a message.
Rewrite the text as if the persona is the one who is
writing or saying this. Make your response around 100 tokens.

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


def get_response(persona: str, message: str) -> Tuple[str, int]:
    prompt = PromptTemplate(
        input_variables=["persona", "message"],
        template=template
    )
    try:
        llm = ChatOpenAI(
            model="gpt-4o",
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.7,
            max_tokens=100
        )

        llm_chain = prompt | llm
        response = llm_chain.invoke({"persona": persona, "message": message})
        return response.content, 200
    except ValidationError as e:
        return str(e), 403
    except Exception as e:
        return str(e), 500


# You can use the same file to test
if __name__ == "__main__":
    # Chat loop
    while True:
        persona = input("Persona (or exit, quit): ")
        if persona.lower() in ["exit", "quit"]:
            break
        message = input("Message: ")
        response = get_response(persona, message)
        print(f"{response[0]}")
