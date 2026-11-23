"""Run the employee and task scheduling command-line application."""

import csv
import json
import os
import sys
from datetime import date, datetime, timedelta

from AccessManager import AccessManager
from Employee import Employee
from Task import Task
from Utility import Utility


def get_hours(prompt):
    """Read and validate a positive number of working hours."""
    try:
        hours = float(input(prompt))
        if hours > 0:
            return hours
    except ValueError:
        pass
    print("Enter a number greater than zero.")
    return None

def get_skills(prompt):
    """Read comma-separated skills from the user."""
    return [
        skill.strip().lower()
        for skill in input(prompt).split(",")
        if skill.strip()
    ]

def add_employee():
    """Ask for employee details and add a new employee."""
    name = input("Enter employee name: ").strip()
    hours = get_hours("Enter working hours per day: ")
    if not name or hours is None:
        print("Employee was not added.")
        return

    skills = get_skills("Enter skills separated by commas: ")
    days = input("Enter available weekdays separated by commas, or All: ").strip()
    if not days or days.lower() == "all":
        availability = "All"
    else:
        availability = [day.strip().lower() for day in days.split(",") if day.strip()]

    employee = Employee(
        Utility.Upcoming_EmployeeId, name, hours, skills, availability
    )
    Utility.employees.append(employee)
    Utility.Upcoming_EmployeeId += 1
    Utility.log("Added employee " + name)
    print("Employee added with ID", employee.id)

def show_employees():
    """Display all employees and their availability."""
    if not Utility.employees:
        print("No employees added yet.")
        return

    for employee in Utility.employees:
        days = (
            "All" if employee.availability == "All"
            else ", ".join(employee.availability)
        )
        print(
            employee.id, employee.name, "-", employee.hours, "hours/day;",
            "skills:", ", ".join(employee.skills), "; available:", days
        )

def add_task():
    """Ask for task details and add a new task."""
    description = input("Task description: ").strip()
    hours = get_hours("Required hours: ")
    if not description or hours is None:
        print("Task was not added.")
        return

    try:
        deadline = datetime.strptime(
            input("Deadline (YYYY-MM-DD): ").strip(), "%Y-%m-%d"
        ).date()
        if deadline < date.today():
            raise ValueError
    except ValueError:
        print("Enter a valid deadline today or later (YYYY-MM-DD).")
        return

    task = Task(
        Utility.Upcoming_TaskId,
        description,
        hours,
        deadline.isoformat(),
        get_skills("Required skills separated by commas: "),
    )
    Utility.tasks.append(task)
    Utility.Upcoming_TaskId += 1
    Utility.log("Added task " + description)
    print("Task added with ID", task.id)

def show_tasks():
    """Display all tasks and their current status."""
    if not Utility.tasks:
        print("No tasks added yet.")
        return

    for task in Utility.tasks:
        print(
            task.id, task.description, "-", task.hours, "hours; due",
            task.deadline, "; skills:", ", ".join(task.skills), ";", task.status
        )

def schedule_tasks():
    """Assign tasks by deadline, skills, availability, and free hours."""
    Utility.schedule = []
    today = date.today()

    for task in sorted(Utility.tasks, key=lambda item: item.deadline):
        task.status = "Pending"
        task.reason = ""
        remaining = task.hours
        deadline = datetime.strptime(task.deadline, "%Y-%m-%d").date()
        assignments = []
        skilled = [
            employee for employee in Utility.employees
            if set(task.skills).issubset(set(employee.skills))
        ]

        day = today
        while day <= deadline and remaining > 0:
            available = [
                employee for employee in skilled
                if employee.is_available(day)
            ]
            available.sort(key=lambda employee: sum(
                item["hours"] for item in Utility.schedule + assignments
                if item["employee_id"] == employee.id
            ))

            for employee in available:
                date_text = day.isoformat()
                used = sum(
                    item["hours"] for item in Utility.schedule + assignments
                    if item["employee_id"] == employee.id
                    and item["date"] == date_text
                )
                free = employee.hours - used
                if free <= 0:
                    continue

                assigned = min(remaining, free)
                assignments.append({
                    "task_id": task.id,
                    "description": task.description,
                    "employee_id": employee.id,
                    "employee_name": employee.name,
                    "date": date_text,
                    "hours": assigned,
                    "deadline": task.deadline,
                })
                remaining -= assigned
                if remaining <= 0:
                    break

            day += timedelta(days=1)

        if remaining > 0:
            task.status = "Unscheduled"
            task.reason = (
                "No employee has the required skills."
                if not skilled else "Not enough available working hours."
            )
        else:
            task.status = "Scheduled"
            Utility.schedule.extend(assignments)

    Utility.log("Ran scheduler")
    print("Scheduling complete.")

def show_schedule():
    """Display the generated employee task schedule."""
    if not Utility.schedule:
        print("No schedule. Run the scheduler first.")
        return

    for item in sorted(Utility.schedule, key=lambda row: row["date"]):
        print(
            item["date"], "|", item["employee_name"], "|",
            item["description"], "|", item["hours"], "hours"
        )

def show_reports():
    """Display unscheduled tasks, overworked employees, and deadlines."""
    print("\nTasks that could not be scheduled:")
    unscheduled = [task for task in Utility.tasks if task.status == "Unscheduled"]
    if unscheduled:
        for task in unscheduled:
            print("-", task.description, ":", task.reason)
    else:
        print("- None")

    print("\nEmployees over their daily hours:")
    found = False
    for employee in Utility.employees:
        days = {
            item["date"] for item in Utility.schedule
            if item["employee_id"] == employee.id
        }
        for day in days:
            total = sum(
                item["hours"] for item in Utility.schedule
                if item["employee_id"] == employee.id and item["date"] == day
            )
            if total > employee.hours:
                print("-", employee.name, "on", day, ":", total, "hours")
                found = True
    if not found:
        print("- None")

    print("\nDeadlines in the next 7 days:")
    today = date.today()
    upcoming = [
        task for task in Utility.tasks
        if today <= datetime.strptime(task.deadline, "%Y-%m-%d").date()
        <= today + timedelta(days=7)
    ]
    for task in sorted(upcoming, key=lambda item: item.deadline):
        print("-", task.description, ":", task.deadline, "-", task.status)
    if not upcoming:
        print("- None")

def export_data():
    """Save employees, tasks, and the schedule as JSON and CSV."""
    filename = input("Export file [data.json]: ").strip() or "data.json"
    if not filename.lower().endswith(".json"):
        filename += ".json"

    data = {
        "employees": [employee.to_dict() for employee in Utility.employees],
        "tasks": [task.to_dict() for task in Utility.tasks],
        "schedule": Utility.schedule,
    }
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    csv_name = os.path.splitext(filename)[0] + "_schedule.csv"
    with open(csv_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Employee", "Task", "Hours", "Deadline"])
        for item in Utility.schedule:
            writer.writerow([
                item["date"], item["employee_name"], item["description"],
                item["hours"], item["deadline"],
            ])

    Utility.log("Exported data to " + filename)
    print("Saved", filename, "and", csv_name)

def import_data():
    """Load employees, tasks, and a schedule from a JSON file."""
    filename = input("Import file [data.json]: ").strip() or "data.json"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        Utility.employees = [
            Employee(
                item["id"], item["name"], item["hours"], item["skills"],
                item.get("availability", "All"),
            )
            for item in data["employees"]
        ]
        Utility.tasks = [
            Task(
                item["id"], item["description"], item["hours"],
                item["deadline"], item["skills"],
            )
            for item in data["tasks"]
        ]
        for task, item in zip(Utility.tasks, data["tasks"]):
            task.status = item.get("status", "Pending")
            task.reason = item.get("reason", "")

        Utility.schedule = data.get("schedule", [])
        Utility.Upcoming_EmployeeId = max(
            [employee.id for employee in Utility.employees], default=0
        ) + 1
        Utility.Upcoming_TaskId = max(
            [task.id for task in Utility.tasks], default=0
        ) + 1
        Utility.log("Imported data from " + filename)
        print("Data imported.")
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("Could not import data:", error)

def show_logs():
    """Display the latest application log messages."""
    try:
        with open(Utility.log_file, "r", encoding="utf-8") as file:
            print("".join(file.readlines()[-20:]) or "No logs.")
    except FileNotFoundError:
        print("No logs yet.")

def main_menu():
    """Display the main menu and run the selected action."""
    actions = {
        "1": ("Add employee", add_employee),
        "2": ("View employees", show_employees),
        "3": ("Add task", add_task),
        "4": ("View tasks", show_tasks),
        "5": ("Run scheduler", schedule_tasks),
        "6": ("View schedule", show_schedule),
        "7": ("Reports", show_reports),
        "8": ("Import data", import_data),
        "9": ("Export data", export_data),
        "10": ("View logs", show_logs),
    }

    while True:
        print("\nMAIN MENU")
        for number, (label, _) in actions.items():
            print(number + ".", label)
        print("0. Exit")
        choice = input("Choose: ").strip()
        if choice == "0":
            Utility.log("Application exited")
            return
        if choice in actions:
            label = actions[choice][0]
            Utility.log("Selected action: " + label)
            actions[choice][1]()
        else:
            print("Invalid choice.")

def main():
    """Display the login menu and start the application."""
    while True:
        print("\n1. Login\n2. Sign up\n3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            if AccessManager.Login():
                main_menu()
                return
        elif choice == "2":
            AccessManager.SignUp()
        elif choice == "3":
            Utility.log("Application exited")
            sys.exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
