import csv
print("\t\tWelcome to your To-Do list App\n")
print("1. Add Task")
print("2. View Task")
print("3. Mark Task as Done")
print("4. Delete Task")
print("5. Exit")

case = int(input("\n\nPlease enter your choice: "))
todo = "todo.csv"

if case == 1:
    print("You have choose to add task")
    n = int(input("Plz enter how many task you want to add:"))
    for i in range(1, n+1):
        with open(todo, "a", newline='') as file:
            writer = csv.writer(file)
            due = input("DUE DATE: ")
            task = input("TASK:")
            status = input("STATUS:")
            writer.writerow([due, task, status])

elif case == 2:
    print("You have choose to view task")
    with open("todo.csv", "r") as file:
        reader = csv.reader(file)

        print(f"{'DUE DATE':<15} {'TASK':<20} {'STATUS':<15}")
        print("-" * 50)
        for row in reader:
            if len(row) < 3:
                continue
            print(f"{row[0]:<15} {row[1]:<20} {row[2]:<15}")

elif case == 3:
    print("You have choose mark task done")
    update = input("Enter Task want to marked as done:")
    new = []
    found = False
    with open(todo, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1].lower() == update.lower():
                row[2] = 'Done'
                found = True
            new.append(row)
    with open(todo, "w", newline='')as file:
        writer = csv.writer(file)
        writer.writerows(new)
    if found:
        print("Updated")
    else:
        print("No Such Task")

elif case == 4:
    print("You have choose to delete task")
    update = input("Enter Task want to delete:")
    new = []
    with open(todo, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1].lower() == update.lower():
                print("Deleted")
                continue
            else:
                new.append(row)
    with open(todo, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new)

elif case == 5:
    print("You choose to exit ")

else:
    print("Enter Valid choice ")
