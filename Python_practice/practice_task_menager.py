from venv import create


user_choice = -1
tasks = []

def show_tasks():
    task_index = 0
    for task in tasks:
        print(task + " [" + str(task_index)+ "]")
        task_index +=1

def add_tasks():
    task = input("wpisz tresc zadania: ")
    tasks.append(task)
    print("Zadanie zostało dodane")

def remove_tasks():
    show_tasks()
    tasks_index = int(input("Podaj index do usuniecia: "))
    if tasks_index > 0 and tasks_index > len(tasks) -1:
        print("Zadanie takie nie istnieje")
        return
    else:
        tasks.pop(tasks_index)
        print("Usunieto zadanie, moj Panie")

def save_tasks():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")

def load_tasks_from_file():
    try:
        file = open("tasks.txt")
        for line in file.readlines():
            tasks.append(line.strip())
        file.close()
    except:
        return

load_tasks_from_file()

while user_choice != 5:
        if user_choice == 1:
            show_tasks()

        if user_choice == 2:
            add_tasks()

        if user_choice == 3:
            remove_tasks()

        if user_choice == 4:
            save_tasks()

        if user_choice < 1 or user_choice > 6:
            print ("Podaj Liczbe od 1 do 5 \n")
           
        if user_choice == 6:
            save_tasks()
            break

        print()
        print ("1. Pokaż zadania")
        print ("2. Dodaj zadanie")
        print ("3. Usuń zadanie")
        print ("4. Zapisz zmiany do pliku")
        print ("5. Wyjdż")
        print ("6. Zapisz i wyjdz")

        try:
            user_choice = int(input("Wybierz liczbe: "))
            print()
        except ValueError:
            print("\nPodałeś litere zamiast liczby byczku" )
