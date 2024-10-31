import streamlit as st
import app1  # Import App 1 (Image Generation)

# Banner Section
st.markdown(
    """
    <div style="background-color:#f0f2f6; padding: 10px; border-radius: 5px;">
        <h2 style="text-align:center; color: #4b8bf4;">Welcome to JTech Learning Point!</h2>
        <p style="text-align:center;">Experience the power of AI with our image generation tools!</p>
    </div>
    """,
    unsafe_allow_html=True
)

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

# Back Button
st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://your-main-website.com" target="_blank">
            <button style="padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px;">
                Go Back to Main Website
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer Section
st.markdown(
    """
    <hr style="border:1px solid #e1e1e1; margin-top: 40px;">
    <div style="text-align: center;">
        <p>© 2024 AI-Powered Tools. All rights reserved. Designed by Md Jamal Uddin</p>
        <p>For more information, visit our <a href="https://www.pixkal.com/" target="_blank" rel="noopener noreferrer">Contact Page</a>.</p>
    </div>
    """,
    unsafe_allow_html=True
)