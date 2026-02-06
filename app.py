import streamlit as st
import sys
import os

# SET ENVIRONMENT VARIABLES AT THE VERY TOP TO DISABLE SIGNALS AND TELEMETRY
os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["CREWAI_TELEMETRY_OPT_OUT"] = "true"

from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from crew import ResearchCrew

# FORCE UTF-8 ENCODING GLOBALLY
os.environ["PYTHONIOENCODING"] = "utf-8"

from dotenv import load_dotenv

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
        margin-bottom: 0px;
    }
    .footer {
        text-align: center;
        color: #888;
        padding: 20px;
        font-size: 0.8em;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown("<h1>🧬 Autonomous AI Research Lab</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>Powered by CrewAI & Multi-Provider AI</p>", unsafe_allow_html=True)

    # Sidebar for API Key check
    with st.sidebar:
        st.title("Settings")
        
        provider = st.selectbox(
            "Select AI Provider", 
            ["Google Gemini (Free)", "Groq (Fast & Recommended)"],
            help="If Gemini's key is failing, Groq is the most stable and fastest alternative."
        )
        
        if provider == "Google Gemini (Free)":
            st.info("Get it from [AI Studio](https://aistudio.google.com/app/apikey)")
            api_key = st.text_input("Google API Key", type="password", key="gemini_key")
            provider_id = "google"
        else:
            st.info("Get it for FREE from [Groq Console](https://console.groq.com/keys)")
            api_key = st.text_input("Groq API Key", type="password", key="groq_key")
            provider_id = "groq"

        if api_key:
            api_key = api_key.strip()
            # Set the environment variable for the underlying LLM library
            if provider_id == "google":
                os.environ["GOOGLE_API_KEY"] = api_key
            else:
                os.environ["GROQ_API_KEY"] = api_key
            st.success(f"✅ {provider} Key Loaded!")
        else:
            st.warning(f"⚠️ Please enter your {provider} Key.")
        
        st.markdown("---")
        st.markdown("### Agents Online")
        st.markdown("🕵️ **Researcher**")
        st.markdown("📊 **Strategist**")
        st.markdown("✍️ **Editor**")

    # Main Input Area
    topic = st.text_input("Deep Research Topic:", placeholder="e.g. Next-gen Solid State Batteries")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col1: pass
    with col2:
        run_btn = st.button("🚀 Start Collaborative Research")
    with col3: pass

    if run_btn:
        if not api_key:
            st.error("Please provide an API Key in the sidebar.")
        elif not topic:
            st.error("Please enter a research topic.")
        else:
            container = st.container()
            with st.spinner(f"Agent Crew is deep-diving into '{topic}' using {provider}..."):
                try:
                    # Run the Crew
                    crew_engine = ResearchCrew(topic, provider=provider_id, api_key=api_key)
                    
                    # Redirect stdout to capture logs if possible, but for streamlit we rely on the final result
                    result = crew_engine.run()
                    
                    st.balloons()
                    st.success("Research Complete!")
                    
                    # Layout for results
                    tab1, tab2 = st.tabs(["📄 Final Report", "⚙️ Status"])
                    
                    with tab1:
                        st.markdown("### 📝 Generated Research Paper")
                        st.markdown(result)
                        # Download button
                        st.download_button(
                            label="📥 Download Report (.md)",
                            data=str(result),
                            file_name=f"research_report_{topic.replace(' ', '_')}.md",
                            mime="text/markdown"
                        )
                    
                    with tab2:
                        st.markdown("### Agentic State")
                        st.info("The multi-agent system successfully collaborated to produce this report.")
                        st.json({
                            "Provider": provider,
                            "Topic": topic,
                            "Agents": 3,
                            "Status": "COMPLETED"
                        })
                
                except Exception as e:
                    st.error("### ❌ An Error Occurred")
                    st.error(f"**Details:** {str(e)}")
                    st.markdown("""
                    **How to fix common issues:**
                    1. **Invalid API Key**: Double-check you copied the full key without extra spaces.
                    2. **Rate Limit**: If you are using a free key, wait 1 minute and try again.
                    3. **Empty Output**: If using Gemini, it might have blocked the topic for safety. Try switching to **Groq**.
                    """)

    # Footer
    st.markdown("<div class='footer'>AI Research Lab v2.0 | Specialization Task</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
