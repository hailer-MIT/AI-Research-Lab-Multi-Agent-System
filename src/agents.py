import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from crewai.tools import tool

load_dotenv()

# Force UTF-8 environment for all underlying libraries to fix Groq encoding errors
os.environ["PYTHONIOENCODING"] = "utf-8"

@tool("search_tool")
def search_tool(topic: str):
    """Search the internet for information on a given topic."""
    try:
        from langchain_community.tools import DuckDuckGoSearchRun
        return DuckDuckGoSearchRun().run(topic)
    except Exception as e:
        return f"Error using search tool: {str(e)}"

class ResearchAgents:
    def __init__(self, provider="google", api_key=None):
        self.api_key = api_key.strip() if api_key else None
        self.provider = provider.lower()
        
        if self.provider == "google":
            self.llm = LLM(
                model="gemini/gemini-2.0-flash",
                api_key=self.api_key,
                temperature=0.4
            )
        elif self.provider == "groq":
            # Using the absolute safest string for the model
            self.llm = LLM(
                model="groq/llama-3.3-70b-versatile",
                api_key=self.api_key,
                temperature=0.4
            )

    def researcher_agent(self):
        return Agent(
            role="Lead Researcher",
            goal="Identify the most accurate and recent details about {topic}.",
            backstory="You are a professional researcher. You verify all facts and ignore hype.",
            tools=[search_tool],
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )

    def technical_analyst_agent(self):
        return Agent(
            role="Technology Strategist",
            goal="Provide strategic insights based on findings about {topic}.",
            backstory="You analyze trends and patterns to identify the significance of research data.",
            llm=self.llm,
            allow_delegation=True,
            verbose=True
        )

    def scientific_writer_agent(self):
        return Agent(
            role="Scientific Editor",
            goal="Create a professional report about {topic} in markdown format.",
            backstory="You write clearly and present complex data in a professional structure.",
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )
