String finder

============

Description:
------------
This script scans all files within a specified directory for a target string. Once the scan is complete, the script lists all files containing the target string.

How to use:
-----------
1. Run the script.
2. When prompted, enter the path to the directory you wish to search.
3. Enter the target string you want to find.
4. The script will then scan all the files within the specified directory for the given string and display any matching file paths.

Functions:
----------
- scan_files_for_string(directory, target_string): This function scans all files in a directory for a specific string. It returns a list of files containing the target string.

Parameters:
-----------
- directory: The path to the directory to scan.
- target_string: The string to search for.

Usage:
------
To use the script directly:

$ python [script_name].py

Enter the required inputs when prompted.

Notes:
------
- The script reads files using the utf-8 encoding. Files that do not adhere to this encoding or have other read issues will be skipped.
- If there's an error reading a file, or if the file type isn't readable as text (binary files, for instance), the script will simply skip it and continue.

