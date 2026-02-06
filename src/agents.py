import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai.tools import tool

load_dotenv()

# Initialize Searching Tool
@tool("search_tool")
def search_tool(topic: str):
    """Search the internet for information on a given topic."""
    from langchain_community.tools import DuckDuckGoSearchRun
    return DuckDuckGoSearchRun().run(topic)

class ResearchAgents:
    def __init__(self):
        # We use the LangChain class which is more stable for AI Studio keys
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.5
        )

    def researcher_agent(self):
        return Agent(
            role="Deep Search Researcher",
            goal="Scan the web and academic sources to find high-quality, up-to-date information on {topic}.",
            backstory="""You are an expert researcher with a knack for finding hidden gems in technical blogs, 
            news articles, and academic papers. You distinguish between hype and reality, 
            ensuring the data collected is factual and relevant.""",
            tools=[search_tool],
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )

    def technical_analyst_agent(self):
        return Agent(
            role="Technical Strategy Analyst",
            goal="Analyze the research findings about {topic} to identify trends, pros/cons, and future implications.",
            backstory="""You are a veteran technology strategist. You take raw information and 
            turn it into actionable insights. You excel at structured thinking and 
            identifying the 'so what?' behind technological shifts.""",
            llm=self.llm,
            allow_delegation=True,
            verbose=True
        )

    def scientific_writer_agent(self):
        return Agent(
            role="Chief Scientific Editor",
            goal="Synthesize all findings into a professional, academic-style markdown report on {topic}.",
            backstory="""You are a world-class technical writer. You take complex analyses and 
            present them in a clear, persuasive, and beautifully structured report. 
            You ensure the final output is ready for a C-suite executive or a lead researcher.""",
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )
