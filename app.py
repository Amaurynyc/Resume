import streamlit as st
import cohere
import re

# Streamlit UI setup
st.sidebar.write("""
# **Amaury Desrosiers**
## **amaury@outlook.com**
""")

st.sidebar.write("Trained with Cohere Command")

st.sidebar.markdown("""
[Solution Architect Director Opening](https://jobs.lever.co/cohere/f2b4fa4a-6f45-4582-bba8-a7ddbd74a2ad)
""")

# URL to your LinkedIn profile
linkedin_profile_url = "https://www.linkedin.com/in/amaurydesrosiers"

# URL to a LinkedIn icon image
linkedin_icon_url = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"

# HTML to embed the icon with a link
linkedin_html = f'<a href="{linkedin_profile_url}" target="_blank"><img src="{linkedin_icon_url}" alt="LinkedIn" style="width:30px;height:30px;border:0;"></a>'

# Display the LinkedIn icon with link in the sidebar
st.sidebar.markdown(linkedin_html, unsafe_allow_html=True)

# Title and Subtitle
st.title("Meet Amaury Desrosiers!")
st.markdown("**Exploring Amaury's fit for Solution Architect leader at Cohere**")


# Example Questions in Grey
questions_html = """
<div style='color: grey;'>
<p>What unique skills does Amaury Desrosiers bring to the role of Solution Architect Director?</p>
<p>How has Amaury's background prepared him for managing solution architects at Cohere?</p>
<p>Can you share examples of Amaury's past achievements in technology leadership?</p>
<p>What are Amaury's key strengths in team management and project execution?</p>
</div>
"""
st.markdown(questions_html, unsafe_allow_html=True)
st.divider()

# Chat interface
user_input = st.text_input(" ℹ️ What do you want to know about Amaury?", value="What specific experiences would set him for success in this role?")



co = cohere.Client(st.secrets["my_cohere_api_key"])

context=st.secrets["secret_message"]

if user_input:
    try:
        # Sending the user message to the model
        response = co.chat(message= f"{context},{user_input}" )

        st.write(response.text)

        text=response.text
        
        )
       
        
       
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
