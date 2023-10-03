import datetime
import os
import pickle

class Employee:
    def __init__(self, name, hourly_rate):
        global next_employee_number
        self.employee_number = next_employee_number
        next_employee_number += 1
        self.name = name
        self.hourly_rate = hourly_rate
        self.logged_in_time = None
        self.total_hours = 0

    def log_time(self):
        if not self.logged_in_time:
            self.logged_in_time = datetime.datetime.now()
            print(f"{self.name} (Employee #{self.employee_number}) logged in at {self.logged_in_time}")
        else:
            logged_out_time = datetime.datetime.now()
            hours_worked = (logged_out_time - self.logged_in_time).seconds / 3600
            self.total_hours += hours_worked
            print(f"{self.name} (Employee #{self.employee_number}) logged out at {logged_out_time}, worked for {hours_worked:.2f} hours.")
            self.logged_in_time = None

    def get_pay(self):
        overtime_hours = 0
        regular_hours = self.total_hours
        if self.total_hours > 40:
            overtime_hours = self.total_hours - 40
            regular_hours = 40
        regular_pay = regular_hours * self.hourly_rate
        overtime_pay = overtime_hours * self.hourly_rate * 1.5
        return regular_pay + overtime_pay

FILE_NAME = "employee_data.pkl"
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "rb") as file:
        employees, next_employee_number = pickle.load(file)
else:
    employees = {}
    next_employee_number = 1

def save_data():
    with open(FILE_NAME, "wb") as file:
        pickle.dump((employees, next_employee_number), file)

def menu():
    os.system('clear')  # This is for Unix-based systems. Use os.system('cls') for Windows.
    print("1. Add Employee")
    print("2. Clock In/Out")
    print("3. View Payroll")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter employee name: ")
        hourly_rate = float(input("Enter hourly rate: "))
        employee = Employee(name, hourly_rate)
        employees[employee.employee_number] = employee
        print(f"Employee {name} added with Employee Number: {employee.employee_number}")
        save_data()

    elif choice == "2":
        try:
            emp_num = int(input("Enter employee number: "))
            if emp_num in employees:
                employees[emp_num].log_time()
                save_data()
            else:
                print("Employee not found!")
        except ValueError:
            print("Please enter a valid employee number!")

    elif choice == "3":
        for emp_num, employee in employees.items():
            print(f"{employee.name} (Employee #{emp_num}) has worked {employee.total_hours:.2f} hours and is owed ${employee.get_pay():.2f}.")

    elif choice == "4":
        break
    else:
        print("Invalid choice!")

    input("\nPress enter to continue...")
