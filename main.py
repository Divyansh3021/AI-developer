from utils.filepaths import extract_file_paths
from utils.create_file import create_files
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew, Process

API_KEY = "AIzaSyCS1bV6_bfizb1tAcQEB9BvCTtqCCLlGFo"
llm = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, temperature=0.5, google_api_key = API_KEY)

# Agents
req_agent = Agent(
    role='Senior Requirement Analyzer',
    goal='Obtain the important requirements of the software from given details',
    backstory="""You are a Senior Requirement Analyzer having more than 10 years of experience as a Product manager.""",
    verbose=False,
    allow_delegation=False,
    llm=llm
)

file_structure_agent = Agent(
    role="File Structure creator",
    goal = "Given the requirements of a software, return a file structure for this software project.",
    backstory="You are a Senior System Architect having more than 10 years of experience in creating structures of software.",
    verbose=False,
    allow_delegation= False,
    llm=llm
)

code_desc = Agent(
    role="File summary writer.",
    goal = "Given the file structure and requirements of the project. Generate a summary of files.",
    backstory="You are a Senior documentation writer with an experience of more than 10 years.",
    verbose=False,
    allow_delegation= False,
    llm=llm
)

# Create tasks for your agents
task1 = Task(
    description="""
    I want to create a Calculator software using Python language having these basic features:
    1. Addition
    2. Subtraction
    3. Division
    4. Multiplication

    Only Python language should be used.
    """,
    expected_output="Requirements of the software mentioned.",
    agent=req_agent
)

task2 = Task(
    description="""
    Based on the requirements of obtained, return a file structure for this project.
    """,
    expected_output="File Structure for the software mentioned.",
    agent=req_agent
)

task3 = Task(
    description="""
    Based on the file structure obtained, generate a summary containing:
    1. classes and function a file have and their parameters.
    2. interaction with other files.
    """,
    expected_output="description of every file, their classes, functions, arguements and return types.",
    agent=code_desc
)


# Instantiate your crew with a sequential process
crew = Crew(
    agents=[req_agent, file_structure_agent, code_desc],
    tasks=[task1, task2, task3],
    verbose=True
)


# Get your crew to work!
file_description = crew.kickoff()

# print("\n\n\n\n\n\n","task2: ",task2.output.raw_output,"\n\n\n\n\n")