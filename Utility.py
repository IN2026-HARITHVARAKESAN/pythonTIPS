import os
from datetime import datetime

from User import User


class Utility:
    users = [User(1, "Harith", "Harith")]
    Upcoming_UserId = 2
    employees = []
    tasks = []
    schedule = []
    Upcoming_EmployeeId = 1
    Upcoming_TaskId = 1
    log_file = "application.log"

    @staticmethod
    def log(message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(Utility.log_file, "a", encoding="utf-8") as file:
            file.write(f"{timestamp} - {message}\n")