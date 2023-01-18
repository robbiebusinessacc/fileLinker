# This function imports the necessary modules, sets the path to a subdirectory, and creates a list of python files in that directory
def fileLinker():
    import glob,sys # imports the glob and sys modules

    # sets the path to the subdirectory 'new'
    sys.path.insert(0,'./new')

    # creates a list of files in the 'new' directory and removes the 'new\' from the file names
    files=[file.replace('new\\',"") for file in glob.glob("new/*.py") if file!='fileLinker.py']

    # prints the list of files in the 'new' directory
    for i in range(len(files)):print(i,files[i])

    # attempts to import and run the file selected by the user
    try:exec("import "+files[int(input('file number: '))])
    # if the file is not found or there is an error in the file, the following message is printed
    except:print('no file found or error in file')
fileLinker()
