from utils.filepaths import extract_file_paths
from utils.create_file import create_files
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew, Process
import dotenv
dotenv.load_dotenv()
import os

llm = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, temperature=0.5, google_api_key = os.getenv('API_KEY'))

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
    verbose = True,
    allow_delegation = False,
    llm = llm
)

# Create tasks for your agents

task1_desc = """
    A library management software using with the option of:
    1. issuing book
    2. returning book
    3. report a missing book
    4. finding book in existing library

    Python language must be used.
    """

task1 = Task(
    description = task1_desc,
    expected_output="Requirements of the software mentioned.",
    agent=req_agent
)

verifiy_task1 = Task(
    description = f"""
    Verify whether requirements obtained is correct according to the task.
    task: {task1_desc}
    """,
    expected_output = "True or False",
    agent = verifier
)


task3 = Task(
    description="""
    Based on the file structure obtained, generate a summary containing:
    1. Their use and types of content it stores.
    1. classes and function a file have and their parameters.
    2. interaction with other files.
    """,
    expected_output="description of every file, their classes, functions, arguements and return types.",
    agent=code_desc
)


# Instantiate your crew with a sequential process
crew = Crew(
    agents=[req_agent, verifier],
    tasks=[task1, verifiy_task1],
    verbose=True
)
# Get your crew to work!
file_description = crew.kickoff()




file_structure_agent = Agent(
    role="File Structure creator",
    goal = "Given the requirements of a software, return a file structure for this software project.",
    backstory="You are a Senior System Architect having more than 10 years of experience in creating structures of software.",
    verbose=False,
    allow_delegation= False,
    llm=llm
)

task2_desc = f"""
    Based on these requirements 

    {task1.output.raw_output}

    , return a file structure for this project.
    """

task2 = Task(
    description = task2_desc,
    expected_output="File Structure for the software mentioned.",
    agent=file_structure_agent
)

verifiy_task2 = Task(
    description = f"""
    Verify whether file structure obtained is correct according to the task.
    task: {task2_desc}
    """,
    expected_output = "True or False",
    agent = verifier
)

crew2 = Crew(
    agents=[file_structure_agent, verifier],
    tasks=[task2, verifiy_task2],
    verbose=True
)

file_structure = crew2.kickoff()