from crewai import Crew, Process
from agents import ResearchAgents
from tasks import ResearchTasks

class ResearchCrew:
    def __init__(self, topic, provider="google", api_key=None):
        self.topic = topic
        self.provider = provider
        self.api_key = api_key

    def run(self):
        # 1. Initialize Agents
        agents = ResearchAgents(provider=self.provider, api_key=self.api_key)
        researcher = agents.researcher_agent()
        analyst = agents.technical_analyst_agent()
        writer = agents.scientific_writer_agent()

        # 2. Initialize Tasks
        tasks = ResearchTasks()
        t1 = tasks.research_task(researcher, self.topic)
        t2 = tasks.analysis_task(analyst, self.topic)
        t3 = tasks.writing_task(writer, self.topic)

        # 3. Assemble the Crew
        crew = Crew(
            agents=[researcher, analyst, writer],
            tasks=[t1, t2, t3],
            process=Process.sequential,
            verbose=True,
            memory=False,
            max_rpm=2 # This prevents hitting the Groq/Gemini rate limits
        )

        return crew.kickoff()
