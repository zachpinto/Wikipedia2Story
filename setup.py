from setuptools import find_packages, setup

setup(
    name='Wikipedia2Story',
    version='0.1.0',
    packages=find_packages(),
    description='Wikipedia2Story is a Streamlit application that lets users learn about history by selecting time periods and subcategories to drill down to specific topics. Upon selection, the app dynamically fetches content from Wikipedia, summarizes it, and uses the OpenAI GPT-4o model to generate ten descriptive captions. These captions are then used with the DALL-E 3 model to create visual representations in a user-selected art style.',
    author='Zachary Pinto',
    license='MIT',
    install_requires=[
        'streamlit',
        'pandas',
        'requests',
        'openai',
        'requests',
        'spacy'
    ],
)
