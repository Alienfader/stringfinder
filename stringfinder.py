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

if __name__ == '__main__':
    directory_to_search = input('Enter the directory path to search in: ')
    string_to_search = input('Enter the string to search for: ')
    
    result = scan_files_for_string(directory_to_search, string_to_search)
    
    if result:
        print(f"Files containing '{string_to_search}':")
        for r in result:
            print(r)
    else:
        print(f"No files found containing '{string_to_search}' in {directory_to_search}")