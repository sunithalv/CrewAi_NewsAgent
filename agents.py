from crewai import Agent
from tools import search_tool
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
import os

#get the apikey from kubernetes secrets
groq_api_key=os.environ["GROQ_API_KEY"]

## call the gemini models
llm=ChatGroq(model="gemma-7b-it",
                    verbose=True,
                    temperature=0.5,
                    groq_api_key=groq_api_key
)

#Define agents with specific role/goal
researcher = Agent(
    role = "Senior News Research Analyst",
    goal = "Investigate and report on the latest news on {topic} in 2024.",
    backstory = """Your expertise lies in sourcing and analyzing news articles.
      You excel at breaking down complex subject matter and presenting it in an accessible and insightful manner.""",
    verbose = False,
    allow_delegation = True,
    tools = [search_tool],
    llm = llm
)
writer = Agent(
    role = "Expert News Report Writer",
    goal = "Craft concise and informative articles summarizing the latest news on the {topic} in 2024.",
    backstory = """You are a well-respected content strategist with a knack for creating engaging and informative articles.
    Your expertise lies in transforming news concepts into clear, compelling narratives that are easily understood by a broad audience.""",
    verbose = True,
    allow_delegation = False,
    llm = llm
)