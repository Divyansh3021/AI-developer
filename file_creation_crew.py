import time
from crewai import Crew, Agent, Task
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from main import file_description, task2 

API_KEY = "AIzaSyCS1bV6_bfizb1tAcQEB9BvCTtqCCLlGFo"
genai.configure(api_key= API_KEY)
model = genai.GenerativeModel(model_name="gemini-pro")

llm = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True, temperature=0.5, google_api_key = API_KEY)

file_creator = Agent(
    role="File creator",
    goal = "Given the file structure of a project, return a list containing the path of every file mentioned.",
    backstory="You are a Software Developer.",
    verbose=False,
    allow_delegation= False,
    llm=llm
)

file_creation = Task(
    description=f"""
    Based on the file structure obtained
    
    file structure:

    {task2.output.raw_output}

    , return a list containing only the path of every file mentioned, also remove any ' or " or ` .
    """,
    expected_output="""list of paths of file mentioned in file structure without any ` or ' or " .""",
    agent=file_creator
)

creation_crew = Crew(
    agents=[file_creator],
    tasks=[file_creation],
    verbose=True
)

filepaths = creation_crew.kickoff()

print("Filepaths: ",filepaths)
