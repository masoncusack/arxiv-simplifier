import os
import json
import streamlit as st
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

title = st.title("arXiv abstracts simplifier 📖🤯👶")
abstract = st.text_area(label="Enter an arXiv abstract that you don't get. Press enter to submit.")
reading_age = st.slider(
    label="Choose your reading age in the field of this paper. 1 is practically newborn, 117 is superhuman (for now).",
    min_value=1,
    max_value=117
)

if reading_age == 0:
    recipient_prompt = "baby"  # TODO: model does not respond well to "newborn baby" - for now I've fixed min above at 1.
else:
    recipient_prompt = f"{reading_age} year old"
openai_prompt = f"A {recipient_prompt} asked me what this abstract means:\n\"\"\"\n{abstract}\n\"\"\"\nI rephrased it for them, in plain language a {recipient_prompt} can understand:\n\"\"\"\n"

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
