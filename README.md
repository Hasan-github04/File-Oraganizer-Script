# File-Oraganizer-Script
This Python script automatically organizes files in a specified directory by categorizing them into predefined folders based on their file types. It helps keep directories clean and structured by moving files into appropriate subfolders.

How It Works:

1. File Categorization – The script classifies files into categories such as Documents, Images, Videos, Audio, Archives, Executables, and Others, based on their extensions.
2. Directory Scanning – It scans the target folder (TARGET_FOLDER) for all files while ignoring subdirectories.
3. Sorting and Moving – Each file is moved into its respective category folder, which is created if it does not already exist.
4. Logging – After organizing, the script displays a summary of how many files were moved and their new locations.

You can modify the FILE_CATEGORIES dictionary to add or remove file types based on your needs. Supports easy expansion for additional file formats and categories.
