from crewai import Agent
from ..llm_config.llm_models import worker_agent_llm, manager_agent_llm
from ..data_config.llama_rag_tool import create_kokomi_tool

worker_agent_llm = worker_agent_llm()

manager_agent_llm = manager_agent_llm()

rag_tool = create_kokomi_tool()

def all_agents() -> list[Agent]:
    return [roleplaying_agent()]

def roleplaying_agent () -> Agent:
    return Agent(
        role=
        """ Cosplayer, Roleplayer, and Stage artist""",
        backstory=
        """ You love roleplaying and cosplay in any character. You can
        do improvisation with less context about scenarios and stage script""",
        goal=
        """ To roleplay based on the //tool// provided to you with the 
        ('{message}')""",
        llm=manager_agent_llm,
        verbose=True,
        tools=[rag_tool]
    )