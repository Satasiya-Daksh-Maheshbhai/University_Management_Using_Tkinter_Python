from tkinter import *
import tkinter.ttk as tk
import tkinter.messagebox as ms
main = Tk()

main.geometry("500x500")
main.minsize(500, 500)
main.title("University Management")
main['bg'] = '#E3F2FD'


s = {
    1: {'Name': 'Nirali', 'Department': 'IT', 'Current sem': 3, 'Mobile no': 9876546789},
    2: {'Name': 'Daksh', 'Department': 'CE', 'Current sem': 3, 'Mobile no': 9876593647},
    3: {'Name': 'Tanisha', 'Department': 'CSD', 'Current sem': 2, 'Mobile no': 9835472834},
    4: {'Name': 'Krisha', 'Department': 'CE', 'Current sem': 1, 'Mobile no': 9435118855},
    5: {'Name': 'Jinsi', 'Department': 'IT', 'Current sem': 2, 'Mobile no': 9435118890}
}
f = {
    1: {'Name': 'Nirali', 'Subject': 'FSD', 'Mobile no': 9876546789},
    2: {'Name': 'Daksh', 'Subject': 'Maths', 'Mobile no': 9876593647},
    3: {'Name': 'Tanisha', 'Subject': 'Python', 'Mobile no': 9835472834},
    4: {'Name': 'Krisha', 'Subject': 'Physics', 'Mobile no': 9435118855},
    5: {'Name': 'Jisni', 'Subject': 'Java', 'Mobile no': 9435118890}
}

def student_panel():
    clear()
    frame = Frame(main, bg="#dcedc8", padx=20, pady=10, relief=RIDGE, borderwidth=5)
    frame.pack(expand=True)
    Label(frame, text="Student Panel", font=('Arial', 30, 'bold'), bg="#dcedc8").pack(pady=10)
    Button(frame, text="Add Student", bg="#4CAF50", fg="white", relief=SUNKEN, command=add_student).pack(pady=10)
    Button(frame, text="Search Student", bg="#4CAF50", fg="white", relief=SUNKEN, command=search_student).pack(pady=10)
    Button(frame, text="Delete Student", bg="#4CAF50", fg="white", relief=SUNKEN, command=delete_student).pack(pady=10)
    Button(frame, text="Display Student", bg="#4CAF50", fg="white", relief=SUNKEN, command=display_all_students).pack(pady=10)
    Button(frame, text="Back", bg="black", fg="#dcedc8", relief=SUNKEN, command=admin).pack(pady=10)

def add_student():
    clear()
    global roll_number_entry, name_entry, dept_entry, sem_entry, mobile_entry

    def submit_student():
        student_id = int(roll_number_entry.get())
        if student_id in s:
            ms.showerror("Error", "Student with this Roll Number already exists!")
        else:
            name = name_entry.get()
            department = dept_entry.get()
            sem = sem_entry.get()
            mobile = mobile_entry.get()

            if name and department and sem and is_mobile(mobile):
                s[student_id] = {
                    'Name': name,
                    'Department': department,
                    'Current sem': sem,
                    'Mobile no': mobile
                }
                ms.showinfo("Success", "Student added successfully!")
                student_panel()
            else:
                ms.showerror("Error", "Please fill all fields correctly!")

    frame = Frame(main, bg="#dcedc8", padx=20, pady=10, relief=RIDGE, borderwidth=5)
    frame.pack(expand=True)
    Label(frame, text="Add Student", font=('Arial', 30, 'bold'), bg="#dcedc8").pack(pady=10)
    Label(frame, text="Roll Number:", font=('Arial', 12), bg="#dcedc8").pack(pady=5)
    roll_number_entry = Entry(frame)
    roll_number_entry.pack(pady=5)
    Label(frame, text="Name:", font=('Arial', 12), bg="#dcedc8").pack(pady=5)
    name_entry = Entry(frame)
    name_entry.pack(pady=5)
    Label(frame, text="Department:", font=('Arial', 12), bg="#dcedc8").pack(pady=5)
    dept_entry = Entry(frame)
    dept_entry.pack(pady=5)
    Label(frame, text="Semester:", font=('Arial', 12), bg="#dcedc8").pack(pady=5)
    sem_entry = Entry(frame)
    sem_entry.pack(pady=5)
    Label(frame, text="Mobile No:", font=('Arial', 12), bg="#dcedc8").pack(pady=5)
    mobile_entry = Entry(frame)
    mobile_entry.pack(pady=5)
    submit_btn = Button(frame, text="Submit", bg="green", fg="white", command=submit_student).pack(pady=10)
    back_btn = Button(frame, text="Back", bg="black", fg="#dcedc8", relief=SUNKEN, command=student_panel).pack(pady=10)

def search_student():
    clear()
    global search_entry

    def search():
        roll_no = int(search_entry.get())
        if roll_no in s:
            details = s[roll_no]
            ms.showinfo("Student Found", f"Student Details:\nName: {details['Name']}\nDepartment: {details['Department']}\nSemester: {details['Current sem']}\nMobile: {details['Mobile no']}")
        else:
            ms.showerror("Error", "Student not found!")

    frame = Frame(main, bg="#dcedc8", padx=20, pady=10, relief=RIDGE, borderwidth=5)
    frame.pack(expand=True)
    Label(frame, text="Search Student", font=('Arial', 30, 'bold'), bg="#dcedc8").pack(pady=10)
    Label(frame, text="Enter Roll Number:", font=('Arial', 12), bg="#dcedc8").pack(pady=5)
    search_entry = Entry(frame)
    search_entry.pack(pady=5)
    search_btn = Button(frame, text="Search", bg="blue", fg="white", command=search).pack(pady=10)
    back_btn = Button(frame, text="Back", bg="black", fg="#dcedc8", relief=SUNKEN, command=student_panel).pack(pady=10)


def delete_student():
    global delete_entry

    def delete():
        student_id = int(delete_entry.get())

        if student_id in s:
            del s[student_id]
            ms.showinfo("Success", "Student deleted successfully!")
            student_panel()
        else:
            ms.showerror("Error", "Student not found!")

    clear()
    frame = Frame(main, bg="#dcedc8", padx=20, pady=10, relief=RIDGE, borderwidth=5)
    frame.pack(expand=True)

    Label(frame, text="Delete Student", font=('Arial', 30, 'bold'), bg="#dcedc8").pack(pady=10)

    Label(frame, text="Enter Roll Number:", font=('Arial', 12), bg="#dcedc8").pack(pady=5)
    delete_entry = Entry(frame)
    delete_entry.pack(pady=5)

    delete_btn = Button(frame, text="Delete", bg="red", fg="white", command=delete)
    delete_btn.pack(pady=10)

    back_btn = Button(frame, text="Back", bg="black", fg="#dcedc8", relief=SUNKEN, command=student_panel).pack(pady=10)



def display_all_students():
    clear()
    frame = Frame(main, bg="#dcedc8", padx=20, pady=10, relief=RIDGE, borderwidth=5)
    frame.pack(expand=True)
    table = tk.Treeview(frame, columns=("Roll No", "Name", "Department", "Semester", "Mobile"), show="headings")
    table.pack(pady=20)
    table.heading("Roll No", text="Roll No")
    table.heading("Name", text="Name")
    table.heading("Department", text="Department")
    table.heading("Semester", text="Semester")
    table.heading("Mobile", text="Mobile No")
    for roll_no, student in s.items():
        table.insert("", "end", values=(roll_no, student["Name"], student["Department"], student["Current sem"], student["Mobile no"]))
    back_btn = Button(frame, text="Back", bg="black", fg="#dcedc8", relief=SUNKEN, command=student_panel)
    back_btn.pack(pady=10)

# -----------------------------------------------------------------------------------------------------------------------


def faculty_panel():
    clear()
    frame = Frame(main, bg="#dcedc8", padx=20, pady=10, relief=RIDGE, borderwidth=5)
    frame.pack(expand=True)
    Label(frame, text="Faculty Panel", font=('Arial', 30, 'bold'), bg="#dcedc8").pack(pady=10)
    Button(frame, text="Add Faculty", bg="#008CBA", fg="white", relief=SUNKEN, command=add_faculty).pack(pady=10)
    Button(frame, text="Search Faculty", bg="#008CBA", fg="white", relief=SUNKEN, command=search_faculty).pack(pady=10)
    Button(frame, text="Delete Faculty", bg="#008CBA", fg="white", relief=SUNKEN, command=delete_faculty).pack(pady=10)
    Button(frame, text="Display Faculty", bg="#008CBA", fg="white", relief=SUNKEN, command=display_all_faculty).pack(pady=10)
    Button(frame, text="Back", bg="black", fg="#dcedc8", relief=SUNKEN, command=admin).pack(pady=10)


def add_faculty():
    clear()
    global faculty_id_entry, name_entry, subject_entry, mobile_entry
    def submit_faculty():
        faculty_id = int(faculty_id_entry.get())
        if faculty_id in f:
            ms.showerror("Error", "Faculty with this ID already exists!")
        else:
            name = name_entry.get()
            subject = subject_entry.get()
            mobile = mobile_entry.get()
            if name and subject and is_mobile(mobile):
                f[faculty_id] = {
                    'Name': name,
                    'Subject': subject,
                    'Mobile no': mobile
                }
                ms.showinfo("Success", "Faculty added successfully!")
                faculty_panel()
            else:
                ms.showerror("Error", "Please fill all fields correctly!")
    frame = Frame(main, bg="#dcedc8", padx=20, pady=10, relief=RIDGE, borderwidth=5)
    frame.pack(expand=True)
    Label(frame, text="Add Faculty", font=('Arial', 30, 'bold'), bg="#dcedc8").pack(pady=10)
    Label(frame, text="Faculty ID:", font=('Arial', 12), bg="#dcedc8").pack(pady=5)
    faculty_id_entry = Entry(frame)
    faculty_id_entry.pack(pady=5)
    Label(frame, text="Name:", font=('Arial', 12), bg="#dcedc8").pack(pady=5)
    name_entry = Entry(frame)
    name_entry.pack(pady=5)
    Label(frame, text="Subject:", font=('Arial', 12), bg="#dcedc8").pack(pady=5)
    subject_entry = Entry(frame)
    subject_entry.pack(pady=5)
    Label(frame, text="Mobile No:", font=('Arial', 12), bg="#dcedc8").pack(pady=5)
    mobile_entry = Entry(frame)
    mobile_entry.pack(pady=5)
    submit_btn = Button(frame, text="Submit", bg="green", fg="white", command=submit_faculty).pack(pady=10)
    back_btn = Button(frame, text="Back", bg="black", fg="#dcedc8", relief=SUNKEN, command=faculty_panel).pack(pady=10)


def search_faculty():
    clear()
    global search_entry
    def search():
        faculty_id = int(search_entry.get())
        if faculty_id in f:
            details = f[faculty_id]
            ms.showinfo("Faculty Found", f"Faculty Details:\nName: {details['Name']}\nSubject: {details['Subject']}\nMobile: {details['Mobile no']}")
        else:
            ms.showerror("Error", "Faculty not found!")
    frame = Frame(main, bg="#dcedc8", padx=20, pady=10, relief=RIDGE, borderwidth=5)
    frame.pack(expand=True)
    Label(frame, text="Search Faculty", font=('Arial', 30, 'bold'), bg="#dcedc8").pack(pady=10)
    Label(frame, text="Enter Faculty ID:", font=('Arial', 12), bg="#dcedc8").pack(pady=5)
    search_entry = Entry(frame)
    search_entry.pack(pady=5)
    search_btn = Button(frame, text="Search", bg="blue", fg="white", command=search).pack(pady=10)
    back_btn = Button(frame, text="Back", bg="black", fg="#dcedc8", relief=SUNKEN, command=faculty_panel).pack(pady=10)

def delete_faculty():
    global delete_entry
    def delete():
        faculty_id = int(delete_entry.get())
        if faculty_id in f:
            del f[faculty_id]
            ms.showinfo("Success", "Faculty deleted successfully!")
            faculty_panel()
        else:
            ms.showerror("Error", "Faculty not found!")
    clear()
    frame = Frame(main, bg="#dcedc8", padx=20, pady=10, relief=RIDGE, borderwidth=5)
    frame.pack(expand=True)
    Label(frame, text="Delete Faculty", font=('Arial', 30, 'bold'), bg="#dcedc8").pack(pady=10)
    Label(frame, text="Enter Faculty ID:", font=('Arial', 12), bg="#dcedc8").pack(pady=5)
    delete_entry = Entry(frame)
    delete_entry.pack(pady=5)
    delete_btn = Button(frame, text="Delete", bg="red", fg="white", command=delete)
    delete_btn.pack(pady=10)
    back_btn = Button(frame, text="Back", bg="black", fg="#dcedc8", relief=SUNKEN, command=faculty_panel).pack(pady=10)


def display_all_faculty():
    clear()
    frame = Frame(main, bg="#dcedc8", padx=20, pady=10, relief=RIDGE, borderwidth=5)
    frame.pack(expand=True)
    table = tk.Treeview(frame, columns=("Faculty ID", "Name", "Subject", "Mobile"), show="headings", height=10)
    table.pack(pady=20)
    table.heading("Faculty ID", text="Faculty ID")
    table.heading("Name", text="Name")
    table.heading("Subject", text="Subject")
    table.heading("Mobile", text="Mobile No")
    for item in table.get_children():
        table.delete(item)
    for faculty_id, faculty in f.items():
        table.insert("", "end", values=(faculty_id, faculty["Name"], faculty["Subject"], faculty["Mobile no"]))

    back_btn = Button(frame, text="Back", bg="black", fg="#dcedc8", relief=SUNKEN, command=faculty_panel)
    back_btn.pack(pady=10)


# --------------------------------------------------------------------------------------------------------------------------



def log_out():
    clear()
    login_ui()

def admin():
    clear()
    frame = Frame(main, bg="#dcedc8", padx=20, pady=10, relief=RIDGE, borderwidth=5)
    frame.pack(expand=True)
    Label(frame, text="Welcome Admin", font=('Arial', 30, 'bold'), bg="#dcedc8").pack(pady=10)
    Button(frame, text="Manage Students", bg="#4CAF50", fg="white", relief=SUNKEN, command=student_panel).pack(pady=10)
    Button(frame, text="Manage Faculty", bg="#008CBA", fg="white", relief=SUNKEN, command=faculty_panel).pack(pady=10)
    Button(frame, text="Log-out", bg="red", fg="white", relief=SUNKEN, command=log_out).pack(pady=10)

def is_mobile(mobile):
    if mobile.isdigit() and len(mobile) == 10:
        return True
    else:
        return False

def clear():
    for i in main.winfo_children():
        i.destroy()

def log_in():
    u = user_name.get()
    p = pass_word.get()

    if u == "1234" and p == "1234":
        ms.showinfo("Success", "Login successful")
        admin()
    else:
        ms.showerror("Error", "Invalid values")

def login_ui():
    frame = Frame(main, bg="#dcedc8", padx=20, pady=10, relief=RIDGE, borderwidth=5)
    frame.pack(expand=True)

    Label(frame, text="University Management", font=('Arial', 30, 'bold'), bg="#dcedc8").pack(pady=10)
    Label(frame, text="Log-in", font=('Arial', 20, 'bold'), bg="#dcedc8").pack(padx=10, pady=20)

    uname = Label(frame, text="Username : ", font=('Arial', 10, 'bold'), bg="#dcedc8").pack()

    global user_name, pass_word
    user_name = StringVar()
    pass_word = StringVar()
    user_entry = Entry(frame, textvariable=user_name)
    user_entry.pack()
    password = Label(frame, text="Password : ", font=('Arial', 10, 'bold'), bg="#dcedc8").pack()
    pass_entry = Entry(frame, show="*", textvariable=pass_word)
    pass_entry.pack()
    Button(frame, text="Submit", bg="black", fg="#dcedc8", relief=SUNKEN, command=log_in).pack(pady=30)

login_ui()
main.mainloop()