import streamlit as st
import app1  # Import App 1 (Image Generation)

# Title and Instructions
st.title("AI-Powered Tools")
st.markdown("### Welcome to the AI Image Generation Service.")
st.markdown("""
Here’s what you can do with our AI-powered tools:
- **🔹 Image Generation**: Provide a text prompt, and our AI will generate an image based on your description.
- **🔹 Future Tools**: Stay tuned for more exciting features coming soon!
""")

# Available AI Tools Section
st.markdown("### Available AI Tools")

# Bullet points for Image Generation
st.markdown("""
- **🔹 Image Generation**: Use AI to generate images based on the prompts you provide.
""")

# Sidebar for navigation between apps
st.sidebar.title("Choose an App")
app_choice = st.sidebar.radio("Select a Service", ["Image Generation", "Future Program (Coming Soon)"])

# Routing based on user selection
if app_choice == "Image Generation":
    app1.run()  # Call the run function from app1.py
elif app_choice == "Future Program (Coming Soon)":
    st.info("This feature is coming soon. Stay tuned!")
