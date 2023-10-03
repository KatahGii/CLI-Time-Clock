# CLITimeClock

<img width="682" alt="Screenshot 2023-10-03 at 11 53 41 AM" src="https://github.com/KatahGii/CLI-Time-Clock/assets/70392903/74e2ce44-dfef-4062-b298-d98934dadae4">

## **CLI-Based Payroll and Time Clock System**

This program allows employers to manage a basic payroll system with the ability to add employees, log their clock-in/clock-out times, calculate overtime pay, and view total owed salaries.

### **Functionalities**

1. **Add Employee**: This option lets you add an employee to the system. Every employee has a unique ID, name, and hourly wage. The employee's total working hours and logged-in time are tracked internally.

2. **Clock In/Out**: An employee can clock in or clock out using their unique ID. The system automatically calculates the total hours they've worked each session and accumulates it.

3. **View Payroll**: The employer can view the total hours each employee has worked and their total salary owed. If an employee has worked over 40 hours, the additional hours are considered as overtime, which is paid 1.5x the regular hourly wage.

4. **Exit**: This option lets you exit the system.

### **Screens**

1. **Main Menu**: This is the primary screen users see. It displays the four functionalities mentioned above.

2. **Add Employee Screen**:
   - Prompt to input the employee's name.
   - Prompt to input the hourly wage for the employee.
   - Displays a confirmation message with the employee's unique ID once added.

3. **Clock In/Out Screen**:
   - Prompt to input the employee's unique ID.
   - If the ID matches an existing employee and they're currently clocked out, it will clock them in. If they're clocked in, it will clock them out.
   - Displays confirmation of the clock-in/clock-out along with the timestamp and total hours worked for that session (if clocking out).

4. **View Payroll Screen**:
   - Lists all employees, their total hours worked, and their total salary owed. Overtime is clearly marked.

5. **Exit Screen**: Closes the application.

### **Technical Details**

- **Persistence**: Employee data is saved in a serialized format using Python's `pickle` module. The file `employee_data.pkl` is used to store this data.

- **Compatibility**: The code uses the `os.system('clear')` command to clear the terminal, which works on Unix-like systems. For Windows, replace this with `os.system('cls')`.


## **Legal Disclaimer**

This CLI-Based Payroll and Time Clock System is provided as a demonstration and for educational purposes only. It is not a regulation time clock and should not be used as a replacement for professional timekeeping systems or legal consultation. The creator and contributors make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability of this software for any purpose. Any reliance you place on such software is strictly at your own risk. Always consult with legal counsel and comply with local, state, and federal regulations related to employment and timekeeping.

---
