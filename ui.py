import streamlit as st
from agent import app, AgentState

st.set_page_config(page_title="Multi-Agent Blog Generator", layout="wide")

st.title("🤖 Multi-Agent Blog Generator")
st.markdown("Generate engaging blog posts automatically using AI agents")

# Sidebar with instructions
with st.sidebar:
    st.markdown("### How it works")
    st.markdown("""
    1. **Enter a topic** you want to write about
    2. **Click "Generate Blog"**
    3. The **Researcher** agent searches for facts
    4. The **Writer** agent creates a blog post
    """)
    


# Main content
col1, col2 = st.columns([2, 1])

with col1:
    topic_input = st.text_input(
        "📝 Enter a topic:",
        placeholder="e.g., The future of AI Agents",
        label_visibility="visible"
    )

with col2:
    generate_button = st.button("Generate Blog", type="primary", use_container_width=True)

st.markdown("---")

# Handle blog generation
if generate_button:
    if not topic_input.strip():
        st.error("❌ Please enter a topic first!")
    else:
        try:
            # Create input state
            inputs: AgentState = {
                "topic": topic_input.strip(),
                "research_data": [],
                "blog_post": "",
            }
            
            # Status placeholders
            status_container = st.container()
            result_container = st.container()
            
            with status_container:
                st.info("🔍 Researching topic...")
                st.info("✍️ Writing blog post...")
            
            # Run the agent system
            result = app.invoke(inputs)
            
            # Clear status messages
            status_container.empty()
            
            # Display result
            with result_container:
                st.success("✅ Blog post generated successfully!")
                st.markdown("---")
                st.markdown("### Generated Blog Post")
                st.markdown(result["blog_post"])
                
                # Option to copy
                st.markdown("---")
                st.text_area(
                    "Copy the blog post below:",
                    value=result["blog_post"],
                    height=200,
                    disabled=True
                )
                
        except Exception as e:
            st.error(f"❌ Error generating blog post: {str(e)}")
            st.markdown("""
            **Troubleshooting:**
            - Ensure Ollama is running (`ollama serve`)
            - Verify llama3 model is installed (`ollama pull llama3`)
            - Check your internet connection for research data
            """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 12px;'>"
    "Multi-Agent Blog Generator | Powered by LangGraph & Ollama"
    "</div>",
    unsafe_allow_html=True
)
