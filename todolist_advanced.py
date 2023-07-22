#======================================================================================================================
# Programmer: Jaydon Thompson
# Program: 4
# Date: 7/22/2023
# Description: Creates a basic GUI application to show a to-do-list where users can add, edit, and delete tasks.
#======================================================================================================================

#-------------------------------- LIBRARY IMPORT --------------------------------

import tkinter as tk
from tkinter import messagebox

#-------------------------------- FUNCTIONS --------------------------------------

# Adds a new task to the list
def add_task():
    task = entry_task.get()
    priority = combo_priority.get()
    due_date = entry_due_date.get()

    if task and priority and due_date:
        task_list.insert(tk.END, f"Task: {task} | Priority: {priority} | Due Date: {due_date}")
        entry_task.delete(0, tk.END)
        entry_due_date.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please fill in all the task details!")

# Edits a selected task in the list
def edit_task():
    try:
        index = task_list.curselection()[0]
        task_details = task_list.get(index)
        task, priority, due_date = extract_task_details(task_details)

        entry_task.delete(0, tk.END)
        entry_task.insert(tk.END, task)

        combo_priority.set(priority)

        entry_due_date.delete(0, tk.END)
        entry_due_date.insert(tk.END, due_date)

        delete_task()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit!")

# Deletes a selected task in the list
def delete_task():
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Marks a selected task as completed or active
def mark_as_completed():
    try:
        index = task_list.curselection()[0]
        task_details = task_list.get(index)
        task, priority, due_date = extract_task_details(task_details)

        if task.endswith(" (Completed)"):
            task = task[:-12]  # Remove the "(Completed)" suffix
        else:
            task += " (Completed)"

        task_list.delete(index)
        task_list.insert(index, f"Task: {task} | Priority: {priority} | Due Date: {due_date}")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

# Extracts task details from the listbox item text
def extract_task_details(task_details):
    parts = task_details.split("|")
    task = parts[0].strip()[6:]
    priority = parts[1].strip()[10:]
    due_date = parts[2].strip()[11:]
    return task, priority, due_date

# Shows an "About" page in a pop up window.
def show_about_page():
    about_text = '''                 To-Do-List Application 
    \n                 Created By: ###### OMITTED FOR ONLINE SECURITY PURPOSES ######
    \n                 Version: Advanced 1.5
    \nInstructions: 
    \nStep 1: Enter your task in the white box next to "Task:" 
    \nStep 2: Select a priority from the drop-down menu.
    \nStep 3: Enter a due date. Any input is allowed, though it is recommended to use a standard date format for ease of use.
    \nStep 4: Click "Add Task."
    \n                 To Delete/Mark as complete: 
    \nSelect your task in the box after adding it, and click the button.
    \n                 To Edit: 
    \nSelect your task and click "Edit Task", then the information will be dragged back into the task, priority, and due date sections. Edit them there.
    \n
    \nTo see this message without constantly clicking, go to https://github.com/Etzerlume/To-Do-List_pytkinter/blob/main/README.md.
    '''
    messagebox.showinfo("About", about_text)

#-------------------------------- MAIN APP, LISTBOX, AND SCROLLBAR --------------------------------------

app = tk.Tk()
app.title("To-Do List Application")

frame_tasks = tk.Frame(app)
frame_tasks.pack(pady=10)

# Creates a listbox widget to display tasks.
# The listbox can hold 60 characters and 10 lines, a scrollbar is also added to handle vertical scrolling using the yscrollcommand option.

task_list = tk.Listbox(frame_tasks, width=60, height=10)
task_list.grid(row=0, column=0, padx=10, pady=5, rowspan=4)

scrollbar = tk.Scrollbar(frame_tasks, orient=tk.VERTICAL)
scrollbar.config(command=task_list.yview)
scrollbar.grid(row=0, column=1, sticky="ns", rowspan=4)

task_list.config(yscrollcommand=scrollbar.set)

#-------------------------------- FOR INPUT WIDGETS --------------------------------------

# Creates a frame to hold the input widgets for adding/editing tasks.
frame_input = tk.Frame(app)
frame_input.pack(pady=10)

# Task Label
label_task = tk.Label(frame_input, text="Task:")
label_task.grid(row=0, column=0, padx=5)

# Task Entrybox
entry_task = tk.Entry(frame_input, width=40)
entry_task.grid(row=0, column=1, padx=5)

# Priority Label
label_priority = tk.Label(frame_input, text="Priority:")
label_priority.grid(row=0, column=2, padx=5)

# Priority Label Dropdown
combo_priority = tk.StringVar()
combo_priority.set("High")  # Default priority is High
priority_choices = ["High", "Medium", "Low"]
dropdown_priority = tk.OptionMenu(frame_input, combo_priority, *priority_choices)
dropdown_priority.grid(row=0, column=3, padx=5)

# Due Date Label
label_due_date = tk.Label(frame_input, text="Due Date:")
label_due_date.grid(row=0, column=4, padx=5)

# Due Date Entrybox
entry_due_date = tk.Entry(frame_input, width=20)
entry_due_date.grid(row=0, column=5, padx=5)

#-------------------------------- INPUT WIDGET CREATION -------------------------------- 
# Create buttons to add, edit, and delete tasks. Also creates a button to mark tasks as completed.
# The columnspan option is used to span multiple columns to ensure proper layout.

btn_add = tk.Button(frame_tasks, text="Add Task", width=15, command=add_task)
btn_add.grid(row=0, column=2, padx=5, pady=5)

btn_edit = tk.Button(frame_tasks, text="Edit Task", width=15, command=edit_task)
btn_edit.grid(row=1, column=2, padx=5, pady=5)

btn_delete = tk.Button(frame_tasks, text="Delete Task", width=15, command=delete_task)
btn_delete.grid(row=2, column=2, padx=5, pady=5)

btn_complete = tk.Button(frame_tasks, text="Mark as Completed", width=15, command=mark_as_completed)
btn_complete.grid(row=3, column=2, padx=5, pady=5)

#-------------------------------- ABOUT PAGE --------------------------------------

frame_about = tk.Frame(app)
frame_about.pack(pady=5)

btn_about = tk.Button(frame_about, text="About", width=10, command=show_about_page)
btn_about.pack()

#-------------------------------- MAIN LOOP --------------------------------------

app.mainloop()
