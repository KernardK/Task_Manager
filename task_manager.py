"""
Progarm Name: task_manger.py
Written by: Kernard
Date: 05 APril 2020
Purpose: This program is for a small business that can help it to manage tasks assigned to each member of the team.
"""
# Import modules.
from datetime import datetime
user_file = "user.txt"
tasks_file = "tasks.txt"
user_overview = "user_overview.txt"
task_overview = "task_overview.txt"
# Boolean initial states.
login = False
register = False

# Formatted dates.
date = datetime.now()
today = date.strftime("%d %B %Y")

# Tasks status initial value
task_complete = "No"

# Menu options for other users.
menu_msg = """Please select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
"""

# Menu options for admin.
admin_menu_msg = """Please select one of the following options:
r  - register user
a  - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds  - statistics
e  - exit
"""

# Formatted message for tasks.
view_all_msg = "All Tasks:"
task_edit_option = """mc - Mark the task as complete
edt - Edit the task
"""

# count values
count = 1
counter = 0
num_of_users = 0
menu_choice = ""

# Input for users.
username = input("Please enter your username: ")
password = input("Please enter your password: ")


# Displays the appropriate menu choice to each user.
def menu():
    if username == "admin":
        print(admin_menu_msg)

    else:
        print(menu_msg)
        # prompts user for selection from menu.
        menu_choice = input("Please enter your option: ")


# Registers a new user to the users.txt file
def reg_user():
    with open(user_file, "r+") as f:
        contents = f.readlines()
        register = False

        new_user = input("Please enter a username for the new user: ")
        new_password = input("Please enter a password for the new user: ")
        confirm_password = input("Please re-enter the password: ")
        # If the passwords do not match then the registration stays false and continues to re-enter the user again
        # until the password and confirm passwords match. When the passwords match the information is written to the users.txt file.
        while register == False:
            if new_password != confirm_password:
                print("The password and confirm password do not match, please re-enter passwords")
                new_password = input("Please enter a password for the new user: ")
                confirm_password = input("Please re-enter the password: ")
            elif new_user in contents:
                register = False
                print(f"The username: {new_user} already exists. Please try again.")
                new_user = input("Please enter a username for the new user: ")
                new_password = input("Please enter a password for the new user: ")
                confirm_password = input("Please re-enter the password: ")
            else:
                register = True
                f.write(new_user + ", " + new_password + "\n")


# Adds a task to the tasks.txt file.
def add_task():
    # Allows user to add a new task to the tasks.txt file.
    # The file tasks.txt is opened and asks the user to eneter the details to be added to the file,
    # when all credentials are added it writes the information in the specified format.
        with open(tasks_file, "a") as tf:
            assign_task = input("Please assign a user(username) to a task: ")
            task_title = input("Please enter a title for the task: ")
            task_desc = input("Please enter a description for the task task: ")
            task_date = today
            task_due = input("Please enter the due date for the task (eg. 10 Apr 2020): ")
            tf.write(assign_task + ", " + task_title + ", " + task_desc + ", " + task_date + ", " + task_due + ", " + task_complete + "\n")
            print("Task has been added successfully.")


# Displays all tasks assigned to a specific user.
def view_all():
    count = 1
    # Allows user to view all tasks in the tasks.txt file.
    # The tasks file.txt is opened and loops through the entire file, and displays all the tasks within the file.
    with open(tasks_file, "r") as tf:
        read_data = tf.readlines()
        print(view_all_msg)
        # splits each column into its own separate variable for easier handeling later.
        for line in read_data:
            view_list = line.split(",")
            user_col = view_list[0]
            title_col = view_list[1]
            desc_col = view_list[2]
            date_col = view_list[3]
            due_date = view_list[4]
            completed_col = view_list[5]
            print(f"""Task {count}.
                User: {user_col}
                Title: {title_col}
                Description: {desc_col}
                Assigned Date:{date_col}
                Due Date: {due_date}
                Task Completed: {completed_col}""")
            count += 1

# Allows the admin user to assign new users to a task and to assign a task completed.
def view_mine():
    username = input("Please enter the username which you want to view the tasks for?\n")
    task_number = 0
    with open('tasks.txt', 'r') as tf:
        view_list = tf.read()
    for row in view_list:
            field = row.strip().split(",")
            user_col = view_list[0]
            title_col = view_list[1]
            desc_col = view_list[2]
            date_col = view_list[3]
            due_date = view_list[4]
            completed_col = view_list[5]
            task_number += 1
            if username == user_col:
                print(f"""\nTask Number: {task_number}.\nUsername: {user_col}\nTitle: {title_col}
                \nDescription: {desc_col}\nDate Assigned: {date_col}\nDue Date: {due_date}\n Completed: {completed_col}""")

    # Allows the user to edit the user and task completion or exit the option.
    edit_task = input("Would you like edit a task? (edit) or return to the menu? (-1): ")

    # Allows the user to edit the task completion column.
    def edit_completed(task_complete):
        users_task = task_f[task_num].strip().split(", ")
        new_task = task_f[task_num].strip().replace(users_task[5], task_complete)
        print(new_task)
        updated_task = view_list.replace(task_f[task_num].strip(), new_task)
        with open('tasks.txt', 'w') as f:
            f.write(updated_task)
    # Allows the user to assign a new user to a task.
    def edit_user(new_user):
        users_task = task_f[task_num].strip().split(", ")
        new_task = task_f[task_num].strip().replace(users_task[0], new_user)
        print(new_task)
        updated_task = view_list.replace(task_f[task_num].strip(), new_task)
        with open('tasks.txt', 'w') as tf:
            tf.write(updated_task)

    # If the users selects 'edit' then allows the user to edit the task.
    if edit_task == "edit":
        task_num = int(input("Please enter the task number you would like to edit: "))
        task_num = task_num - 1
        with open('tasks.txt', 'r') as tf:
            task_f = tf.readlines()
            for line in task_f:
                print(task_f[task_num])
                break

        # Allows the user to edit the username assigned to the task or the task completion.
        edit_choice = input("would you like to assign a new user to the task (user) or mark a task as complete (comp): ")

        # If the users selects 'user' then allows the user to edit the username assigned to the task.
        if edit_choice == "user":
            new_user = input("Please assign a new user to this task (please enter their username): ")
            edit_user(new_user)
        # If the users selects 'comp' then allows the user to edit the task completed column.
        elif edit_choice == "comp":
            task_complete = input("Has the task been completed? (Yes): ").capitalize()
            if task_complete == "Yes":
                edit_completed(task_complete)
            else:
                print("Sorry invalid input, Please try again.")

    # If the user enters '-1' it takes the user back to the menu.
    elif edit_task == "-1":
        menu()
        # prompts user for selection from menu.
        menu_choice = input("Please enter your option: ")



# Function to generate reports related to all tasks and users.
def generate_reports():
        # Writes the information to the new task_overview.txt file.
        # Opens file and allows it to be read only.
        with open(tasks_file, "r+") as tf:
            task_count = 0
            complete_tasks = 0
            incomplete_tasks = 0
            overdue_tasks = 0
            overdue_incomplete_tasks = 0
            task_data = tf.readlines()
            # splits each column into its own separate variable for easier handeling later.
            for line in task_data:
                view_list = line.replace("\n", "").split(", ")
                user_col = view_list[0]
                title_col = view_list[1]
                desc_col = view_list[2]
                date_col = view_list[3]
                due_date = view_list[4]
                completed_col = view_list[5]

                # Counts the number of tasks in the file.
                task_count += 1

                # checks if the task has been completed in the 'completed_col'.
                if completed_col == "Yes":
                    complete_tasks += 1
                else:
                    incomplete_tasks += 1

                # Converts the date_col into a datetime format to check if the due_date column's date has passed
                convert_date_col = datetime.strptime(
                    due_date, "%d %B %Y").date()
                today_converted_date = datetime.strptime(
                    today, "%d %B %Y").date()

                if today_converted_date > convert_date_col:
                    overdue_tasks += 1

                # Calculates the number of overdue and incomplete tasks.
                if completed_col == "No" and today_converted_date > convert_date_col:
                    overdue_incomplete_tasks += 1

                # Calculates the percentage of uncompleted tasks.
                incomplete_percentage = round(
                    (incomplete_tasks / task_count) * 100)
                # Calculates the percentage of uncompleted tasks.
                overdue_percentage = round((overdue_tasks / task_count) * 100)

                # Calculates the percentage of incomplete tasks.
                if incomplete_tasks == 0:
                    incomplete_percentage = 0
                else:
                    incomplete_percentage = incomplete_percentage

                # Calculates the percentage of overdue tasks.
                if overdue_percentage == 0:
                    overdue_percentage = 0
                else:
                    overdue_percentage = overdue_percentage


            # Creates the task_overview.txt file and writes the information into the file.
            with open(task_overview, "w+") as to:
                header_1 = "The total number of tasks: "
                header_2 = "The total tasks completed: "
                header_3 = "The total incomplete tasks: "
                header_4 = "The total incomplete and overdue tasks: "
                header_5 = "The percentage of incomplete tasks: "
                header_6 = "The percentage of overdue tasks: "

                # Writes the information into the 'tasks_overview.txt' file in the prescribed format.
                to.writelines(header_1 + str(task_count) + "\n"
                              + header_2 + str(complete_tasks) + "\n"
                              + header_3 + str(incomplete_tasks) + "\n"
                              + header_4 + str(overdue_tasks) + "\n"
                              + header_5 +
                              str(incomplete_percentage) + "%" + "\n"
                              + header_6 + str(overdue_percentage) + "%" + "\n")

        print("Task_Overview file has been generated successfully")
    # Writes the information to the new task_overview.txt file.
        user_count = 0
        user_counter = 0
        tasks = 0
        user_task_count = 0
        user_incomplete_tasks = 0
        user_overdue_tasks = 0
        # Opens the user text file and allows it to be read.
        with open(user_file, "r") as f:
            user_data = f.readlines()
            # splits each column into its own separate variable for easier handeling later.
            for line in user_data:
                view_list = line.replace("\n", "").split(", ")
                username_col = view_list[0]
                password_col = view_list[1]
                user_count += 1
            print(user_count)

        # Opens file and allows it to be read only.
        with open(tasks_file, "r") as tf:
            task_data = tf.readlines()
            users = {}
            user_complete = {}
            user_incomplete = {}
            user_overdue = {}
            # splits each column into its own separate variable for easier handeling later.
            for line in task_data:
                view_list = line.replace("\n", "").split(", ")
                user_col = view_list[0]
                title_col = view_list[1]
                desc_col = view_list[2]
                date_col = view_list[3]
                due_date = view_list[4]
                completed_col = view_list[5]

                tasks += 1

                # stores how many tasks are assigned to each user in a dictionary.
                if user_col in users:
                    users[user_col] += 1
                else:
                    users[user_col] = 1

                # stores how many tasks are assigned to each user are completed a dictionary.
                if user_col in user_complete and completed_col == "Yes":
                    user_complete[user_col] += 1
                else:
                    user_complete[user_col] = 0

                if user_col in user_incomplete and completed_col == "No":
                    user_incomplete[user_col] += 1
                else:
                    user_incomplete[user_col] = 0

                # Calculates the total number of incomplete tasks
                # Converts the date_col into a datetime format to check if the due_date column's date has passed
                convert_date_col = datetime.strptime(
                    due_date, "%d %B %Y").date()
                today_converted_date = datetime.strptime(
                    today, "%d %B %Y").date()

                if today_converted_date > convert_date_col and completed_col == "No":
                    user_overdue[user_col] += 1
                else:
                    user_overdue[user_col] = 0

            # Calculates the percentage of tasks for each value in each dictionary.
            sum_of_dict = sum(users.values())
            complete_sum_dict = sum(user_complete.values())
            incomplete_sum_dict = sum(user_incomplete.values())
            overdue_sum_dict = sum(user_overdue.values())

            # Creates the task_overview.txt file and writes the information into the file.
            with open(user_overview, "w+") as uf:

                # Heading for Incomplete Tasks.
                print(f"Total Tasks: {tasks}\n")
                print(f"Tasks assigned to each user: {users}")

                # Heading for Incomplete Tasks.
                print("Percentage of tasks: \n")
                # Calculates the percentage of each tasks for each value in the dictionary.
                for key, values in users.items():
                    if values == 0:
                        user_task_percentage = 0
                    else:
                        user_task_percentage = round(
                            (values / sum_of_dict) * 100)

                    # Writes the values to the file and displays to the user.
                    uf.writelines("Number of tasks percentage: " +
                                  str(key) + ": " + str(values) + "\n")
                    print(f"{key}: {user_task_percentage}%\n")

                # Heading for Incomplete Tasks.
                print("Percentage of complete tasks: \n")
                # Calculates the percentage of complete tasks for each value in the dictionary.
                for k, v in user_complete.items():
                    if v == 0:
                        user_complete_percentage = 0
                    else:
                        user_complete_percentage = round(
                            (v / complete_sum_dict) * 100)

                    # Writes the values to the file and displays to the user.
                    uf.writelines(
                        "Number of complete tasks percentage: " + str(k) + ": " + str(v) + "%" + "\n")
                    print(f"{k}: {user_complete_percentage}%\n")


                # Heading for Incomplete Tasks.
                print("Incomplete Tasks: \n")
                # Calculates the percentage of incomplete tasks for each value in the dictionary.
                for i, val in user_incomplete.items():
                    if val == 0:
                        user_incomplete_percentage = 0
                    else:
                        user_incomplete_percentage = round(
                            (val / incomplete_sum_dict) * 100, 2)

                    # Writes the values to the file and displays to the user.
                    uf.writelines(
                        "Number of incomplete tasks percentage: " + str(i) + ": " + str(val) + "%" + "\n")
                    print(f"{i}: {user_incomplete_percentage}%\n")


                # Heading for Incomplete Tasks.
                print("Percentage of overdue tasks: \n")
                # Calculates the percentage of overdue tasks for each value in the dictionary.
                for o, va in user_overdue.items():
                    if va == 0:
                        overdue_percentage = 0
                    else:
                        overdue_percentage = round(
                            (va / overdue_sum_dict) * 100)

                    # Writes the values to the file and displays to the user.
                    uf.writelines(
                        "Number of overdue and incomplete tasks percentage: " + str(i) + ": " + str(val) + "%" + "\n")
                    print(f"{o}: {overdue_percentage}%\n")


            # Creates the task_overview.txt file and writes the information into the file.
            with open(user_overview, "a+") as uf:
                # Texts to be printed to the users_overview.txt file
                header_1 = "The total number of tasks: "
                header_2 = "The tasks assigned to each user: "
                header_3 = "Percentage of completed tasks: "
                header_4 = "Percentage of incomplete tasks: "
                header_5 = "Percentage of incomplete and overdue tasks: "

                # Writes the information into the 'tasks_overview.txt' file in the prescribed format.
                uf.writelines(header_1 + str(tasks) + "\n"
                              + header_2 + str(users) + "\n"
                              + header_3 + str(user_complete) + "\n"
                              + header_4 + str(user_incomplete) + "\n"
                              + header_5 + str(user_overdue) + "\n")

            print(f"{users}\n{user_complete}\n{user_incomplete}\n{user_overdue}")
        print("Task_Overview file has been generated successfully")


# Displays all of the information in the task file from the task_overview.txt file and user_overview.txt file.
def display_statistics():

    print("Task Overview File Info")
    # Opens file and allows it to be read only.
    with open(task_overview, "r") as tf:
        task_data = tf.readlines()
        # splits each column into its own separate variable for easier handeling later.
        for lines in task_data:
            lines.strip()
            print(lines)

    print("=======End of Task Overview File Info======\n")


    print("User Overview File Info")
    # Opens file and allows it to be read only.
    with open(user_overview, "r") as uf:
        user_data = uf.readlines()
        # splits each column into its own separate variable for easier handeling later.
        for line in user_data:
            line.strip()
            print(line)

    print("======= End of User Overview File Info ======")





# Opens users.txt file.
with open(user_file, "r+") as f:
    contents = f.read()
    while login == False:
        if username not in contents or password not in contents:
            print("Invalid credentials entered. Please enter a valid username and password.")
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")

        # Checks that the credentials entered by the user are in the users.txt file.
        # If the user is admin then the admin's menu options are displayed, if user is not admin a different set of options are displayed.
        if username in contents and password in contents:
            login = True
            # prompts user for selection from menu.
            menu()
            menu_choice = input("Please enter your option: ")

            # Calls the functions depending on the menu entered.
            if menu_choice == "r":
                reg_user()
            elif menu_choice == "a":
                add_task()
            elif menu_choice == "va":
                view_all()
            elif menu_choice == "vm":
                view_mine()
            elif menu_choice == "gr":
                generate_reports()
            elif menu_choice == "ds":
                display_statistics()
            else:
                print("Sorry invalid input please try again. ")


