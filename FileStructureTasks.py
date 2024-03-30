from crewai import Task
from RequirementCrew import req
from Agents import file_structure_agent, verifier



file_structure_task_desc = f"""
    Develop a well-structured file system for a library management system written in Python. This structure should promote code maintainability, readability, and modularity.

    Requirements:

    {req.output.raw_output}

    Desired File Structure:

    Outline a directory structure that logically groups related functionalities.
    Specify the purpose and content of each file within the directories.
    Consider modularization using Python modules or classes.
    Include a data folder to store book and member information (CSV or SQLite).
    Deliverable:

    A clear and concise description of the project's file structure, including folder names, file names, and their intended purposes.
    """

file_structure_task = Task(
    description = file_structure_task_desc,
    expected_output="File Structure for the software mentioned.",
    agent=file_structure_agent
)

verifiy_file_structure_task = Task(
    description = f"""
    Verify whether Project structure obtained is correct according to the requirements, return True if and only if every requirement is followed and file strucutre contains corresponding file names, False otherwise.

    Project Structure:
    {file_structure_task_desc}

    Requirements:
    {req.output.raw_output}
    """,
    expected_output = "True or False",
    agent = verifier
)


# task3 = Task(
#     description="""
#     Based on the file structure obtained, generate a summary containing:
#     1. Their use and types of content it stores.
#     1. classes and function a file have and their parameters.
#     2. interaction with other files.
#     """,
#     expected_output="description of every file, their classes, functions, arguements and return types.",
#     agent=code_desc
# )