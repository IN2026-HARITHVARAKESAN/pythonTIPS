"""Store shared application data and write activity logs."""

import os
from datetime import datetime

from User import User

class Utility:
    """Keep users, employees, tasks, schedules, and application settings."""

    users = [User(1, "Harith", "Harith")]
    Upcoming_UserId = 2
    employees = []
    tasks = []
    schedule = []
    Upcoming_EmployeeId = 1
    Upcoming_TaskId = 1
    current_user = None
    module_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(module_dir).lower() == "__pycache__":
        module_dir = os.path.dirname(module_dir)
    log_file = os.path.join(module_dir, "application.log")

    @staticmethod
    def log(message):
        """Write a timestamped message to the application log."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if Utility.current_user is not None:
            actor = (
                f"User {Utility.current_user.name} "
                f"(ID {Utility.current_user.id})"
            )
            message = f"{actor} - {message}"
        with open(Utility.log_file, "a", encoding="utf-8") as file:
            file.write(f"{timestamp} - {message}\n")