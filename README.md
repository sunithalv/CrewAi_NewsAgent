# CrewAi_NewsAgent

## Overview
This is a news report generation engine that generates latest news report related to topic provided as input. It uses Crew AI for Research and Writer Agents and SerperDevTool for getting the latest google results. The LLM used is llama3 via the langchain groq platform for faster inference.The input is provided via a Streamlit interface.

![Screenshot 2024-06-19 223152](https://github.com/sunithalv/CrewAi_NewsAgent/assets/28974154/b005a7aa-6142-4575-aaf9-7cc6a2e47bc1)

## Getting Started

### Prerequisites
- Python 3.8 or later
- GROQ API key
- SERPER API KEY

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sunithalv/CrewAi_NewsAgent.git
  
2. **Set Up a Conda Environment (Recommended)**
* Create a new Conda environment:
   ```bash
   conda create -p venv python=3.10 -y
* Activate the environment:
   ```bash
   conda activate venv/

3. **Install Dependencies**
* Install the required packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt

4. **Set Up Your Keys**
* Create a .env file in the root directory of the project.
* Add your keys to the `.env` file

### Usage
To run the API, execute the following command:
   ```bash
   streamlit run app.py
```



