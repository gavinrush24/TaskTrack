# TaskTrack

TaskTrack is a command-line task manager created for CPS 310.

## Current Features

- display main menu
- add tasks to a to-do list 
- display tasks that you have added to the list
- Save tasks to a seperate file so they don't dissapear when the program closes

## Requirements

-Python 3

## Project Files

-`tasktrack.py` — the main python code that handles the menu, adding tasks, viewing the list, and file I/O\

-`tasks.txt` — File to store tasks once aded to task list

-`.gitignore` — any type of file that you want Git to ignore when commiting and pushing 

## Running the Program

Go into options and go Terminal->New Terminal 
```text
python tasktrack.py
```

## Task Persistence

Tasks are loaded when the program is ran and saved once the task is entered using the "Add task" feature

## Sample Interaction

```text
python tasktrack.py

TaskTrack - Task Manager
1. View tasks
2. Add task
3. Exit
Enter choice: 2
Enter a new task: Complete ICA04 assignment
Task added successfully.

TaskTrack - Task Manager
1. View tasks
2. Add task
3. Exit
Enter choice: 1

Tasks:
1. Complete ICA04 assignment
```

## Current Limitation

Cannot remove a task when completed 

## Version Control

This project uses Git as its local version control and GitHub as an online repository. To change something locally use 'commit' and when you want to update the online repo use 'push'. When downloading something from the repo use 'pull'