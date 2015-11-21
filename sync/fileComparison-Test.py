from nose.tools import *
from sync import FileComparison
from os import path

@raises(Exception)
def When_File_Does_Not_Exist_Throws_Exception_Test():
    _load('')

def check_Correct_Files_Test():
    currentDirectory = path.dirname(path.realpath(__file__))
    assert FileComparison.compare_Files(currentDirectory, currentDirectory) == True, "Files were not equal"
