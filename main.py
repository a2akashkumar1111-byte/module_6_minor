import json
import csv
import os
import datetime

def get_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

sub = ["Python", "Maths", "DBMS"]
students = {}

def load_data():
    global students
    if os.path.exists("students.json"):
        with open("students.json", "r") as f:
            text = f.read()
            if text.strip() != "":
                with open("students.json", "r") as f2:
                    students = json.load(f2)
    else:
        students = {}

def write_log(msg):
    with open("activity_log.txt", "a") as f:
        f.write(f"[{get_time()}] {msg}\n")

def add_student():
    n = int(input("Number of students: "))
    for i in range(n):
        sid = input("Student ID: ").strip()
        if sid in students:
            print("Already exist")
            continue
        
        name = input("Students name: ").strip()
        dept = input("Department: ").strip()
        marks = []

        for j in range(len(sub)):
            m = int(input(f"{sub[j]} marks: "))
            while m < 0 or m > 100:
                print("out of range")
                m = int(input(f"{sub[j]} marks: "))
            marks.append(m)

        students[sid] = {
            "name": name,
            "department": dept,
            "marks": {
                "Python": marks[0],
                "Maths": marks[1],
                "DBMS": marks[2]
            }
        }
        write_log(f"Added student {sid}")

    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)
    print("Record saved to students.json")

def search_student():
    sid = input("Enter student id to search: ").strip()
    if sid in students:
        rec = students[sid]
        print(f"Name: {rec['name']} | Department: {rec['department']} | Marks: {rec['marks']}")
        s = json.dumps(rec)
        print("JSON string:", s)
        d = json.loads(s)
        print("Back to dict:", d)
    else:
        print("detail not found")

def show_all():
    if len(students) == 0:
        print("No records")
    else:
        for sid in students:
            print(sid, ":", students[sid])

def export_csv():
    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Student_id", "Name", "Department", "Python", "Maths", "DBMS"])
        for sid in students:
            writer.writerow([
                sid,
                students[sid]["name"],
                students[sid]["department"],
                students[sid]["marks"]["Python"],
                students[sid]["marks"]["Maths"],
                students[sid]["marks"]["DBMS"]
            ])
    print("CSV export completed: students.csv")
    write_log(f"Exported {len(students)} records")

def view_log():
    if not os.path.exists("activity_log.txt"):
        print("No log file")
        return
    print("\n-- read() --")
    with open("activity_log.txt", "r") as f:
        print(f.read())
    print("\n-- readline() --")
    with open("activity_log.txt", "r") as f:
        print(f.readline())
    print("\n-- readlines() --")
    with open("activity_log.txt", "r") as f:
        for line in f.readlines():
            print(line.strip())
    with open("activity_log.txt", "a") as f:
        f.write("write demo\n")
        f.writelines(["writelines line1\n", "writelines line2\n"])


load_data()

while True:
    print("\n1. Add student")
    print("2. Search student")
    print("3. Show all")
    print("4. Export CSV")
    print("5. View log")
    print("6. Exit")
    
    ch = input("Choice: ").strip()

    if ch == "1":
        add_student()
    elif ch == "2":
        search_student()
    elif ch == "3":
        show_all()
    elif ch == "4":
        export_csv()
    elif ch == "5":
        view_log()
    elif ch == "6":
        break
    else:
        print("Invalid choice")