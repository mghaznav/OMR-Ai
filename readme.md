# OMR-Ai

## Description

OMR-Ai is a vision-based AI project that scans MCQ (Multiple Choice Questions) bubble sheets used for examinations in universities and schools. It will be used in a mobile app that will take pictures of the bubble sheets, and use OMR-Ai to find the answers provided by the students, and generate a result by matching the answers against an answer sheet.

## Prerequisites

- Python 3.12.2 (We recommend using `pyenv` for easy Python version management)

## Environment Setup

1. **Set the Local Python Version**
   First, set the local Python version for the project using `pyenv`:
   ```bash
   pyenv local 3.12.2
   ```

2. **Create a Virtual Environment**
    Then, create a new virtual environment using the pyenv virtualenv command. This will use the Python version set by pyenv:
    ```bash
    pyenv virtualenv 3.12.2 venv
    ```

3. **Activate the Virtual Environment**
    Activate the virtual environment using the following command:
    ```bash
    pyenv activate venv
    ```

4. **Install the Required Packages**
    Install the required packages from the requirements.txt file:
    ```bash
    pip install -r requirements.txt
    ```