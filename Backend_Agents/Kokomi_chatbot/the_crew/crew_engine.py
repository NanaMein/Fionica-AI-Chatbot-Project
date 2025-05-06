from ..agents_config.agents import all_agents
from ..tasks_config.tasks import all_tasks
from crewai import Process, Crew
from ..data_config.llama_rag_tool import create_kokomi_tool
from crewai.memory import LongTermMemory, ShortTermMemory
from mem0 import MemoryClient

memory = MemoryClient()

crew = Crew(
    agents=all_agents(),
    tasks=all_tasks(),
    process=Process.sequential,
    verbose=True,
    memory=True
)
while True:
    messages = input("Kokomi is ready to chat, Tell her how you feel:  \n")
    inputs={
        'message':messages
    }
    print(crew.kickoff(inputs=inputs))