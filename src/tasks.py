from crewai import Task
from datetime import datetime

class ResearchTasks:
    def research_task(self, agent, topic):
        return Task(
            description=f"""Conduct a thorough search on the topic: {topic}. 
            Focus on gathering recent developments (within the last 2 years), 
            technical architecture details, and major market players.
            Current Date: {datetime.now().strftime("%Y-%m-%d")}""",
            expected_output="""A comprehensive list of findings including key facts, statistics, 
            and links to major sources. At least 5 detailed bullet points.""",
            agent=agent
        )

    def analysis_task(self, agent, topic):
        return Task(
            description=f"""Review the findings provided by the researcher on {topic}. 
            Categorize the information into:
            1. Technical Feasibility
            2. Market Impact
            3. Challenges/Limitations
            4. Paradoxes or conflicting data.""",
            expected_output="""A structured analysis document that breaks down the 'why' and 'how' 
            of the research topic. This should be internal-ready for the writer.""",
            agent=agent
        )

    def writing_task(self, agent, topic):
        return Task(
            description=f"""Using the research and analysis, write a final, polished 
            Research Paper on {topic}. 
            The paper must include:
            - Executive Summary
            - Detailed Technical Analysis
            - Future Outlook
            - References/Sources gathered.
            Format the output in clean Markdown with professional headers.""",
            expected_output="A full-length Markdown Research Report (approx 800-1200 words).",
            agent=agent,
            output_file=f"research_report.md"
        )
