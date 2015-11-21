from os import path, walk, chdir

def _getPath(location):
    assert location, 'location is not a string or is empty'

    fileArrayList = []
    chdir(location)
    for root, dirs, files in walk(location):
        for file in files:
            fileArrayList.append(file)

    return fileArrayList

def compare_Files(location1, location2):
    fileArray = _getPath(location1)
    fileArray2 = _getPath(location2)

    return fileArray2 == fileArray
