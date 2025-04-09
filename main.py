import json
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

TASKS_FILE = "tasks.json"
USERNAME = "thekanhakodes"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(Fore.GREEN + f"\n✅ Task added: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print(Fore.YELLOW + "\n📭 Your task list is empty.\n")
        return
    print(Fore.CYAN + f"\n📋 {USERNAME}'s To-Do List:\n" + "-"*35)
    for i, task in enumerate(tasks, start=1):
        status = Fore.GREEN + "✅" if task["done"] else Fore.RED + "❌"
        print(f"{Fore.WHITE}{i}. {task['task']} [{status}]")
    print("-"*35)

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(Fore.GREEN + f"\n🎉 Task marked as done: {tasks[index]['task']}")
    else:
        print(Fore.RED + "\n⚠️ Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(Fore.MAGENTA + f"\n🗑️ Task deleted: {removed['task']}")
    else:
        print(Fore.RED + "\n⚠️ Invalid task number.")

def show_menu():
    print(Fore.BLUE + Style.BRIGHT + f"\n📌 TO-DO CLI APP | by @{USERNAME}")
    print(Fore.WHITE + "-" * 40)
    print("1️⃣  Add Task")
    print("2️⃣  List Tasks")
    print("3️⃣  Mark Task as Done")
    print("4️⃣  Delete Task")
    print("5️⃣  Exit")
    print("-" * 40)

def print_welcome():
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + f"\n🚀 Welcome to {USERNAME}'s Fancy To-Do CLI 💙\n")

def print_goodbye():
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"\n👋 Bye, thanks for using @{USERNAME}'s app. Stay productive!\n")

if __name__ == "__main__":
    print_welcome()
    while True:
        show_menu()
        choice = input(Fore.YELLOW + "\n🔘 Enter your choice: ")

        if choice == "1":
            task = input(Fore.CYAN + "📝 Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            try:
                index = int(input(Fore.CYAN + "✔️  Enter task number to mark as done: ")) - 1
                mark_done(index)
            except ValueError:
                print(Fore.RED + "⚠️ Invalid input. Please enter a number.")
        elif choice == "4":
            try:
                index = int(input(Fore.CYAN + "❌ Enter task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print(Fore.RED + "⚠️ Invalid input. Please enter a number.")
        elif choice == "5":
            print_goodbye()
            break
        else:
            print(Fore.RED + "⚠️ Invalid choice. Try again.")
