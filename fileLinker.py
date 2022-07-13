#file linker
def fileLinker():
	import glob,sys #imports
	sys.path.insert(0,'./new')#subdirectory
	files=[file.replace('new\\',"") for file in glob.glob("new/*.py") if file!='fileLinker.py']#list of files
	for i in range(len(files)):print(i,files[i])#prints list of files
	try:exec("import "+files[int(input('file number: '))])#runs file 
	except:print('no file found or error in file')#prints that if there is no file found or error in file
fileLinker()