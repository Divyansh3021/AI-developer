import re

def extract_file_paths(input_string):
    # Define regex patterns for both formats
    pattern_format1 = r"'([^']+)'"
    pattern_format2 = r"\[([^]]+)\]"

    # Check if the input string matches format 1 or format 2
    matches_format1 = re.findall(pattern_format1, input_string)
    matches_format2 = re.findall(pattern_format2, input_string)

    if matches_format1:  # If format 1 matches
        return matches_format1
    elif matches_format2:  # If format 2 matches
        file_paths_str = matches_format2[0]
        return [path.strip() for path in file_paths_str.split(',')]
    else:
        return []


# def extract_file_paths(input_string):
#     # Define the regex pattern to match file paths
#     pattern = r'\[([^]]+)\]'
    
#     # Find all matches of the pattern in the input string
#     matches = re.findall(pattern, input_string)
    
#     if matches:
#         # Get the first match
#         file_paths = matches[0]
        
#         # Split the matched string by comma and strip whitespace
#         file_paths_list = [path.strip() for path in file_paths.split(',')]
        
#         return file_paths_list
#     else:
#         return []
