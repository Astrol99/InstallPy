import subprocess
import wget
import sys
import os

def install(url, path, file):
    pass

while True:
    # Ask for path - default is path of script
    currentPath = str(input("[!] Enter the path to install {Press enter to go on with Default -> path of script}: "))
    if currentPath == " " or currentPath == "" or currentPath == None:
        currentPath = os.getcwd()