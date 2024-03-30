from crewai import Crew
from Agents import file_structure_agent, verifier
from FileStructureTasks import file_structure_task, verifiy_file_structure_task

file_structure_crew = Crew(
    agents=[file_structure_agent, verifier],
    tasks=[file_structure_task, verifiy_file_structure_task],
    verbose=False
)

file_structure = file_structure_crew.kickoff()