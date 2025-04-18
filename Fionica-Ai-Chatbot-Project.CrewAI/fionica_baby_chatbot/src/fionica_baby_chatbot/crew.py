import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
from crewai.agents.agent_builder.base_agent import BaseAgent
from dotenv import load_dotenv
from typing import List

load_dotenv()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class FionicaBabyChatbot:
    # agents: List[BaseAgent]
    # tasks: List[Task]
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    llm_model = ChatGroq(model=os.getenv('CHEAP_MODEL'), api_key=os.getenv('GROQ_API_KEY'), temperature=.3)


    @agent
    def school_girl_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['school_girl_agent'],# type: ignore[index]
            llm=self.llm_model,
            verbose=True
        )

    @agent
    def translator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['translator_agent'],# type: ignore[index]
            llm=self.llm_model,
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def entry_task(self) -> Task:
        return Task(
            config=self.tasks_config['entry_task'],# type: ignore[index]
        )

    @task
    def second_task(self) -> Task:
        return Task(
            config=self.tasks_config['second_task'],# type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the FionicaBabyChatbot crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,

        )
