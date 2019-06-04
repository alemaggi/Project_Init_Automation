import sys
import os 
from github import Github

#Project folder location
path = "/Users/alessandromaggi/Documents/MyProjects/"

#Github login information
username = ''
password = ''

def create():

    #Crate new project folder
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))

    #Logging in in Github
    user = Github(username, password).get_user()
    #Create new repository using github API
    repo = user.create_repo(folderName)
    print("Succesfully created repository")

if __name__ == "__main__":
    create()