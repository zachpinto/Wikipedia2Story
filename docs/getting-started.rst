Getting Started
===============

This document outlines the steps required to get set up with the Wikipedia2Story project.

**Prerequisites**

- Python 3.8 or higher
- pip and virtualenv

**Installation**

First, clone the repository:

.. code-block:: bash

    git clone https://github.com/zachpinto/Wikipedia2Story.git
    cd Wikipedia2Story

Create and activate a virtual environment:

.. code-block:: bash

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the project and its dependencies:

.. code-block:: bash

    pip install -e .

**Running the Application**

To run the application:

.. code-block:: bash

    streamlit run app.py

Open your web browser to `http://localhost:8501` to view the app.
