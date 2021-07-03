import os
import json
import streamlit as st
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

title = st.title("arXiv abstracts simplifier 📖🤯👶")
text_field = st.text_input(label="Enter an arXiv abstract that you don't get. Press enter to submit.")
reading_age = st.slider(
    label="Choose your reading age in the field of this paper. 0 is newborn, 117 is superhuman (for now).",
    min_value=1,
    max_value=117
)

openai_prompt = f"An {reading_age} year old asked me what this passage means:\n\"\"\"\n{text_field}\n\"\"\"\nI rephrased it for them, in plain language a {reading_age} year old can understand:\n\"\"\"\n"

response = openai.Completion.create(
  engine="davinci",
  prompt=openai_prompt,
  temperature=0.5,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.2,
  presence_penalty=0,
  stop=["\"\"\""]
)

st.text("Summary:")
st.write(response["choices"][0]["text"])
