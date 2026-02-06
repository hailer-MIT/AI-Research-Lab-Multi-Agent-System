from crewai import Crew, Process
from agents import ResearchAgents
from tasks import ResearchTasks

class ResearchCrew:
    def __init__(self, topic):
        self.topic = topic

    def run(self):
        # 1. Initialize Agents
        agents = ResearchAgents()
        researcher = agents.researcher_agent()
        analyst = agents.technical_analyst_agent()
        writer = agents.scientific_writer_agent()

        # 2. Initialize Tasks
        tasks = ResearchTasks()
        t1 = tasks.research_task(researcher, self.topic)
        t2 = tasks.analysis_task(analyst, self.topic)
        t3 = tasks.writing_task(writer, self.topic)

        # 3. Assemble the Crew
        # We use a sequential process to demonstrate the flow of knowledge
        crew = Crew(
            agents=[researcher, analyst, writer],
            tasks=[t1, t2, t3],
            process=Process.sequential,
            verbose=True,
            memory=False # We disable this to avoid the OpenAI API key requirement
        )

        return crew.kickoff()
