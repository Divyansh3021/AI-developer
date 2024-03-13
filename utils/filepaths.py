import re

def extract_file_paths(input_string):
    # Define the regex pattern to match file paths
    pattern = r'\[([^]]+)\]'
    
    # Find all matches of the pattern in the input string
    matches = re.findall(pattern, input_string)
    
    if matches:
        # Get the first match
        file_paths = matches[0]
        
        # Split the matched string by comma and strip whitespace
        file_paths_list = [path.strip() for path in file_paths.split(',')]
        
        return file_paths_list
    else:
        return []

# # Example string
# input_string = "[calculator/__init__.py, calculator/addition.py, calculator/division.py, calculator/multiplication.py, calculator/subtraction.py, calculator/user_interface.py, calculator/error_handling.py, tests/test_addition.py, tests/test_division.py, tests/test_multiplication.py, tests/test_subtraction.py, tests/test_user_interface.py, documentation/user_guide.md, documentation/developer_guide.md, setup.py]"

# # Extract file paths using the function
# file_paths = extract_file_paths(input_string)
# print("File paths extracted:")
# for path in file_paths:
#     print(path)
