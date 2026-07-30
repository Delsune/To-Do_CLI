MENU = ("===============================\n"
        + "|   Command-Line To-Do List   |\n"
        + "|  *please make a selection*  |\n"
        + "|                             |\n"
        + "| 1 = Add/Remove Task         |\n"
        + "| 2 = Save Tasks to File      |\n"
        + "| 3 = Load Tasks from File    |\n"
        + "| 4 = View Tasks              |\n"
        + "===============================")
tasks = []
in_progress = True


def task_editing():
    try:
        amount = int(input("How many tasks? "))
    except ValueError:
        print("That is not an integer.")
        exit()

    mode = input("Adding or Removing? ").lower().strip()

    match mode:
        case "adding":
            for i in range(amount):
                tasks.append(input().strip() + "\n")

        case "removing":
            if amount > len(tasks):
                print("You cannot remove more than what have in your list, "
                      + "please restart the app.")
                exit()

            try:
                for i in range(amount):
                    tasks.remove(input().strip() + "\n")
            except ValueError:
                print("Could not remove something that doesn't exist in "
                      + "the list, please restart the app.")
                exit()

        case _:
            print("That is not an option, please restart the app.")


def is_finished():
    complete = input("Are you done? (Y or N)\n").upper().strip()

    match complete:
        case "Y":
            print("Thank you using Delsune's Command-Line To-Do List.")
            exit()

        case "N":
            in_progress = True

        case _:
            print("That is not an option, defaulting to completed.")
            exit()


while in_progress:
    try:
        choice = int(input(MENU + "\n"))
    except ValueError:
        print("That is not an option, please enter an integer value and "
              + "try again.")
        exit()

    match choice:
        case 1:
            task_editing()
            is_finished()

        case 2:
            with open("To-Do List.txt", 'w+') as file:
                file.writelines(tasks)

            print("To-Do list saved to file.")
            is_finished()

        case 3:
            with open("To-Do List.txt", 'r+') as file:
                tasks = file.readlines()

            print("To-Do list loaded from file.")

            is_finished()

        case 4:
            print(tasks)
            is_finished()
