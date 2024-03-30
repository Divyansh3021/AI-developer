from utils.filepaths import extract_file_paths
from utils.create_file import create_files
from crewai import Task, Crew, Process
from Agents import *
from Tasks import *

# Instantiate your crew with a sequential process
req_crew = Crew(
    agents=[req_agent, verifier],
    tasks=[req, verifiy_req],
    verbose=False
)
