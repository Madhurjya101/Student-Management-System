
print("\n\n-------------Students Management System------------- ")

def add_student():
    while True:
        try:
            raw_name = input("\nEnter the name of the student : ")
            name = raw_name.title()
        except KeyboardInterrupt:
            print("\nPlease try again....")
            continue
        except Exception:
            print("Please try again....")
            continue
        try:
            cls = int(input("\nEnter the class of the student : \n"))
            if cls<1 or cls>12:
                print("\nPlease enter a valid class !!\n")
                continue
            break
        except KeyboardInterrupt:
            print("\nPlease try again....")
            continue
        except Exception:
            print("\nPlease enter a valid class !!\n")
            continue
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []
    roll = len(lines)+1
    with open("students.txt", "a") as a:
        a.write(f"Name - {name} | Roll number - {roll} | Class - {cls}\n")
        print("\nAddition completed\n")
        return



def view_student():
    try:
        with open("students.txt", "r") as f:
            a = f.read()
            if a.strip() == "":
                print("\nNo student found !!\n")
                return
            else:
                print(a)
                return
    except FileNotFoundError:
        print("\nFile not found.... please try again !!\n")
        return



def delete_student():
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No student found !!")
        return
    while True:
        try:
            user_delete = input("\nEnter the system which you choose to delete any student's data (By name/ By roll) : ")
            if user_delete.lower() == "by name":
                break
            if user_delete.lower() == "by roll":
                break
            else:
                print("\nPlease enter a valid system !!")
                continue
        except KeyboardInterrupt:
            print("\nPlease try again.....")
            continue
    new_lines = []
    if user_delete.lower() == "by name":
        while True:
            try:
                delete_name = input("\nEnter the name you want to delete : \n")
                break
            except KeyboardInterrupt:
                print("\nPlease try again.....")
                continue
        for line in lines:
            part = line.split("|")[0]
            name = part.split("-")[1].strip()
            if delete_name.lower() != name.lower():
                new_lines.append(line)
        updated_lines = []
        for i, line in enumerate(new_lines, start=1):    # "i" lines ko ek number deta hai jo "start = 1" 1 se start karwata hai.... 
            parts = line.split("|")
            name_part = parts[0].strip()
            class_part = parts[2].strip()
            updated_lines.append(f"{name_part} | Roll number - {i} | {class_part}\n")
        with open("students.txt", "w") as f:
            f.writelines(updated_lines)
        if len(updated_lines) == len(lines):
            print(f"There is no student with the name '{delete_name.capitalize()}'")
        else: 
            print("Deletation completed\n")
            return

    elif user_delete.lower() == "by roll":
        while True:
            try:
                delete_roll = int(input("\nEnter the roll number you want to delete : \n"))
                if delete_roll<=0:
                    print("Please enter a valid roll number !!\n")
                    continue
                else:
                    break
            except KeyboardInterrupt:
                print("\nPlease try again.....")
                continue
            except Exception:
                print("Please enter a valid roll number !!\n")
                continue
        for line in lines:
            roll = int(line.split("|")[1].split("-")[1].strip())
            if delete_roll != roll:
                new_lines.append(line)
        updated_lines = []
        for i, line in enumerate(new_lines, start = 1):
            parts = line.split("|")
            name_part = parts[0].strip()
            class_part = parts[2].strip()
            updated_lines.append (f"{name_part} | Roll number - {i} | {class_part}\n")
        with open("students.txt", "w") as f:
            f.writelines(updated_lines)
        if len(updated_lines) == len(lines):
            print(f"There is no student by roll {delete_roll}\n")
        else:
            print("Deletation completed\n")
            return



def menu():
    while True:
        try:
            choice = int(input("\nSelect one--\n1. Add student\n2. View student\n3. Delete student\n4. Exit\n\n\nyour choice - "))
            if choice<=0 or choice>=5:
                print("\nPlease enter a valid choice (1-4)")
                continue
        except KeyboardInterrupt:
            print("\nPlease try again !!")
            continue
        except Exception:
            print("\nPlease enter a valid number (1-4)\n")
            continue

        if choice==1:
            add_student()
        elif choice==2:
            view_student()
        elif choice==3:
            delete_student()
        elif choice==4:
            print("\n\nProgram closing...........\n")
            break


menu()








