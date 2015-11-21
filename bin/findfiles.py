import glob, os

def findFiles(str):
    os.chdir(str)
    for file in glob.glob("*"):
        print(file)
