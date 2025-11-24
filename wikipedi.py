import warnings
warnings.filterwarnings("ignore")

import wikipedia
wikipedia.set_lang("en")

import streamlit as st

st.title("Search in Wikipedia")

message = st.chat_input("Enter your search?")

def search_wikipedia_full(query):
    try:
        page = wikipedia.page(query)
        st.write(f"### 🔍 Full content of the page «{query}»:")
        st.write(page.content)

    except wikipedia.exceptions.DisambiguationError as e:
        st.write("⚠ **Multiple meanings found:**")

        choice = st.selectbox("Choose an option:", e.options)
        if choice:
            search_wikipedia_full(choice)

    except wikipedia.exceptions.PageError:
        st.write("❌ No page found for this term.")


if message:
    search_wikipedia_full(message)
