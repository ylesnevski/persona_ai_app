import streamlit as st
import requests

st.title("Rewrite text as persona")

with st.form("rewrite_form"):
    persona = st.text_input("Persona:", key="persona")
    message = st.text_input("Message:", key="message")

    submit = st.form_submit_button("Submit")

    if submit:
        if persona and message:
            try:
                response = requests.post(
                    "http://backend:8000/chat",
                    json={"message": message, "persona": persona}
                )
                response.raise_for_status()
                rewritten_text = response.json().get("response", "")
                st.text_area("Rewritten Text:", rewritten_text, height=200)
            except requests.RequestException as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please fill in both the Persona and the Message.")
