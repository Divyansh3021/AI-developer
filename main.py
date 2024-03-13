# from langchain.tools import ToolBase
from langchain_community.utilities import SerpAPIWrapper

from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew, Process

API_KEY = "AIzaSyCS1bV6_bfizb1tAcQEB9BvCTtqCCLlGFo"
llm = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, temperature=0.5, google_api_key = API_KEY)

# Agents
req_agent = Agent(
    role='Senior Requirement Analyzer',
    goal='Obtain the requirements of a software from given details',
    backstory="""You are a Senior Requirement Analyzer having more than 10 years of experience as a Product manager.""",
    verbose=False,
    allow_delegation=False,
    llm=llm
)

file_structure_agent = Agent(
    role="File Structure creator",
    goal = "Given the requirements of a software, create a file structure for this software project.",
    backstory="You are a Senior System Architect having more than 10 years of experience in creating structures of software.",
    verbose=False,
    allow_delegation= False,
    llm=llm
)

# Create tasks for your agents
task1 = Task(
    description="""
    I want to create a Calculator software having these basic features:
    1. Addition
    2. Subtraction
    3. Division
    4. Multiplication

    The coding language should be Python.
    """,
    expected_output="Requirements of the software mentioned.",
    agent=req_agent
)

task2 = Task(
    description="""
    Based on the requirements of obtained, create a file structure for this project.
    """,
    expected_output="File Structure of the software mentioned.",
    agent=req_agent
)

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[req_agent, file_structure_agent],
    tasks=[task1, task2],
    verbose=True
)

# Get your crew to work!
result = crew.kickoff()

# print("######################")
print(result)
