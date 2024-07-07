import streamlit as st
import pandas as pd
from src.models.openai import generate_images, summarize_content
from src.data.fetch_wp_page_content import fetch_wp_page_content


# load csv data
def load_data():
    return pd.read_csv('data/processed/pages.csv')


# helper function to get rid of asterisks in the captions
def format_caption(caption):
    formatted_caption = caption.replace("**", "")
    return formatted_caption


# main function for the streamlit app
def main():
    st.title("Wikipedia2Story")
    df = load_data()

    # sidebar styling
    st.sidebar.markdown("""
        <style>
        .css-18e3th9 {
            background-color: black;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

    # Sidebar directions
    with st.sidebar:
        st.write("""
        ### DIRECTIONS:
        1. **First, choose a time period.**
        2. **Then, you can either continue 'drilling down' into new subcategories or select a specific history topic on the main menu.**
        
        *Please note, the further you 'drill down' by subcategory, the more narrow your options of topics will be.*
        """)

    # Sidebar dropdown logic
    max_columns = df.shape[1] - 2
    options = [None] * max_columns
    choices = {}

    options[0] = st.sidebar.selectbox("Select Time Period:", [''] + pd.unique(df['1']).tolist())

    # Loop through the columns to create the dropdowns
    for i in range(1, max_columns):
        if options[i - 1]:

            filtered_df = df[df['1'] == options[0]]

            for j in range(1, i):
                column_name = str(j + 1)
                filtered_df = filtered_df[filtered_df[column_name] == options[j]]

            next_column_name = str(i + 1)
            if next_column_name in filtered_df.columns and len(pd.unique(filtered_df[next_column_name].dropna())) > 0:
                unique_values = [''] + pd.unique(filtered_df[next_column_name].dropna()).tolist()

                if unique_values and len(unique_values) > 1:
                    options[i] = st.sidebar.selectbox(f"(Optional) Select Subcategory:", unique_values)
            else:
                break

    # Main content for selecting topic and art style
    selected_topic = None
    if options[0]:
        filtered_topics = df[df['1'] == options[0]]
        for j in range(1, max_columns):
            if options[j]:
                filtered_topics = filtered_topics[filtered_topics[str(j+1)] == options[j]]
        topics = filtered_topics['Topic'].tolist()
        selected_topic = st.selectbox("Select Topic", [''] + topics)

    # Theme selection
    theme_options = {
        "8-bit pixel art": "8-bit Pixel Art",
        "Anime": "Anime-Style",
        "Watercolor": "Watercolor style",
        "CUSTOM": "Custom"
    }
    theme_choice = st.selectbox("Choose a visual theme:", list(theme_options.keys()))

    # Initialize theme_code variable
    theme_code = None

    # Check if custom theme is selected
    if theme_choice == "CUSTOM":
        theme_code = st.text_input("Type your custom theme style here:", "")
    else:
        theme_code = theme_options[theme_choice]

    # This print statement is just for debugging, can be removed later
    st.write(f"Current theme code: {theme_code}")  # Helps you see what theme_code is being set

    # Generate story button
    if st.button("Generate Story"):
        if selected_topic and theme_choice:
            content = fetch_wp_page_content(selected_topic)
            summaries = summarize_content(content)
            if summaries:
                images_urls = generate_images(summaries, theme_code)
                for url, caption in zip(images_urls, summaries):
                    formatted_caption = format_caption(caption)
                    if url.startswith('http'):
                        st.image(url, width=700)
                        st.markdown(f"<div style='font-size:16px;'>{formatted_caption}</div>", unsafe_allow_html=True)
                        st.markdown("<br>", unsafe_allow_html=True)
                    else:
                        st.error(f"Failed to load image for caption: {caption}")
                        st.write("URL provided:", url)
            else:
                st.error("Failed to generate summaries. Check the content length and API limits.")


if __name__ == "__main__":
    main()
