from ..llm_config.llm_models import worker_agent_llm, manager_agent_llm
from ..agents_config.agents import roleplaying_agent
from crewai import Task

def first_task() -> Task:
    return Task(
        agent=roleplaying_agent(),
        description=
        """ Based on the message //{message}//, you will roleplay based on the tool
         //tool// provided to you and make a reply based on the tool and message to you.""",
        expected_output=
        """ Roleplay and reply like the character in the document in tool
         and then reply based on {message}""",
        tools=[]
    )