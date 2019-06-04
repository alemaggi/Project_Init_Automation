#!/bin/bash

cd
python3 /Users/alessandromaggi/Documents/MyProjects/Project_Init_Automation/create.py $1
cd /Users/alessandromaggi/Documents/MyProjects/$1
git init
git remote add origin https://github.com/alemaggi/$1.git
touch README.md
git add .
git commit -m "Initial commit"
git push -u origin master
code .
