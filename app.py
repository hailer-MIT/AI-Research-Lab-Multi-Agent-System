import streamlit as st
import sys
import os
from dotenv import load_dotenv

# Ensure the 'src' directory is in the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from crew import ResearchCrew

# Load environment variables
load_dotenv()

# UI Config
st.set_page_config(page_title="AI Research Lab", page_icon="🧬", layout="wide")

# Custom CSS for Premium Look
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        border: none;
    }
    .agent-card {
        padding: 20px;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }
    h1 {
        background: -webkit-linear-gradient(#00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 800;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown("<h1>🧬 Autonomous AI Research Lab</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>Powered by CrewAI & Google Gemini</p>", unsafe_allow_html=True)

    # Sidebar for API Key check
    with st.sidebar:
        st.title("Settings")
        api_key = st.text_input("Google API Key", type="password", value=os.getenv("GOOGLE_API_KEY", ""))
        if api_key:
            os.environ["GOOGLE_API_KEY"] = api_key
            st.success("API Key Loaded!")
        else:
            st.warning("Please enter your Gemini API Key to proceed.")
        
        st.markdown("---")
        st.markdown("### Agents in the Crew")
        st.markdown("🕵️ **Lead Researcher**")
        st.markdown("📊 **Technical Strategist**")
        st.markdown("✍️ **Scientific Editor**")

    # Main Input Area
    topic = st.text_input("Enter the research topic:", placeholder="e.g. Next-gen Solid State Batteries")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        pass
    with col2:
        run_btn = st.button("🚀 Start Deep Research")
    with col3:
        pass

    if run_btn:
        if not api_key:
            st.error("Please provide an API Key first.")
        elif not topic:
            st.error("Please enter a research topic sample.")
        else:
            with st.spinner(f"Agent Crew is investigating '{topic}'... This will take a few minutes."):
                try:
                    # Run the Crew
                    crew_engine = ResearchCrew(topic)
                    result = crew_engine.run()
                    
                    st.success("Research Complete!")
                    
                    # Layout for results
                    tab1, tab2 = st.tabs(["📄 Final Report", "🪵 Agent Logs"])
                    
                    with tab1:
                        st.markdown(result)
                        # Download button
                        st.download_button(
                            label="Download Report",
                            data=str(result),
                            file_name=f"research_report_{topic.replace(' ', '_')}.md",
                            mime="text/markdown"
                        )
                    
                    with tab2:
                        st.info("Agent process logs are visible in the terminal while running. In this UI, we show the final state.")
                        st.markdown("Check `research_report.md` in your project folder for the persistent version.")
                
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

    # Footer
    st.markdown("---")
    st.markdown("<p style='text-align: center;'>Specialization: Autonomous Mult-Agent Systems Training Task</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
