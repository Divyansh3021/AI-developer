# def writeCode(code, file_name):
#     try:
#         with open("Project/"+file_name, 'w') as file:
#             file.write(code)
#         print(f"Python code has been written to '{file_name}' successfully.")
#     except Exception as e:
#         print(f"Error occurred while writing Python code to '{file_name}': {e}")

def writeCode(code, file_name):
    try:
        # Remove enclosing triple backticks
        code_lines = code.split('\n')
        if code_lines[0].startswith("```") and code_lines[-1].endswith("```"):
            code_lines = code_lines[1:-1]

        # Write the code to the file
        if file_name[0] == "/":
            directory = "Project"
        else:
            directory = "Project/"

        with open(directory + file_name, 'w') as file:
            file.write('\n'.join(code_lines))
        print(f"Python code has been written to '{file_name}' successfully.")
    except Exception as e:
        print(f"Error occurred while writing Python code to '{file_name}': {e}")
