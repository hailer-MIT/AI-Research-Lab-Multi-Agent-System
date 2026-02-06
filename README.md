# 🧬 Autonomous AI Research Lab (MAS)

A specialized Multi-Agent System (MAS) built with **CrewAI** and **Google Gemini** to automate deep research, analysis, and technical writing.

## 🚀 Overview
This system demonstrates the core concepts of Multi-Agent Systems, including:
- **Autonomy**: Agents make independent decisions on how to search and analyze.
- **Social Ability**: Agents work together in a sequential pipeline to share context and memory.
- **Specialization**: Each agent has a distinct role, goal, and backstory.
- **Tool Usage**: Integration with DuckDuckGo for live environment interaction.

## 👥 The Crew
1. **Deep Search Researcher**: Scours the web for raw data and recent developments.
2. **Technical Strategy Analyst**: Synthesizes data into structured technical insights.
3. **Chief Scientific Editor**: Formats and polishes the final research paper.

## 🛠️ Tech Stack
- **Framework**: CrewAI
- **Brain**: Google Gemini 1.5 Flash
- **Orchestration**: Python
- **UI**: Streamlit (Premium Dark Theme)

## 📥 Installation
1. Ensure you have Python 3.10+ installed.
2. Navigate to the project folder:
   ```bash
   cd AI_Research_Lab
   ```
3. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## 🏃 Running the Lab
1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Enter your **Google API Key** in the sidebar.
3. Type a research topic and watch the agents collaborate in the terminal!

## 📄 Output
The system generates a high-quality Markdown report named `research_report.md` in the root directory.
