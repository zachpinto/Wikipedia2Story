import streamlit as st
import re


def clean_wikipedia_text(text):
    # Remove citations
    text = re.sub(r'\[\d+\]', '', text)
    # Remove any remaining square brackets
    text = re.sub(r'\[.*?\]', '', text)
    return text.strip()


def main():
    st.title("Wikipedia2Story")

    # Input for Wikipedia topic
    topic = st.text_input("Enter a Wikipedia topic:")

    # Theme selection (placeholder for now)
    theme = st.selectbox("Choose a visual theme:", ["8-bit pixel art", "Anime", "Watercolor"])

    if st.button("Generate Story"):
        if topic:
            summary, url = get_wikipedia_summary(topic)
            if summary:
                st.subheader(f"Summary of '{topic}'")
                st.write(summary)
                st.write(f"Source: [Wikipedia]({url})")
                st.write("(Image generation and story creation will be implemented in future steps)")
        else:
            st.warning("Please enter a Wikipedia topic.")


if __name__ == "__main__":
    main()
