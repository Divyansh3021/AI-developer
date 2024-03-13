import os

def create_files(file_paths):
    for path in file_paths:
        try:
            # Extract directory path from the file path
            directory = os.path.dirname(path)
            
            # Create the directory if it doesn't exist
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Directory '{directory}' created successfully.")
            
            # Create the file
            with open(path, 'w') as file:
                print(f"File '{path}' created successfully.")
        except Exception as e:
            print(f"Error occurred while creating file '{path}': {e}")