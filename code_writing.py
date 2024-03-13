from utils.filepaths import extract_file_paths
from utils.create_file import create_files
from file_creation_crew import filepaths, file_description,  model
import time
from utils.writeCode import writeCode

filePaths = extract_file_paths(filepaths)

for file in filePaths:
    print(file)
# # creating files.
create_files(filePaths)

for filepath in filePaths:
    prompt = f"""Given the description of the all the files of the Project. 
    Description:
    {file_description}

    Generate code for file: {filepath} according to the description. Make sure to import neccessary classes and functions from other files. Return Code only.
    """

    result = model.generate_content(prompt)

    writeCode(result.text, filepath)

    # print(f"Code for {filepath}: \n\n")
    # print(result.text)
    # print("\n\n\n")
    time.sleep(2)