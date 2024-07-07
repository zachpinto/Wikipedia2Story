Wikipedia2Story
==============================

Wikipedia2Story is a Streamlit application that lets users learn about history by selecting time periods and subcategories to drill down to specific topics. Upon selection, the app dynamically fetches content from Wikipedia, summarizes it, and uses the OpenAI GPT-4o model to generate ten descriptive captions. These captions are then used with the DALL-E 3 model to create visual representations in a user-selected art style.

Demo: streamlit.com

## Features

- **Dynamic Topic Selection**: Users can navigate through a hierarchical structure of historical topics, allowing users to drill down to specific topics.
- **Art Style Customization**: Users can select from predefined art styles (e.g., 8-bit, Anime, Watercolor) or input a custom style for the image generation.
- **Automated Content Generation**: The app summarizes Wikipedia content and generates corresponding images.
- **Interactive Visual Experience**: Generated images are displayed in chronological order with captions

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/zachpinto/Wikipedia2Story.git
   cd Wikipedia2Story

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   
3. **Run the Streamlit app:**
   ```bash
    streamlit run app.py
   
## Usage

1. **Select a Category**: Choose a category from the dropdown menu to explore.
2. **Select one or more Subcategories**: Choose a subcategory to narrow down the topic, drilling down as far as you like.
3. **Generate Content**: Click the "Generate Story" button to fetch Wikipedia content, summarize it, and generate images with captions.


## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          
    ├── data
    │   ├── interim        <- Wikipedia pages, preprocessed
    │   ├── processed      <- Final wikipedia page data for the app
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    │
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to 1. Transform Wikipedia data from md to csv, 2. Retrieve an individual page's contents from Wikipedia
    │   │
    │   ├── features       <- Script to transform wikipedia page data into hierarchical categories with nested structure
    │   │
    │   ├── models         <- API calls to summarize data (GPT-4o) and generate images (DALL-E 3)
    │   │
    │
    ├── app.py             <- Streamlit app
    ├── .env               <- Environment variables (OpenAI API key)
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

