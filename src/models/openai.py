import openai
import os
from dotenv import load_dotenv
import streamlit as st

# Access API Key securely from Streamlit's secrets
API_KEY = st.secrets["OPENAI_API_KEY"]

# Initialize OpenAI client with the API key
client = openai.OpenAI(api_key=API_KEY)


# Function to call the OpenAI API
def call_openai_api(content):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": content}
            ]
        )
        print("API Response:", response)
        return response
    except Exception as e:
        print(f"API Call Error: {str(e)}")
        return None


# Function to extract summaries from the API response
def extract_summaries(response, segments=10):
    """ Extract summaries from the API response, ensuring there are always exactly ten segments. """
    try:
        if response:
            if hasattr(response, 'choices') and len(response.choices) > 0:
                full_summary = response.choices[0].message.content
                summaries = full_summary.split('\n\n')

                while len(summaries) < segments:
                    if summaries:
                        summaries.append("Additional information not available.")
                    else:
                        summaries.append("Content not provided.")

                if len(summaries) > segments:
                    summaries = summaries[:segments]

                return summaries
            else:
                print("Response structure is unexpected or missing 'choices' key.")
                return None
        else:
            print("No response received from API")
            return None
    except Exception as e:
        print(f"Error Extracting Summaries: {str(e)}")
        return None


# Function to summarize content into distinct segments
def summarize_content(content, segments=10):
    """Generates summaries for given content, split into specified number of segments."""
    content_to_summarize = f"Please provide a detailed summary divided into {segments} distinct parts, each part focusing on a different aspect of the content. It is extremely vital that you create exactly {segments} parts. Do not preface with anything like 'Here are the 10 distinct parts', just jump straight into the 10 distinct parts. Say nothing else before or after giving these 10 parts: {content}"
    response = call_openai_api(content_to_summarize)
    return extract_summaries(response, segments)


# Function to generate images based on summaries user-selected art style theme code
def generate_images(summaries, theme_code):
    """Generates images for each summary part based on the specified theme code."""
    print("Using theme code:", theme_code)
    images = []
    for summary in summaries:
        # Generate a prompt for the image generation API
        prompt = f"Create a {theme_code} image focusing on summary: {summary}. Please avoid generating abstract art, text, or anything unrelated to the summary. If you find the summary too long or sensitive to display as artwork, choose keywords that are tangentially related to the summary, like proper nouns, locations, etc. Focus on visual representation."

        if len(prompt) > 1000:
            prompt = prompt[:1000]

        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                n=1
            )
            if response and response.data:
                images.append(response.data[0].url)
            else:
                # In case of image generation error, use fallback
                images.append('https://raw.githubusercontent.com/zachpinto/Wikipedia2Story/2679bb5abd9a3838717915a606b173c945aea270/assets/error.jpg')
        except Exception as e:
            print(f"Error generating image for summary starting with '{summary[:30]}...': {str(e)}")
            images.append('https://raw.githubusercontent.com/zachpinto/Wikipedia2Story/2679bb5abd9a3838717915a606b173c945aea270/assets/error.jpg')
    return images


# Function to format the caption for the image
def generate_images_from_content(content, theme_code):
    """Generates images from summaries of the provided content based on user-selected art style theme."""
    summaries = summarize_content(content)
    return generate_images(summaries, theme_code)
