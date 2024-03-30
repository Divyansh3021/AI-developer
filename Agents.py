from crewai import Agent
from llm import llm

# Agents
req_agent = Agent(
    role='Senior Requirement Analyzer',
    goal='Obtain the important requirements of the software from given details',
    backstory="""You are a Senior Requirement Analyzer having more than 10 years of experience as a Product manager.""",
    verbose=False,
    allow_delegation=False,
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


verifier = Agent(
    role = "Verify task and corresponding output",
    goal = "Given the task and corresponding result from an LLM, verify whether given result is according to the task or not. Return True or False only.",\
    backstory = "You are a requirement verifier",
    verbose = False,
    allow_delegation = False,
    llm = llm
)

file_structure_agent = Agent(
    role="File Structure creator",
    goal = "Given the requirements of a software, return a file structure for this software project.",
    backstory="You are a Senior System Architect having more than 10 years of experience in creating structures of software.",
    verbose=False,
    allow_delegation= False,
    llm=llm
)