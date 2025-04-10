import http
import os
from typing import Tuple

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from openai import AuthenticationError


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
    except AuthenticationError as ae:
        return f"You should enter a valid OPEN AI API key: {str(ae)}", http.HTTPStatus.UNAUTHORIZED
    except Exception as e:
        return f"A general error occurred: {str(e)}", http.HTTPStatus.INTERNAL_SERVER_ERROR


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
