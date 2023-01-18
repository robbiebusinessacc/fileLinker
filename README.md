# fileLinker

The File Linker is a Python script that allows you to easily import and run Python files in a specified subdirectory.

# Usage

1. Place the fileLinker.py script in the same directory as the subdirectory containing the Python files you wish to import.

2. Run the script by calling fileLinker() or by running the script in your command line/terminal.

3. The script will print a list of all Python files in the specified subdirectory (by default, the subdirectory is named "new").

4. Enter the number of the file you wish to import and run. The script will attempt to import and run the selected file.

5. If the file is not found or there is an error in the file, the script will print a message to the console.

# Customization

You can customize the script to change the name of the subdirectory by modifying the following line of code:
`sys.path.insert(0,'./new')`
To specify a different subdirectory, simply replace './new' with the path to your desired subdirectory.

# Note

Please be careful when running unknown python files from other sources as it can be harmful.

# Contributing

If you have any ideas or suggestions for improvements to the File Linker, please feel free to create a pull request or open an issue.

# License

This project is licensed under the terms of the MIT license.


