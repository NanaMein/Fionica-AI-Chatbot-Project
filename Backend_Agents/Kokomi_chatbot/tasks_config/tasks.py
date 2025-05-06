from ..agents_config.agents import roleplaying_agent
from ..data_config.llama_rag_tool import create_kokomi_tool
from crewai import Task

rag_tool = create_kokomi_tool()
def all_tasks() -> list[Task]:
    return [first_task()]

def first_task() -> Task:
    return Task(
        agent=roleplaying_agent(),
        description=
        """ Based on the message //{message}//, you will roleplay based on the tool
         //tool// provided to you and make a reply based on the tool and message to you.""",
        expected_output=
        """ Roleplay and reply like the character in the document in tool
         and then reply based on {message}""",
        tools=[rag_tool]
    )