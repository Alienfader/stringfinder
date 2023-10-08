import os

def scan_files_for_string(directory, target_string):
    """
    Scans all files in a directory for a specific string.
    
    :param directory: The path to the directory to scan.
    :param target_string: The string to search for.
    :return: A list of files containing the target string.
    """
    matching_files = []

    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    if target_string in file.read():
                        matching_files.append(file_path)
            except:
                # If there's an error reading the file or if the file type isn't readable as text
                # we simply skip it and move on.
                pass

    return matching_files

def get_input_with_history(prompt, history_list):
    """
    Gets input from the user with a history option.
    
    :param prompt: The input prompt.
    :param history_list: The list maintaining history for this type of input.
    :return: User's input.
    """
    print(prompt)
    for i, previous_input in enumerate(history_list, 1):
        print(f"{i}. {previous_input}")
    user_input = input("Your choice or new input: ")
    if user_input.isdigit() and 0 < int(user_input) <= len(history_list):
        return history_list[int(user_input) - 1]
    else:
        history_list.append(user_input)
        return user_input

if __name__ == '__main__':
    directory_history = []
    string_history = []
    
    directory_to_search = get_input_with_history('Enter the directory path to search in or choose from history:', directory_history)
    string_to_search = get_input_with_history('Enter the string to search for or choose from history:', string_history)
    
    result = scan_files_for_string(directory_to_search, string_to_search)
    
    if result:
        print(f"Files containing '{string_to_search}':")
        for r in result:
            print(r)
    else:
        print(f"No files found containing '{string_to_search}' in {directory_to_search}")
