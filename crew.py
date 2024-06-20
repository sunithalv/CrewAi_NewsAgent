from crewai import Crew,Process
from tasks import research_task,write_task
from agents import researcher,writer

crew_news = Crew(
    agents = [researcher, writer],
    tasks = [research_task, write_task],
    process=Process.sequential,
)

