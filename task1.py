# todo_list.py

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_todo_list(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task(todo_list):
    task = input("Enter the task to add: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task(todo_list):
    view_todo_list(todo_list)
    if not todo_list:
        return
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")                                                                        
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
