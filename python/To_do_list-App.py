# created a functions that print out options for selections
def menu():
    print("✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔✔")
    print("\n==To-Do-List-App==\n1. Add task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Delete tasks")
    print("5. View tasks statistics")
    print("6. Mark completed tasks ✔")
    print("7. Exit")
# Created a class called Do
class Do:
    def __init__(self):     # initialize the two lists for storing tasks.
        self.choice = []  # stores the tasks.
        self.le = []    #  stores the completed tasks.
    def add(self,desk):    # create a function in the class that adds a task to the list.
        self.choice.append(desk)   # append task to the first list above.
        print(f"Task '{desk}' added successfully")   # print out the added task.
    def view(self):     # created a function that allows a user to view the added tasks.
        if self.choice:      # if the first is not empty.
            for it in self.choice:    # arrange the tasks in the first task.
                print(it)    # print out the added tasks accordingly.
        else:    # if the first list is empty.
            print("No tasks added yet.")
    def delete(self):   # created a function that allows a user to delete all the tasks.
        if self.choice:      # if the first is not empty
            self.choice.clear()    # this will erase out tasks in the first list.
            print("All tasks deleted successfully.")
        else:       # if the first list is empty
            print("No tasks available")
    def remove(self,tan):
        self.choice.remove(self.choice[tan])
        print(f"Task '{self.choice[tan]}' removed successfully")
    def statistics(self):     # created a function that allows a user to view total tasks.
        print("Tasks statistics:")
        print("Total tasks: ", len(self.choice))
        print(f"Completed tasks: {len(self.le)} ✔")
        print("Uncompleted tasks: ", len(self.choice)-len(self.le))
n = Do()   # called out the class function above and store it in a variable.
# Creating a while loop
while True:
    # called out the menu function above.
    menu()
    # Ask the user to an input.
    choice = input("Enter your choice: ").strip()  # The strip method prevent the input from space errors.
    if choice == "1":
        task = input("Enter task: ")  # Input task name.
        n.add(task)    # Added task to the add function above if the user input '1'.
    elif choice == "2":
        n.view()   # Call the view function above if input '2'.
    elif choice == "3":
        if n.choice:
            # Error handling
            try:
                for desk in n.choice:
                    print(desk)
                pen = int(input("Enter task number to remove: "))
                pen -=1
                n.remove(pen)
            except ValueError:
                print("Number only.")
            except IndexError:
                print("Invalid number.")
        else:
            print("No task available to remove.")
    elif choice == "4":
        n.delete()    # call the delete function above if input '3'.
    elif choice == "5":
       n.statistics()    # call the statistics function above if input '4'.
    elif choice == "6":
        if not n.choice:   # if no task
            print("No tasks available for completing.")
        else:
            # Error handling.
            try:
                for i in n.choice:   # arrange the tasks in the first task.
                    print(i)
                mark = int(input("Enter task number to mark ✔ complete: ").strip())  # input an index number to mark
                mark -= 1   # subtract 1 from the mark to balance hte index .
                print(f"Completed Task: {n.choice[mark]} ✔")
                n.le.append(mark)   # append to the second list.
            except ValueError:
                print("Number only please.")
            except IndexError:
                print("Task number not found.")
    elif choice == "7":
        break    # to exit the program.
    else:   # if false input.
        print("Invalid choice..........")