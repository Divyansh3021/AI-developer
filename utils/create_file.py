import os

def create_files(file_paths ,folder_path = "Project"):
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' created successfully.")
        
        # Iterate through each file path and create the file in the folder
        for path in file_paths:
            full_path = os.path.join(folder_path, path)
            directory = os.path.dirname(full_path)
            
            # Create the directory if it doesn't exist
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Directory '{directory}' created successfully.")
            
            # Create the file
            with open(full_path, 'w') as file:
                print(f"File '{full_path}' created successfully.")
    except Exception as e:
        print(f"Error occurred while creating files in folder '{folder_path}': {e}")