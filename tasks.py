from crewai import Task
from tools import search_tool
from agents import researcher,writer

research_task = Task(
    description = "Investigate the most recent news in 2024 based on {topic}.",
    expected_output = "A detailed summary of the latest news on {topic}.",
    agent = researcher
)

write_task = Task(
    description = "Compose a concise and informative article highlighting the latest details on {topic}.",
    expected_output = "An engaging and well-structured article on the recent news on {topic}.",
    agent = writer
)