import os
import pickle
import datetime

class TimeLog:
    def __init__(self):
        self.clock_in = datetime.datetime.now()
        self.clock_out = None

class Employee:
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate
        self.time_logs = []

    def log_time(self):
        if not self.time_logs or self.time_logs[-1].clock_out:
            self.time_logs.append(TimeLog())
            print(f"Clocked in at {self.time_logs[-1].clock_in}")
        else:
            self.time_logs[-1].clock_out = datetime.datetime.now()
            print(f"Clocked out at {self.time_logs[-1].clock_out}")

    def get_total_hours(self):
        total_seconds = sum([(log.clock_out - log.clock_in).total_seconds() for log in self.time_logs if log.clock_out])
        return total_seconds / 3600

    def get_pay(self):
        return self.get_total_hours() * self.hourly_rate

def display_edit_screen(employee):
    while True:
        os.system('clear')
        print(f"Editing time logs for {employee.name}")

        # Get unique dates
        unique_dates = sorted(list(set([log.clock_in.date() for log in employee.time_logs])))

        # Print headers
        print("\nEntry No. |", " | ".join([date.strftime("%Y-%m-%d") for date in unique_dates]))

        # Print times for each date
        for i, log in enumerate(employee.time_logs, 1):
            times_for_date = [f"{log.clock_in.time()} - {log.clock_out.time() if log.clock_out else 'Not logged out'}" if log.clock_in.date() == date else "" for date in unique_dates]
            print(f"{i}.       |", " | ".join(times_for_date))

        try:
            entry_num = int(input("\nEnter the number of the entry you want to edit (0 to go back): "))

            if entry_num == 0:
                break
            elif 0 < entry_num <= len(employee.time_logs):
                selected_log = employee.time_logs[entry_num - 1]

                # Editing only times, not dates
                new_clock_in_time = input(f"Enter new Clock In TIME for entry {entry_num} (HH:MM:SS or leave empty for no change): ")
                new_clock_out_time = input(f"Enter new Clock Out TIME for entry {entry_num} (HH:MM:SS or 'none' for not logged out, or leave empty for no change): ")

                if new_clock_in_time:
                    time_parts = [int(part) for part in new_clock_in_time.split(':')]
                    selected_log.clock_in = selected_log.clock_in.replace(hour=time_parts[0], minute=time_parts[1], second=time_parts[2])

                if new_clock_out_time == 'none':
                    selected_log.clock_out = None
                elif new_clock_out_time:
                    time_parts = [int(part) for part in new_clock_out_time.split(':')]
                    selected_log.clock_out = selected_log.clock_in.replace(hour=time_parts[0], minute=time_parts[1], second=time_parts[2])

        except ValueError:
            print("Please enter a valid number.")
            input("\nPress enter to try again...")


def save_data():
    with open('employee_data.pkl', 'wb') as file:
        pickle.dump((employees, next_employee_number), file)

def load_data():
    try:
        with open('employee_data.pkl', 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}, 1

def main_menu():
    global employees
    global next_employee_number

    while True:
        os.system('clear')
        print("Time Clock System")
        print("1. Clock In/Out")
        print("2. Add Employee")
        print("3. View Payroll")
        print("4. Edit Clock In/Out Times")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            emp_num = int(input("Enter your employee number: "))
            if emp_num in employees:
                employees[emp_num].log_time()
            else:
                print("Employee not found!")
            save_data()

        elif choice == "2":
            name = input("Enter employee name: ")
            hourly_rate = float(input("Enter hourly rate: "))
            employees[next_employee_number] = Employee(name, hourly_rate)
            print(f"Employee added with number: {next_employee_number}")
            next_employee_number += 1
            save_data()

        elif choice == "3":
            for emp_num, employee in employees.items():
                total_hours = employee.get_total_hours()
                pay_due = employee.get_pay()
                print(f"Employee {employee.name} ({emp_num}): {total_hours:.2f} hours worked. Pay due: ${pay_due:.2f}")

        elif choice == "4":
            emp_num = int(input("Enter employee number to edit times: "))
            if emp_num in employees:
                display_edit_screen(employees[emp_num])
                save_data()
            else:
                print("Employee not found!")

        elif choice == "5":
            break

        else:
            print("Invalid choice!")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    employees, next_employee_number = load_data()
    main_menu()
