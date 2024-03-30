from RequirementCrew import req_crew
from Tasks import *
requirements = req_crew.kickoff()
print(req.output.raw_output, "\n")

from FileStructureCrew import file_structure_crew
file_structure = file_structure_crew.kickoff()
from FileStructureTasks import *
print(file_structure_task.output.raw_output,"\n")
print(verifiy_file_structure_task.output.raw_output)